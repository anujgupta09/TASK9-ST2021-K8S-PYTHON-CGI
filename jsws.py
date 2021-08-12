#! /usr/bin/python3
import cgi

print("content-type: text/html")
print()

import subprocess

f = cgi.FieldStorage()
cmd_recieved = f.getvalue("cmd")


op=subprocess.getoutput("sudo " + cmd_recieved)

print(op)
