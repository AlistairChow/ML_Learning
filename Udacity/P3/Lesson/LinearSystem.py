#!/usr/bin/env python
# -*- coding:utf-8 -*-
from decimal import Decimal, getcontext
from copy import deepcopy

from Vector_ import Vector
from Hyperplane import Hyperplane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimention'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            # 验证线性方程的所有维度都相同
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def compute_solution(self):
        '''
        计算
        :return:
        '''
        try:
            return self.do_gaussian_elimination_and_parametrize_solution()

        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG:
                return str(e)
            else:
                raise e

    def do_gaussian_elimination_and_parametrize_solution(self):
        '''
        高斯消元法
        :return:
        '''
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()

        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()

        return Parametrization(basepoint, direction_vectors)

    def extract_direction_vectors_for_parametrization(self):
        '''
        提取参数化方向向量
        :return:
        '''
        num_variables = self.dimension
        #主变量
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        #自由变量
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)

        direction_vectors = []

        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector[free_var]
            direction_vectors.append(Vector(vector_coords))

        return direction_vectors

    def extract_basepoint_for_parametrization(self):
        '''
        提取基准点
        :return:
        '''
        num_variables = self.dimension
        pivot_indice = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coords = [0] * num_variables

        for i, p in enumerate(self.planes):
            pivot_var = pivot_indice[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var] = p.constant_term

        return Vector(basepoint_coords)

    def raise_exception_if_contradictory_equation(self):
        '''
        无解
        :return:
        '''
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector)

            except Exception as e:
                if str(e) == 'no nonzero elements found':

                    constant_term = p.constant_term
                    if constant_term != 0:
                        raise Exception(self.NO_SOLUTIONS_MSG)

                else:
                    raise e

    def raise_exception_if_too_few_pivots(self):
        '''
        无数解
        :return:
        '''
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        num_variables = self.dimension

        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)

    def compute_rref(self):
        '''
        线性方程组转换为最简形
        :return:
        '''
        tf = self.compute_triangular_form()

        num_equations = len(tf)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for i in range(num_equations)[::-1]:
            j = pivot_indices[i]
            if j < 0:
                continue
            tf.scale_row_to_make_coefficient_equal_one(i, j)
            tf.clear_coefficients_above(i, j)

        return tf

    def scale_row_to_make_coefficient_equal_one(self, row, col):
        '''
        将指定系数变换为1
        :param row:
        :param col:
        :return:
        '''
        n = self[row].normal_vector
        beta = Decimal('1') / n[col]
        self.multiply_coefficient_and_row(beta, row)

    def clear_coefficients_above(self, row, col):
        '''
        清除指定方程上方方程的指定系数
        :param row:
        :param col:
        :return:
        '''
        for k in range(row)[::-1]:
            n = self[k].normal_vector
            alpha = -(n[col])
            self.add_multiple_times_row_to_row(alpha, row, k)

    def compute_triangular_form(self):
        '''
        线性方程组三角变换
        :return:
        '''
        system = deepcopy(self)

        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = system[i].normal_vector[j]
                if c == 0:
                    swap_succeeded = system.swap_with_row_below_for_nonzero_cofficient_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue

                system.clear_coefficients_below(i, j)
                j += 1
                break

        return system

    def swap_with_row_below_for_nonzero_cofficient_if_able(self, row, col):
        '''
        当前线性方程与下面非0系数线性方程交换位置
        :param row: 当前线性方程位置
        :param col: 系数位置
        :return:
        '''
        num_equations = len(self)

        for k in range(row+1, num_equations):
            coefficient = self[k].normal_vector[col]
            if coefficient != 0:
                self.swap_rows(row, k)
                return True

        return False

    def clear_coefficients_below(self, row, col):
        '''
        清除指定方程下面方程的指定系数
        :param row:
        :param col:
        :return:
        '''
        num_equations = len(self)
        beta = self[row].normal_vector[col]

        for k in range(row+1, num_equations):
            n = self[k].normal_vector
            gamma = n[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, k)

    def swap_rows(self, row1, row2):
        '''
        交换线性方程位置
        :param row1:
        :param row2:
        :return:
        '''
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        '''
        线性方程等比扩大或缩小
        :param coefficient:
        :param row:
        :return:
        '''
        self.planes[row].normal_vector = self.planes[row].normal_vector.times_scale(coefficient)
        self.planes[row].constant_term *= coefficient
        self.planes[row].set_basepoint()

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        v = self.planes[row_to_add].normal_vector.times_scale(coefficient)
        self.planes[row_to_be_added_to].normal_vector = self.planes[row_to_be_added_to].normal_vector.plus(v)
        self.planes[row_to_be_added_to].constant_term += self.planes[row_to_add].constant_term * coefficient
        self.planes[row_to_be_added_to].set_basepoint()

    def indices_of_first_nonzero_terms_in_each_row(self):
        '''
        找出所有线性方程的第一个非0项索引
        :return:
        '''
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Hyperplane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def __len__(self):
        '''
        线性方程个数
        :return:
        '''
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = (
        'The basepoint and direction vectors should all live in same dimension')

    def __init__(self, basepoint, direction_vectors):
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.basepoint.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        num_decimal_places = 3

        output = ''
        for i in range(self.dimension):
            output += 'X_{} = '.format(i+1)
            if self.basepoint[i] < 0:
                output += '-'
            output += '{} '.format(
                abs(round(self.basepoint[i], num_decimal_places))
                if round(self.basepoint[i], num_decimal_places) != 0
                else '')

            for j, value in enumerate(self.direction_vectors):
                if value[i] == 0:
                    continue
                elif value[i] < 0:
                    output += '-'
                else:
                    output += '+'

                output += ' {}t_{}'.format(
                    round(abs(value[i]), num_decimal_places) if abs(value[i]) != 1 else '',
                    j+1)

            output += '\n'
        return output
