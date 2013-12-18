#!/usr/bin/python

name = raw_input('Who are you?')
if name in ('Alice', 'Bob'):
    print 'Hello,', name+'!'
else:
    print "I don't know you."