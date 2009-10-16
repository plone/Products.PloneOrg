print '<script type="text/javascript">'
quoted = "<', '".join(data.replace(r"'", r"\'").split('<'))
lines = quoted.split('\n')
print "    document.write('%s');" % "', '".join(lines)
print "</script>"
return printed
