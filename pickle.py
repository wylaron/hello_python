#!/usr/bin/python
# Filename: pickling.py

import cPickle as p
#import pickle as p

my_file = 'class.data'
# the name of the file where we will store the object

class MyClass(object):
    def hello(self):
        print 'Hello'

my_class = MyClass()
my_class.hello()
# Write to the file
f = file(my_file, 'w')
p.dump(my_class, f) # dump the object to a file
f.close()

del my_class # remove the shoplist

# Read back from the storage
f = file(my_file)
my_class = p.load(f)
my_class.hello()
print my_class