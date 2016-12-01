#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

import test

from pymake2 import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(name='my_target')
def my_target1(conf):
    pass

@target(name='my_target')
def my_target2(conf):
    pass

#---------------------------------------
# SCRIPT
#---------------------------------------

test.should_fail()

pymake2({}, [])

test.success()
