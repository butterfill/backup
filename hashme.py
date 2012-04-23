#! /usr/bin/python

import os
import hashlib
import base64
import getpass

pw1 = getpass.getpass('pw:')
domain1 = raw_input('domain:')
pw2 = getpass.getpass('pw:')
domain2 = raw_input('domain:')
if pw1 != pw2 or domain1 != domain2:
  exit("mismatch")

m = hashlib.sha512()
m.update(pw1)
m.update(domain1)
res = base64.b64encode(m.hexdigest())[5:5+16]
os.system("echo %s | tr -d '\n'  | pbcopy" % res)
exit(res)
