#!/usr/bin/python
import sys

# plugin by Roland Kainbacher
# rka@beautyparlour.at


text= sys.stdin.read()
output = ''


for line in text.splitlines():

    linePos = line.find(':')
    if linePos > 1:

        #space befor : 
        if line[linePos] != ' ':
            line = line[:linePos] + ' ' + line[linePos:]
        else:
            line = line

        #space after :
        linePosAfter = linePos + 2

        if line[linePosAfter] != ' ':
            line = line[:linePosAfter] + ' ' + line[linePosAfter:]
        else:
            line = line


        #positioner
        steper = 20 - linePos
        for i in range(steper):
            output = output + ' '
        output = output + line + '\n'
    else:
        output = output + line + '\n'


sys.stdout.write(output)