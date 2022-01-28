#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()
import os
import json
import templates

print ('Content-Type: text/html')
print()
print(templates.login_page())

exit(0)