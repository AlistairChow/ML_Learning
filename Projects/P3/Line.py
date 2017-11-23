#!/usr/bin/env python
# -*- coding:utf-8 -*-
from decimal import Decimal, getcontext
from Vector_ import Vector

getcontext().prec = 30


class Line(object):
    '''
    直线操作类
    '''
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        '''
        直线初始化
        :param normal_vector: 法向量
        :param constant_term: 常量系数
        '''
        self.dimension = 2

        if not normal_vector:
            # 若法向量为空，则赋值法向量为原点
            all_zeros = [Decimal('0')]*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            # 若常数为空，则赋值常数为0
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def __eq__(self, ell):
        '''
        两线性方程是否为同一直线
        :param ell:
        :return:
        '''
        if self.normal_vector.is_zero():
            #如果法向量为0，那么每个变量系数为0
            #检测常量系数是否相等
            #常量系数相等则两条直线为同一直线
            #如果不同则不是同一直线
            if not ell.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - ell.constant_term
                return MyDecimal(diff).is_near_zero()
        elif ell.normal_vector.is_zero():
            return False

        if not self.is_parallel_to(ell):
            #不平行则不为同一直线
            return False

        #从两条直线上选取一个点，然后观察连接两个点的向量
        #如果该向量与第一条直线的法向量正交，那么两条直线是同一直线
        #否则两条直线不为同一直线
        x0 = self.basepoint
        y0 = ell.basepoint
        basepoint_difference = x0.minus(y0)

        n = self.normal_vector
        return basepoint_difference.is_orthogonal_to(n)

    def __str__(self):
        '''
        打印输出线性方程
        :return:
        '''
        num_decimal_places = 3
        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def is_parallel_to(self, ell):
        '''
        两线性方程是否平行
        通过检验法向量是否平行得出结论
        :param v:
        :return:
        '''
        return self.normal_vector.is_parallel_to(ell.normal_vector)

    def intersection_with(self, ell):
        '''
        计算交点
        :param ell:
        :return:
        '''
        try:
            A, B = self.normal_vector.coordinates
            C, D = ell.normal_vector.coordinates
            k1 = self.constant_term
            k2 = ell.constant_term

            x_numerator = D*k1 - B*k2
            y_numerator = -C*k1 + A*k2
            one_over_denom = Decimal('1')/(A*D - B*C)

            return Vector([x_numerator, y_numerator]).times_scale(one_over_denom)

        except ZeroDivisionError:
            if self == ell:
                return self
            else:
                return None

    def set_basepoint(self):
        '''
        设置基点
        :return:
        '''
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [Decimal('0')]*self.dimension

            # 初始化系数(coegficent)为法向量中第一个不为0的数
            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    @staticmethod
    def first_nonzero_index(iterable):
        '''
        遍历返回不为0的数索引
        :param iterable:
        :return:
        '''
        for k, item in enumerate(iterable):
            #if not MyDecimal(item).is_near_zero():
            if item != 0:
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
