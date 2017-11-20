#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Vector

a = Vector.Vector((1, 2))
print Vector.Vector.plus(a, a)
print Vector.Vector.minus(a, a)
print Vector.Vector.times_scalar(a, 3)
print a.magnitude()
print a.normalized()