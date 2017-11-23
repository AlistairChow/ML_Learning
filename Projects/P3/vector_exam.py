#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Vector_ import Vector


def print_title(title):
    print '-'*20
    print title
    print '-'*20


print_title(2.4)
v = Vector(['8.218', '-9.341'])
w = Vector(['-1.129', '2.111'])
print v.plus(w)

v = Vector(['7.119', '8.215'])
w = Vector(['-8.223', '0.878'])
print v.minus(w)

v = Vector(['1.671', '-1.012', '-0.318'])
print v.times_scale('7.41')

print_title(2.6)
v = Vector(['-0.221', '7.437'])
print v.magnitude()

v = Vector(['5.581', '-2.136'])
print v.normalized()

v = Vector(['8.813', '-1.331', '-6.247'])
print v.magnitude()

v = Vector(['1.996', '3.108', '-4.554'])
print v.normalized()

print_title(2.8)
v = Vector(['7.887', '4.138'])
w = Vector(['-8.802', '6.776'])
print v.dot(w)

v = Vector(['3.183', '-7.627'])
w = Vector(['-2.668', '5.319'])
print v.angle_with(w)

v = Vector(['-5.955', '-4.904', '-1.874'])
w = Vector(['-4.496', '-8.755', '7.103'])
print v.dot(w)

v = Vector(['7.35', '0.221', '5.188'])
w = Vector(['2.751', '8.259', '3.985'])
print v.angle_with(w, True)

print_title(2.10)
v = Vector(['-7.579', '-7.88'])
w = Vector(['22.737', '23.64'])
print v.is_parallel_to(w), v.is_orthogonal_to(w)

v = Vector(['-2.029', '9.97', '4.172'])
w = Vector(['-9.231', '-6.639', '-7.245'])
print v.is_parallel_to(w), v.is_orthogonal_to(w)

v = Vector(['-2.328', '-7.284', '-1.214'])
w = Vector(['-1.821', '1.072', '-2.94'])
print v.is_parallel_to(w), v.is_orthogonal_to(w)

v = Vector(['2.118', '4.827'])
w = Vector(['0', '0'])
print v.is_parallel_to(w), v.is_orthogonal_to(w)

print_title(2.12)
v = Vector(['3.039', '1.879'])
w = Vector(['0.825', '2.036'])
print v.component_parallel_to(w)

v = Vector(['-9.88', '-3.264', '-8.159'])
w = Vector(['-2.155', '-9.353', '-9.473'])
print v.component_orthogonal_to(w)

v = Vector(['3.009', '-6.172', '3.692', '-2.51'])
w = Vector(['6.404', '-9.144', '2.759', '8.718'])
print v.component_parallel_to(w)
print v.component_orthogonal_to(w)

print_title(2.14)
v = Vector(['8.462', '7.893', '-8.187'])
w = Vector(['6.984', '-5.975', '4.778'])
print v.cross(w)

v = Vector(['-8.987', '-9.838', '5.031'])
w = Vector(['-4.268', '-1.861', '-8.866'])
print v.area_of_parallelogram_with(w)

v = Vector(['1.5', '9.547', '3.691'])
w = Vector(['-6.007', '0.124', '5.772'])
print v.area_of_triangle_with(w)