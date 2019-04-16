#!/bin/python

import sys

ntrips,capacity,nboat = raw_input().strip().split(' ')
ntrips,capacity,nboat = [int(ntrips),int(capacity),int(nboat)]
p = map(int, raw_input().strip().split(' '))
print ntrips,capacity,nboat
print p