#! /usr/bin/env python
from __future__ import print_function
import sys
import commands
line = sys.stdin.read()
if "/*" and "*/" in line:
	line = line.replace('/*','')
	line = line.replace('*/','')
	msg = "Code block in selection uncommented"
else:
	line = "/*" + line
	line = line + "*/"
	msg = "Code block in selection commented"
sys.stdout.write(line)
exit(msg)

## Set gedit external tools params as below:
## "Save" ==> "Current Document"
## "Input" ==> "Current Selection"
## "Output" ==> "Replace Current Selection"
