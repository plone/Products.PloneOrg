# VCL file optimized for Plone with a webserver in front.  See vcl(7) for details

#Default backend is nginx on port 80:

backend default {
	.host = "127.0.0.1";
	.port = "80";
}

# Define a sub to handle requests where we ignore cache-control headers.  Now
# we don't have to put the check for a 200 status code in every content type:
sub override {
    if (obj.status == 200) {
	deliver;	
    }
    pass;
}

acl purge {
    "localhost";
    "127.0.0.1";
}

sub vcl_recv {

  set req.backend = default;
  set req.grace = 120s;

    if (req.request == "PURGE") {
            if (!client.ip ~ purge) {
                    error 405 "Not allowed.";
            }
            purge_url(req.url);
	    error 200 "Purged";
    }
    if (req.request != "GET" && req.request != "HEAD") {
        /* We only deal with GET and HEAD by default */
        pass;
    }
    if (req.restarts != 0) {
        /* We only restart if we get a 500 error, serve our custom page instead */
        set req.url = "/500.html";
    }
    lookup;
}

sub vcl_hit {
    if (req.request == "PURGE") {
	set obj.ttl = 0s;
	error 200 "Purged";
    }
    if (!obj.cacheable) {
        set obj.http.X-Varnish-Action = "PASS (not cacheable - hit)";
        pass;
    }
    if (obj.http.Cache-Control ~ "(stale-while-revalidate|no-transform)") {
    	# This is a special cache. Don't serve to authenticated.
    	if (req.http.Cookie ~ "__ac=" || req.http.Authorization) {
    		set obj.http.X-Varnish-Action = "PASS (special not cacheable - hit)";
                	pass;
                }
        }

    set obj.http.X-Varnish-Action = "HIT (deliver - from cache)";
    deliver;
}

sub vcl_miss {
    if (req.request == "PURGE") {
            error 404 "Not in cache.";
    }
    fetch;
}

sub vcl_fetch {
    if (obj.status == 500) {
        /* This is probably an html parsing error in the nginx transform, serve our custom page instead */
        restart;
    }
    if (req.url == "/500.html") {
        set obj.status = 500;
        set obj.response = "Internal Server Error";
        pass;
    }
    if (obj.http.Cache-Control ~ "(stale-while-revalidate|no-transform)") {
            # Leveraging a non-varnish token to set a minimum ttl without contaminating s-maxage
            # Wouldn't need this if varnish supported Surrogate-Control
            if (obj.ttl < 3600s) {
                    set obj.http.X-Varnish-Special = "SPECIAL (local proxy for 1 hour)";
                    unset obj.http.expires;
                    set obj.ttl = 3600s;
                    # Add reset marker
                    set obj.http.reset-age = "1";
            }
    }

    if (req.url ~ "\.(jpg|jpeg|gif|png|tiff|tif|svg|swf|ico|css|js|vsd|doc|ppt|pps|xls|pdf|mp3|mp4|m4a|ogg|mov|avi|wmv|sxw|zip|gz|bz2|tgz|tar|rar|odc|odb|odf|odg|odi|odp|ods|odt|sxc|sxd|sxi|sxw|dmg|torrent|deb|msi|iso|rpm)$") {
	set obj.ttl = 600s;
	call override;
    }
    if (obj.http.Content-Type ~ "image.*$") {
	set obj.ttl = 600s;
        call override;
    }
    if (obj.http.Set-Cookie) {
            set obj.http.X-Varnish-Action = "FETCH (pass - response sets cookie)";
            pass;
    }
    if (req.http.Authorization && !obj.http.Cache-Control ~ "public") {
            set obj.http.X-Varnish-Action = "FETCH (pass - authorized and no public cache control)";
            pass;
    }
    if (obj.http.cookie ~ "__ac.*$") {
        pass;
    }
    if (!obj.cacheable) {
	set obj.http.X-Varnish-Action = "FETCH (pass - not cacheable)";
        pass;
    }
    set obj.prefetch =  -30s;
    deliver;
}

sub vcl_error {
    set obj.http.Content-Type = "text/html; charset=utf-8";
    synthetic {"
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <title>"} obj.status " " obj.response {"</title>
  </head>
  <body>
    <h1>Error "} obj.status " " obj.response {"</h1>
    <p>"} obj.response {"</p>
    <h3>Guru Meditation:</h3>
    <p>XID: "} req.xid {"</p>
    <address><a href="http://www.varnish-cache.org/">Varnish</a></address>
  </body>
</html>
"};
    deliver;
}
