#!/usr/bin/python
import sys

# plugin by Roland Kainbacher
# rka@beautyparlour.at


text= sys.stdin.read()
output = '\n/* !$$IP$$ */\n/* ---------------------------------------------------------------------- */\n\n'



def lineparse(line1, finder, output):

    linerest = ''

    if finder == 'id':
        
        linepart = line1.find( finder + '="')
        line1 = line1[linepart+4:]
        linepart = line1.find('"')
        linerest = line1[linepart:]
        lineparam = line1[:linepart]
        output =  output + '#' + lineparam + ' {\n}\n\n'
    
    
    else:
        linepart = line1.find( finder + '="')
        line1 = line1[linepart+7:]
        linepart = line1.find('"')
        linerest = line1[linepart:]
        lineparam = line1[:linepart]
        output =  output + '.' + lineparam + ' {\n}\n\n'


    listoutput = [output, linerest]
    return listoutput




for line in text.splitlines():
    
    line1 = line
    
    if line1.find('id="') != -1:
        finder = 'id'
        parsefunc = lineparse(line1, finder, output)
        output = parsefunc[0]

        if parsefunc[1].find( finder + '="') != -1:
            parsefuncrepeat = lineparse(parsefunc[1], finder, output)
            output = parsefuncrepeat[0]



    if line.find('class="') != -1:
        finder = 'class'
        parsefunc = lineparse(line1, finder, output)
        output = parsefunc[0]

        if parsefunc[1].find( finder + '="') != -1:
            parsefuncrepeat = lineparse(parsefunc[1], finder, output)
            output = parsefuncrepeat[0]



sys.stdout.write(output)




