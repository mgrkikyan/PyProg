#!/usr/bin/env python3
# -*- coding: utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

# 1 
print(garden_set)
print(meadow_set)

# 2 
print(garden_set & meadow_set)

# 3
print(garden_set - meadow_set)

# 4
print(meadow_set - garden_set)