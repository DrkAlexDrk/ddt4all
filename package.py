#!/usr/bin/python

import os, zipfile, glob

__author__ = "Cedric PAILLE"
__copyright__ = "Copyright 2016-2017"
__credits__ = []
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Cedric PAILLE"
__email__ = "cedricpaille@gmail.com"
__status__ = "Beta"


def zipdir(dirname):
    for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            if ".pyc" in filename:
                continue
            print "Adding source file %s" % filename
            zip.write(filename)

zip = zipfile.ZipFile("ddt4all_windows.zip", mode="w", compression=zipfile.ZIP_DEFLATED, allowZip64=True)
files = glob.glob("*.py")

for file in files:
    print "Adding source file %s" % file
    zip.write(file)

files = glob.glob("plugins/*.py")
for file in files:
    print "Adding plugin file %s" % file
    zip.write(file)

zip.write("ecu.zip")
zip.write("DDT4ALL.BAT")
zip.write("json/")
zip.write("logs/")

zipdir("./Python27")
zipdir("./importlib")
zipdir("./serial")
zipdir("./icons")
zipdir("./locale")
zipdir("./crcmod")

zip.close()
