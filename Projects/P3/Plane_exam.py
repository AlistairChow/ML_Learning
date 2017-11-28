#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Plane import Plane
from Vector_ import Vector

p1 = Plane(normal_vector=Vector(['-0.412', '3.806', '0.728']), constant_term='-3.46')
p2 = Plane(normal_vector=Vector(['1.03', '-9.515', '-1.82']), constant_term='8.65')
print p1.is_parallel_to(p2)
print p1 == p2

p1 = Plane(normal_vector=Vector(['2.611', '5.528', '0.283']), constant_term='4.6')
p2 = Plane(normal_vector=Vector(['7.715', '8.306', '5.432']), constant_term='3.76')
print p1.is_parallel_to(p2)
print p1 == p2

p1 = Plane(normal_vector=Vector(['-7.926', '8.625', '-7.212']), constant_term='-7.952')
p2 = Plane(normal_vector=Vector(['-2.642', '2.875', '-2.404']), constant_term='-2.443')
print p1.is_parallel_to(p2)
print p1 == p2

