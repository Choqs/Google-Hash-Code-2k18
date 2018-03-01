#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:14:34 2018

@author: Vincoux & Sam
"""

from sys import argv

class Car:
    #x = 0
    #y = 0
    #travels = []
    #available_step = 0
    def __init__(self):
        self.x = 0
        self.y = 0
        self.travels = []
        self.available_step = 0
        
        
        
    @property
    def get_pos(self):
        return self.x, self.y
    def set_pos(self, x_, y_):
        self.x = x_
        self.y = y_
    def how_many_time(self, l):
        return distance(self.x, self.y, l[0], l[1]) + distance(l[0], l[1], l[2], l[3])
    def attribute(self, index, l, step):
        self.travels.append(index)
        self.available_step = step + self.how_many_time(l)


#----------------------------- PARSING -----------------------------
data = open(argv[1], 'r').read()
l = data.split('\n')
fl = l[0].split(' ')
row, col, nbv, nbr, bns, steps = [ int(x) for x in fl ]
matrix = []
for i in range(nbr):
    matrix.append([int(x) for x in l[i + 1].split(' ')])
    

#----------------------------- INIT --------------------------------

res = []
for i in range(nbv):
    res.append(Car())

#----------------------------- COMPUTE -----------------------------

def distance(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2))

def finish(travel_list):
    for travel in travel_list:
        if not travel:
            return False
    return True

step = 0
travel_list = [False] * len(matrix)
while (not finish(travel_list)):
    for j in range(len(matrix)):
        if travel_list[j]:
            continue
        if (finish(travel_list)):
            break
        mini = 1000000000
        mini_index = 0
        for i in range(len(res)):
            if (res[i].available_step <= step):
                if (res[i].how_many_time(matrix[j]) < mini):
                    mini = res[i].how_many_time(matrix[j])
                    mini_index = i
        if (mini != 1000000000):
            res[mini_index].attribute(j + 1, matrix[j], step)
            travel_list[j] = True
        step += 1



#----------------------------- OUTPUT ------------------------------

result = open(argv[1][:-3] + ".out", 'w')
r = ""
for i in range(nbv): 
    r += str(i + 1) + " "
    for j in range(len(res[i].travels)):
        r += str(res[i].travels[j]) + (" " if j < len(res[i].travels) - 1 else "")
    r += "\n"
result.write(r)
result.close()