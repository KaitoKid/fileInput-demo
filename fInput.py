import sys
import fileinput

# open up the file you want to change
f = fileinput.input(files=(sys.argv[-1]), inplace=False)

# create the file you want to write to with the fixed version
output = open('fixed_' + sys.argv[-1], 'w+')

# for each line you read, do something and write to the new file
for line in f:
    newline = line.replace('walk', 'GUCCIGANG')
    output.write(newline)

# close the streams or it breaks on python2
f.close()
output.close()