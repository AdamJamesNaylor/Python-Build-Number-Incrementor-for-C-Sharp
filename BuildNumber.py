import os
import sys

if len(sys.argv) < 2:
    print 'must specify a working directory'
    sys.exit()

wd = sys.argv[1]
print "Working directory: " + wd
path = wd + "\Properties\AssemblyInfo.cs"
tmpPath = path + ".tmp"
f = open(path, "r")
f2 = open(tmpPath, "w")
print "Successfully opened " + path + " for read."

line = f.readline()
    
while True:
    if (line.startswith("[assembly: AssemblyVersion")):
        version = line[line.rindex(".")+1:line.rindex("\"")]
        print "Current version: " + version
        version = int(version) + 1
        line = "[assembly: AssemblyVersion(\"1.0.0." + str(version) + "\")]\n"
    f2.write(line)
    line = f.readline()
    if line == "": break
print "New file with version " + str(version) + " created @ " + tmpPath + "."
f.close()
os.remove(path)
f2.close()
os.rename(tmpPath, path)
print "All done."
