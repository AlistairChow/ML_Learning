#!/usr/bin/env python
# -*- coding:utf-8 -*-
from decimal import Decimal
from math import acos, pi


class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two three dims'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            self.prev = -1
            self.curr = -1

        except ValueError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        '''
        向量加法
        :param v:
        :return:
        '''
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        '''
        向量减法
        :param v:
        :return:
        '''
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scale(self, c):
        '''
        向量与标量乘积
        :param
        :return:
        '''
        new_coordinates = [x*Decimal(c) for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        '''
        向量的模
        :return:
        '''
        return sum([x**2 for x in self.coordinates]).sqrt()

    def normalized(self):
        '''
        单位向量
        :return:
        '''
        return self.times_scale(Decimal('1') / self.magnitude())

    def dot(self, v):
        '''
        点积
        :param v:
        :return:
        '''
        return sum(x*y for x, y in zip(self.coordinates, v.coordinates))

    def angle_with(self, v, in_degrees=False):
        '''
        向量夹角
        :param v:
        :param in_degrees: True 转换为度数
        :return:
        '''
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            cos_value = u1.dot(u2)
            angle_in_radians = acos(cos_value)

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def is_parallel_to(self, v):
        '''
        向量是否平行
        鉴定方式为：是否为零向量（零向量与所有向量平行），两个向量之间的夹角为0（相向），两个向量之间夹角为180（相反）
        :param v:
        :return:
        '''
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)

    def is_orthogonal_to(self, v):
        '''
        向量是否相交
        :param v:
        :return:
        '''
        return self.dot(v) == 0

    def is_zero(self):
        '''
        是否为零向量
        :return:
        '''
        return self.magnitude() == 0

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        '''
        求到basis的投影
        :param basis:
        :return:
        '''
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scale(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        '''
        与V所构成的三角形面积
        :param v:
        :return:
        '''
        return self.area_of_parallelogram_with(v)/Decimal('2')

    def area_of_parallelogram_with(self, v):
        '''
        与v所构成的平行四边形面积
        :param v:
        :return:
        '''
        cross_product = self.cross(v)
        return cross_product.magnitude()

    def cross(self, v):
        '''
        叉乘
        :param v:
        :return:
        '''
        try:
            x1, x2, x3 = self.coordinates
            y1, y2, y3 = v.coordinates

            return Vector([x2*y3 - x3*y2,
                           x3*y1 - x1*y3,
                           x1*y2 - x2*y1])

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                other_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(other_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                  msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __iter__(self):
        self.curr = -1
        return self

    def next(self):
        self.prev = self.curr
        self.curr += 1
        if self.curr >= self.dimension:
            raise StopIteration
        return self.coordinates[self.curr]

    def __getitem__(self, item):
        if item >= self.dimension:
            raise IndexError
        return self.coordinates[item]

