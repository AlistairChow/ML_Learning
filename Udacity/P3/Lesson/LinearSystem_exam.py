#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Vector_ import Vector
from Plane import Plane
from LinearSystem import LinearSystem
from decimal import Decimal
from Hyperplane import Hyperplane

p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

s = LinearSystem([p0, p1, p2, p3])

print s.indices_of_first_nonzero_terms_in_each_row()
print '{},{},{},{}'.format(s[0], s[1], s[2], s[3])
print len(s)
print s

s.swap_rows(0, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 1 failed'

s.swap_rows(3, 1)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print 'test case 2 failed'

s.swap_rows(3, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 3 failed'

s.multiply_coefficient_and_row(1, 0)
if not(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 4 failed'

s.multiply_coefficient_and_row(-1, 2)
if not (s[0] == p1 and
        s[1] == p0 and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print 'test case 5 failed'

s.multiply_coefficient_and_row(10, 1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print 'test case 6 failed'

s.add_multiple_times_row_to_row(0, 0, 1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print 'test case 7 failed'


s.add_multiple_times_row_to_row(1, 0, 1)
if not (s[0] == p1 and
        s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print 'test case 8 failed'

s.add_multiple_times_row_to_row(-1, 1, 0)
if not (s[0] == Plane(normal_vector=Vector(['-10', '-10', '-10']), constant_term='-10') and
        s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
        s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
        s[3] == p3):
    print 'test case 9 failed'

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2):
    print 'test case 1 failed'

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == Plane(constant_term='1')):
    print 'test case 2 failed'

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
s = LinearSystem([p1, p2, p3, p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(normal_vector=Vector(['0', '0', '-2']), constant_term='2') and
        t[3] == Plane()):
    print 'test case 3 failed'

p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
s = LinearSystem([p1, p2, p3])
t = s.compute_triangular_form()
if not (t[0] == Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2') and
        t[1] == Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1') and
        t[2] == Plane(normal_vector=Vector(['0', '0', '-9']), constant_term='-2')):
    print 'test case 4 failed'

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']), constant_term='-1') and
        r[1] == p2):
    print 'test case 1 failed'

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == p1 and
        r[1] == Plane(constant_term='1')):
    print 'test case 2 failed'

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
s = LinearSystem([p1, p2, p3, p4])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']), constant_term='0') and
        r[1] == p2 and
        r[2] == Plane(normal_vector=Vector(['0', '0', '-2']), constant_term='2') and
        r[3] == Plane()):
    print 'test case 3 failed'

p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
s = LinearSystem([p1, p2, p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']), constant_term=Decimal('23')/Decimal('9')) and
        r[1] == Plane(normal_vector=Vector(['0', '1', '0']), constant_term=Decimal('7')/Decimal('9')) and
        r[2] == Plane(normal_vector=Vector(['0', '0', '1']), constant_term=Decimal('2')/Decimal('9'))):
    print 'test case 4 failed'

p1 = Plane(normal_vector=Vector(['5.862', '1.178', '-10.336']), constant_term='-8.15')
p2 = Plane(normal_vector=Vector(['-2.931', '-0.589', '5.183']), constant_term='-4.075')
s = LinearSystem([p1, p2])
print s.compute_solution()

p1 = Plane(normal_vector=Vector(['8.631', '5.112', '-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=Vector(['4.315', '11.132', '-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=Vector(['-2.158', '3.01', '-1.727']), constant_term='-0.831')
s = LinearSystem([p1, p2, p3])
print s.compute_solution()

p1 = Plane(normal_vector=Vector(['5.262', '2.739', '-9.878']), constant_term='-3.441')
p2 = Plane(normal_vector=Vector(['5.111', '6.358', '7.638']), constant_term='-2.152')
p3 = Plane(normal_vector=Vector(['2.016', '-9.924', '-1.367']), constant_term='-9.278')
p4 = Plane(normal_vector=Vector(['2.167', '-13.543', '-18.883']), constant_term='-10.567')
s = LinearSystem([p1, p2, p3, p4])
print s.compute_solution()

p1 = Plane(normal_vector=Vector(['0.786', '0.786', '0.588']), constant_term='-0.714')
p2 = Plane(normal_vector=Vector(['-0.131', '-0.131', '0.244']), constant_term='0.319')
s = LinearSystem([p1, p2])
print 'System 1 solution:\n{}'.format(s.compute_solution())

p1 = Plane(normal_vector=Vector(['8.631', '5.112', '-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=Vector(['4.315', '11.132', '-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=Vector(['-2.158', '3.01', '-1.727']), constant_term='-0.831')
s = LinearSystem([p1, p2, p3])
print 'System 2 solution:\n{}'.format(s.compute_solution())

p1 = Plane(normal_vector=Vector(['0.935', '1.76', '-9.365']), constant_term='-9.955')
p2 = Plane(normal_vector=Vector(['0.187', '0.352', '-1.873']), constant_term='-1.991')
p3 = Plane(normal_vector=Vector(['0.374', '0.704', '-3.746']), constant_term='-3.982')
p4 = Plane(normal_vector=Vector(['-0.561', '-1.056', '5.619']), constant_term='5.973')
s = LinearSystem([p1, p2, p3, p4])
print 'System 3 solution:\n{}'.format(s.compute_solution())

p1 = Hyperplane(normal_vector=Vector(['0.786', '0.786']), constant_term='-0.714')
p2 = Hyperplane(normal_vector=Vector(['-0.131', '-0.131']), constant_term='0.319')
s = LinearSystem([p1, p2])
print 'System 1 solution:\n{}'.format(s.compute_solution())

p1 = Hyperplane(normal_vector=Vector(['2.102', '7.489', '-0.786']), constant_term='-0.714')
p2 = Hyperplane(normal_vector=Vector(['-1.131', '-8.318', '1.209']), constant_term='0.319')
p3 = Hyperplane(normal_vector=Vector(['9.015', '-5.873', '1.105']), constant_term='0.319')
s = LinearSystem([p1, p2, p3])
print 'System 2 solution:\n{}'.format(s.compute_solution())

p1 = Hyperplane(normal_vector=Vector(['0.786', '0.786', '8.123', '1.111', '-8.363']), constant_term='-0.714')
p2 = Hyperplane(normal_vector=Vector(['-0.131', '0.131', '7.05', '-2.813', '1.19']), constant_term='0.319')
p3 = Hyperplane(normal_vector=Vector(['9.015', '-5.873', '-1.105', '2.013', '-2.802']), constant_term='0.319')
s = LinearSystem([p1, p2, p3])
print 'System 2 solution:\n{}'.format(s.compute_solution())