#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''

'''
__author__ = "Yogi Arif Widodo (point_bug)"
__copyright__ = "Copyright 2019, Bugs_Bunny Team | Dsp Tools"
__version__ = "0.1"
__email__ = "yogirenbox33@gmail.com"
__status__ = "Development"
__codename__ = 'python-matlab-data-signal'
__source__ = "https://github.com/yogithesymbian/python-matlab-data-signal"
__info__ = "URL scodeid"

# math lib
import matplotlib.pyplot as plt
import numpy as np
import math
# end of math lib
import os
import sys
# colorstyle with figlet
from color import ColorPrint as pyogclr
from lib.colors import colors as c
from pyfiglet import figlet_format
import string


def hr_yogi():
    pyogclr.print_info(figlet_format('____________'))


def banner():
    hr_yogi()
    print(
        '. DEFAULT VALUE X = ', x, ' AND N = ', n)
    pyogclr.print_info('.  YOU CAN CUSTOMIZE with [*] CHOOSE : dspolnes')
    hr_yogi()
    pyogclr.print_warn(
        'Birt Of Date : 15 march 1999 \t x = { 15 03 99 } \t n = { 0 1 2 }')
    pyogclr.print_info(figlet_format('        DSP-Mr-Day     '))
    pyogclr.print_warn(
        'NAME: Yogi Arif Widodo \t\t NIM: 17 615 006 \t CLASS: TI(4A)')
    hr_yogi()
    pyogclr.print_fail('.\n. \t\t\t\t MENU PROGRAM')
    pyogclr.print_warn('.\t\t\t_________________________________')
    pyogclr.print_pass('. \tx(n) dalam runtun diskret dalam bentuk notasi')
    pyogclr.print_fail('. \t\t\t 1. Bentuk Tabular Form')
    pyogclr.print_fail('. \t\t\t 2. fungsi x(n)')
    pyogclr.print_fail('. \t\t\t 3. Grafis')
    pyogclr.print_fail('. \t\t\t 4. Persamaan Beda\n')
    pyogclr.print_pass('.\n. \tBagaimana bentuk X(n) Baru Jika')
    pyogclr.print_fail('. \t\t\t 5. -x(n-3)')
    pyogclr.print_fail('. \t\t\t 6. -3x(n)')
    pyogclr.print_fail('. \t\t\t 7.  x(n)-X(n-3)\n')
    pyogclr.print_pass('. \tCarilah x(n)')
    pyogclr.print_fail('. \t\t\t 8. Transformasi Fourier ')
    pyogclr.print_fail('. \t\t\t 8. Transformasi Z ')
    pyogclr.print_fail('. \t\t\t N. Exit')

    # choose = pyogclr.print_warn('. \t\t\t [*].Choose : ',)
    # inputString = input()

    ioMenu = input('.\n. \t\t\t [*].Choose : ')
    if ioMenu == 'dspolnes':
        ioGrafis()
    elif ioMenu == '3':
        yoGrafis()
    else:
        pyogclr.print_bold('asdasdasd')


def start():
    banner()


def grafis(n, x):
    # markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
    markerline, stemlines, baseline = plt.stem(n, x, '-.')
    # setting property of baseline with color red and linewidth 2
    plt.setp(baseline, color='r', linewidth=2)
    xn = 'grafis x(n) = { '
    xn1 = x + n
    xn2 = ' }'
    xnh = xn, xn1, xn2

    plt.title(xnh)
    plt.grid(True)
    plt.ylabel('x(n)')
    plt.xlabel('n = [0:2]')
    # plt.yscale('linear')
    plt.show()


# default
x = 15, 3, 99
n = 0, 1, 2


def yoGrafis():
    pyogclr.print_pass('opening figure . . .')

    grafis(n, x)


def ioGrafis():
    print("Masukan Nilai x : ")

    # x = [int(i) for i in input().split()]
    x = list(map(int, input().split()))

    print("Masukan Nilai n : "),
    n = [int(i) for i in input().split()]

    hr_yogi()

    pyogclr.print_bold('output will execute')
    print('\t\tnilai x = ', x)
    print('\t\tNilai n = ', n)


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print("\n[!] By ...:")
        sys.exit(0)
