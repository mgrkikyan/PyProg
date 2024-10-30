#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = dict()

m = sites['Moscow']
l = sites['London']
p = sites['Paris']

Moscow_London = ((m[0] - l[0]) ** 2 + (m[1] - l[1]) ** 2) ** 0.5
Moscow_Paris = ((m[0] - p[0]) ** 2 + (m[1] - p[1]) ** 2) ** 0.5
London_Moscow = ((l[0] - m[0]) ** 2 + (l[1] - m[1]) ** 2) ** 0.5
London_Paris = ((l[0] - p[0]) ** 2 + (l[1] - p[1]) ** 2) ** 0.5
Paris_Moscow = ((p[0] - m[0]) ** 2 + (p[1] - m[1]) ** 2) ** 0.5
Paris_London = ((p[0] - l[0]) ** 2 + (p[1] - l[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = Moscow_London
distances['Moscow']['Paris'] = Moscow_Paris

distances['London'] = {}
distances['London']['Moscow'] = London_Moscow
distances['London']['Paris'] = London_Paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = Paris_Moscow
distances['Paris']['London'] = Paris_London

result = {'Moscow-London': distances['Moscow']['London'], 'London-Paris': distances['London']['Paris'], 'Paris-Moscow': distances['Paris']['Moscow']}

print(result)
