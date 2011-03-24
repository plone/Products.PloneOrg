$(function(){
    var url = window.location.href;
    $("#login-link").click(function() {
        // the login template is static html so we define came_from
        // here as there is no TAL available
        $('#came-from-input').val(url);
        $("#login-popup").slideToggle();
        return false;
    });
    $("#login-slide-form").submit(function(){
    // for testing purposes, we want the form action to point to
    // /plone.org/login_form if we are local or staging
    if(url.indexOf('http://plone.org') != 0 && url.indexOf('https://plone.org') != 0){
        if(url.indexOf('http://staging.plone.org') == 0 || url.indexOf('https://staging.plone.org') == 0){
            $(this).attr('action', 'https://staging.plone.org/login_form');
        } else {
            $(this).attr('action', '/plone.org/login_form');
        }
    }
});

});
