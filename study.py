#!/usr/bin/env python3
# -*-coding:utf-8-*-

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x*self.x

obj = MyObject()

print(hasattr(obj,'x'))

print(hasattr(obj,'y'))

setattr(obj,'y',19)

print(hasattr(obj,'y'))

getattr(obj,'z',404)

print(hasattr(obj,'power'))

fn = getattr(obj,'power')

print(fn())
