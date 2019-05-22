import matplotlib.pyplot as plt
import numpy as np
import math
import os
import sys

print("Grafis Runtun Descret")
# returns 10 evenly spaced samples from 0.1 to 2*PI
# x = np.linspace(0.1, 2 * np.pi, 10)
n = 0, 1, 2
x = 15, 3, 99
# NO 1
#       -> Tabular-> x(n) = { 15,3,99 }
#       -> Fungsi x(n) = { x|0 < x < 99 , x bil.bulat }
#       -> grafis ->
# markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
markerline, stemlines, baseline = plt.stem(n, x, '-.')
# setting property of baseline with color red and linewidth 2
plt.setp(baseline, color='r', linewidth=2)
plt.title('grafis x(n) = { 15, 3, 99, 0, 1, 2 }')
plt.grid(True)
plt.ylabel('x(n)')
plt.xlabel('n = [0:2]')
# plt.yscale('linear')
plt.show()


def grafis(n, x):

    # markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
    markerline, stemlines, baseline = plt.stem(n, x, '-.')
    # setting property of baseline with color red and linewidth 2
    plt.setp(baseline, color='r', linewidth=2)
    plt.title('grafis x(n) = { 15, 3, 99, 0, 1, 2 }')
    plt.grid(True)
    plt.ylabel('x(n)')
    plt.xlabel('n = [0:2]')
    # plt.yscale('linear')
    plt.show()


print("Masukan Nilai x : ")
x = [int(i) for i in input().split()]

print("Masukan Nilai n : ")
n = [int(i) for i in input().split()]

grafis(n, x)
