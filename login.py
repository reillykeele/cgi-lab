#!/usr/bin/env python3
import cgi
import cgitb
from re import template
cgitb.enable()

import templates
import secret
import os
from http.cookies import SimpleCookie


form = cgi.FieldStorage()
username = form.getfirst('username')
password = form.getfirst('password')

form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_user = None
cookie_pass = None
if cookie.get("username"): 
    cookie_user = cookie.get("username").value
if cookie.get("password"): 
    cookie_user = cookie.get("password").value

cookie_ok = cookie_user = secret.username and cookie_pass == secret.password

if cookie_ok:
    username = cookie_user
    password = cookie_pass

print ('Content-Type: text/html')
if form_ok:
    print(f'Set-Cookie: username={username}')    
    print(f'Set-Cookie: password={password}')    
print()


if not username and not password:
    print(templates.login_page())
elif username == secret.username and password == secret.password:
    print(templates.secret_page(username, password))
else:
    print(templates.after_login_incorrect())

exit(0)