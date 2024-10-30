#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1
pi = 3.1415926
r = 42
S = pi * r ** 2
print('s = ', S)

# 2 
point_1 = (23, 34)
point_0 = (0, 0)
# формула (x – x0)^2 + (y – y0)^2 = r^2
# x0 = 0; y0 = 0 => x^2 + y^2 = r^2 (r = 42)
rastoyanie = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(rastoyanie <= S)

# 3
point_2 = (30, 30)
point_0 = (0, 0)
rastoyanie2 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(rastoyanie2 <= S)