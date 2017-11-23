#!/usr/bin/env python
# -*- coding:utf-8 -*-
from math import sqrt, acos, pi
from decimal import Decimal


class Vector(object):
    """
    向量操作类
    """
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two three dims'

    def __init__(self, coordinates):
        """
        向量初始化
        :param coordinates:向量坐标值
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, other):
        """
        向量加法
        :param other: 被加向量
        :return: 向量和
        """
        new_coordinates = [x+y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def minus(self, other):
        """
        向量减法
        :param other: 被减向量
        :return: 向量差
        """
        new_coordinates = [x-y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        """
        向量与标量乘积
        :param c: 标量
        :return: 乘积
        """
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        """
        计算向量大小
        :return: 向量大小
        """
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def normalized(self):
        """
        向量标准化,单位向量
        :return:标准化向量
        """
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, other):
        """
        向量点积
        :param other: 被点积向量
        :return: 点积结果
        """
        return sum([x*y for x, y in zip(self.coordinates, other.coordinates)])

    def angle_with(self, other, in_degrees=False):
        """
        向量夹角
        :param other: 被计算夹角向量
        :param in_degrees: True 为显示角度
        :return: 夹角结果
        """
        try:
            u1 = self.normalized()
            u2 = other.normalized()
            # 超出(-1,1)截断，防止acos异常
            cos_val = max(min(u1.dot(u2), 1.0), -1.0)
            angle_in_radians = acos(cos_val)

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

    def is_parallel_to(self, other, tolerance=1e-10):
        '''
        是否平行，零向量与所有向量平行，夹角为0或180°
        :param other:
        :return:
        '''
        return (self.is_zero() or
                other.is_zero() or
                self.angle_with(other) == tolerance or
                self.angle_with(other) == pi)

    def is_orthogonal_to(self, other, tolerance=1e-10):
        '''
        是否相交，点积为0
        :param other:
        :param tolerance: 公差
        :return:
        '''
        return abs(self.dot(other)) < tolerance

    def is_zero(self, tolerance=1e-10):
        '''
        是否为零向量，大小为0
        :param tolerance: 公差
        :return:
        '''
        return self.magnitude() < tolerance

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_orthogonal_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            else:
                raise e

    def area_of_triangle_with(self, other):
        return self.area_of_parallelogram_with(other) / Decimal('2.0')

    def area_of_parallelogram_with(self, other):
        cross_product = self.cross(other)
        return cross_product.magnitude()

    def cross(self, other):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = other.coordinates
            new_coordinates = [y_1*z_2 - y_2*z_1,
                               -(x_1*z_2 - x_2*z_1),
                               x_1*y_2 - x_2*y_1]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                other_embedded_in_R3 = Vector(other.coordinates + ('0',))
                return self_embedded_in_R3.cross(other_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                  msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates
