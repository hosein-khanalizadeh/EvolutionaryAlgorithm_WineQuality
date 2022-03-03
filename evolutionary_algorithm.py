#!/usr/bin/python
'''Created by hosein-khanalizadeh'''

import random
# import csv
import matplotlib.pyplot as plt


min = 0
max = 1

def first_generation():
    for i in range(1000):
        aj = []
        for j in range(11):
            r = random.uniform(min,max)
            aj.append(r)
        ai.append(aj)
    return ai

def compute_y0(a,x):
    y0 = 0
    for l in range(len(a)):
        y0 += float(a[l])*float(x[l])
    return y0

def error(y,y0):
    er = (float(y)-y0)**2
    return er

def compute_fitness(ai):
    global data
    sum_fit = 0
    for k in range(len(data)):
        xi = data[k]
        y0 = compute_y0(ai,xi)
        er = error(data[k][11],y0)
        sum_fit += er
    fitness = sum_fit/100
    return fitness

def select_chromeosome(fit_list):
    sum = 0
    count = 0.0
    bi = []
    for n in fit_list:
        bi_obj = 1 / float(n)
        bi.append(bi_obj)
        sum += bi_obj
    r = random.uniform(0,sum)
    for n in range(len(bi)):
        if r <= float(bi[n])+count:
            return n
        count += bi[n]

def crossover(first,second):
    global cross
    nerkh = 1
    r = random.randint(0, len(first))
    first[r:] = second[r:]
    second[r:] = first[r:]
    cross = first[:r]+second[r:]
    mut = mutation(nerkh)
    if mut == True:
        r = random.randint(0,len(cross)-1)
        ran = random.uniform(min,max)
        cross[r] = ran
    return cross

def mutation(nerkh):
    r = random.randint(0,100)
    if nerkh <= r:
        is_mutation = True
    else:
        is_mutation = False
    return is_mutation


ai = list()
y0 = 0
sum_fit = 0
cross = list()
all_fit_list = list()

data = list()
f = open('data.txt', 'r+')
file = f.read().splitlines()
for m in range(len(file)):
    data.append(file[m].split(';'))

# data = list()
# file = open('test_label.csv' , 'r')
# test_label_reader = csv.reader(file)
# for row in test_label_reader:
#     for i in row:
#         data.append(float(i))
# file.close()

fg = first_generation()
for q in range(10):
    fit_list = []
    cr = []
    for o in range(len(fg)):
        fit_list.append(compute_fitness(fg[o]))
    plt.plot(fit_list)
    plt.title('fitness diagram')
    plt.ylabel('fitness')
    plt.show()
    all_fit_list.append(fit_list)
    for p in range(1000):
        f1 = select_chromeosome(fit_list)
        f2 = select_chromeosome(fit_list)
        cr.append(crossover(fg[f1],fg[f2]))
    fg = cr

plt.hist(all_fit_list[0], color='blue', edgecolor='red', bins=25)
plt.show()
plt.hist(all_fit_list[-1], color='blue', edgecolor='red', bins=25)
plt.show()
fit_list.sort()
print(fit_list[0])
