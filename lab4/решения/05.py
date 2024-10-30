#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
print(zoo)

# 2
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# 3 
zoo.remove('elephant')
print(zoo)

# 4 
print("Lion v kletke № " + str(zoo.index('lion')+1))
print("Lark v kletke № " + str(zoo.index('lark')+1))