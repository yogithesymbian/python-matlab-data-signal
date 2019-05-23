#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Symbol sinyal diskrit sampling ke n adalah:
Input = x(n)
Proses = x(n)
Output = x(n)

Untuk:
x[0], nilai 0 dalam kurung siku menyatakan sample ke-0,
x[1], nilai 1 dalam kurung siku menyatakan sample ke-1.

x[n-1] menyatakan sinyal sampel ke n digeser ke kanan sejauh 1
sampel, dan x[n-2] menyatakan sinyal sampel ke n digeser ke
kanan sejauh 2 sampel.

x[n+1] menyatakan sinyal diskrit digeser ke kiri sejauh 1, x[n+2]
menyatakan sinyal diskrit digeser ke kiri sejauh 2 sample.
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
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy.fftpack  # for fourier lib
import math
# end of math lib
import os
import sys
# colorstyle with figlet
from color import ColorPrint as pyogclr
from lib.colors import colors as c
from pyfiglet import figlet_format
import string

# default
x = 1, 5, 0, 3, 9, 9
n = 0, 1, 2, 3, 4, 5


def hr_yogi():
    pyogclr.print_info(figlet_format('____________'))


def banner():
    hr_yogi()
    pyogclr.print_fail('. THIS PROGRAM HAS DEFAULT VALUE')
    pyogclr.print_info('.  YOU CAN CUSTOMIZE with [*] CHOOSE : dspolnes')
    hr_yogi()
    pyogclr.print_warn(
        'Birt Of Date : 15 march 1999 \t x = { 1 5 0 3 9 9 } \t n = { 0 1 2 3 4 5}')
    pyogclr.print_info(figlet_format('        DSP-Mr-Day     '))
    pyogclr.print_warn(
        'NAME: Yogi Arif Widodo \t\t NIM: 17 615 006 \t CLASS: TI(4A)')
    hr_yogi()


def bannerProgram():
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
    pyogclr.print_fail('. \t\t\t 7.  x(n)-x(n-3)\n')
    pyogclr.print_pass('. \tCarilah x(n)')
    pyogclr.print_fail('. \t\t\t 8. Transformasi Fourier ')
    pyogclr.print_fail('. \t\t\t 9. Transformasi Z ')
    pyogclr.print_fail('. \t\t\t N. Exit')

    # choose = pyogclr.print_warn('. \t\t\t [*].Choose : ',)
    # inputString = input()

    ioMenu = input('.\n. \t\t\t [*].Choose : ')
    '''
        Action Menu Program
    '''
    if ioMenu == 'dspolnes':
        ioGrafis()
    elif ioMenu == '1':
        # clearscreen
        yogiClear()
        # banner
        banner()
        # function
        tabularForm()
    elif ioMenu == '2':
        yogiClear()
        banner()
        bentukFxn()
    elif ioMenu == '3':
        yogiClear()
        banner()
        yoGrafis()
    elif ioMenu == '4':
        yogiClear()
        banner()
        differentialEquation()
    elif ioMenu == '5':
        yogiClear()
        banner()
        nomorLima()
    elif ioMenu == '6':
        yogiClear()
        banner()
        nomorEnam()
    elif ioMenu == '7':
        yogiClear()
        banner()
        nomorTujuh()
    elif ioMenu == '8':
        yogiClear()
        banner()
        yoFourier()
        # y/n [against|exit]
        yogiAsk()
    elif ioMenu == '9':
        yogiClear()
        banner()
        yoTransz()
        yogiAsk()
    else:
        pyogclr.print_bold('still development choose other menu')


# begining start program
def start():
    banner()  # banner copyright by yogithesymbian
    bannerProgram()  # menu program dsp


def yogiClear():
    os.system('cls')
    os.system('clear')


def nomorLima():
    pyogclr.print_pass('            THIS A BENTUK -x(n-3) :')
    print('From : x = ', x)
    print('       n = ', n)
    pyogclr.print_pass('opening figure . . .')
    x1 = -x[0]
    x2 = -x[1]
    x3 = -x[2]
    x4 = -x[3]
    x5 = -x[4]
    x6 = -x[5]
    xberubah = x1, x2, x3, x4, x5, x6
    n1 = n[0] - 3
    n2 = n[1] - 3
    n3 = n[2] - 3
    n4 = n[3] - 3
    n5 = n[4] - 3
    n6 = n[5] - 3
    nberubah = n1, n2, n3, n4, n5, n6
    # xberubah = -x
    # nberubah = n - 3
    grafis(nberubah, xberubah)


def nomorEnam():
    pyogclr.print_pass('            THIS A BENTUK -3x(n) :')
    print('From : x = ', x)
    print('       n = ', n)
    pyogclr.print_pass('opening figure . . .')
    minusnya = -3
    x1 = minusnya * x[0]
    x2 = minusnya * x[1]
    x3 = minusnya * x[2]
    x4 = minusnya * x[3]
    x5 = minusnya * x[4]
    x6 = minusnya * x[5]
    xberubah = x1, x2, x3, x4, x5, x6
    # xberubah = -x
    # nberubah = n - 3
    grafis(n, xberubah)


def nomorTujuh():
    pyogclr.print_pass('            THIS A BENTUK x(n)-x(n-3) :')
    print('From : x = ', x)
    print('       n = ', n)
    pyogclr.print_pass('opening figure . . .')
    x1 = x[0] - x[0]
    x2 = x[1] - x[1]
    x3 = x[2] - x[2]
    x4 = x[3] - x[3]
    x5 = x[4] - x[4]
    x6 = x[5] - x[5]
    xberubah = x1, x2, x3, x4, x5, x6
    n1 = n[0] - (n[0]-3)
    n2 = n[1] - (n[1]-3)
    n3 = n[2] - (n[2]-3)
    n4 = n[3] - (n[3]-3)
    n5 = n[4] - (n[4]-3)
    n6 = n[5] - (n[5]-3)
    nberubah = n1, n2, n3, n4, n5, n6
    # xberubah = -x
    # nberubah = n - 3
    grafis(nberubah, xberubah)


# function that returns dy/dt
def model(y, t):
    k = 0.3
    dydt = -k * y
    return dydt


def differentialEquation():
    print('\n ')
    print('model: Function name that returns derivative values at requested y and t values as dydt=model(y, t)')
    print('y0: Initial conditions of the differential states')
    print('t: Time points at which the solution should be reported. Additional internal points are often calculated to maintain accuracy of the solution but are not reported.')
    pyogclr.print_pass('opening figure . . .')
    print('From : x = ', x)
    print('       n = ', n)
    # initial condition
    # for x(n) = { 1 5 0 3 9 9}
    y0 = x

    # time points
    # arr[0:5]
    t = np.linspace(n[0], n[5])

    # solve ODE
    y = odeint(model, y0, t)

    # plot results
    plt.plot(t, y)

    plt.title('Differential Equation')
    plt.grid(True)
    plt.ylabel('y(t)')
    plt.xlabel('time')

    plt.show()
    yogiAsk()


def bentukFxn():
    print('\n\n')
    pyogclr.print_pass('            THIS A BENTUK FUNGSI x(n) :')
    print('\n\t\t\t x(n) = { n | ', n[0],
          ' <= n <= ', n[5], ', n bil. ganjil }')
    yogiAsk()


def tabularForm():
    print('\n\n')
    pyogclr.print_pass('            THIS A TABULAR FORM :')
    print('\t\t WHERE ')
    print('\t\t\t x(n) = { d d m m y y }')
    print('\t\t\t x(n) = {', x[0], x[1], x[2], x[3], x[4], x[5], '}')
    yogiAsk()


def grafis(n, x):
    # markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')
    markerline, stemlines, baseline = plt.stem(n, x, '-.')
    # setting property of baseline with color red and linewidth 2
    plt.setp(baseline, color='r', linewidth=2)

    xn = 'grafis x(n) = { '
    xn1 = x
    xn2 = ' }'
    xnh = xn, xn1, xn2

    nilFrom = n[0]
    nilEnd = n[5]
    label = ('N = [ ', nilFrom, ':', nilEnd, ' ]')

    plt.title(xnh)
    plt.grid(True)
    plt.ylabel('Grafis Discrete Signal')
    plt.xlabel(label)
    # plt.yscale('linear')
    plt.show()
    yogiAsk()


def yoGrafis():
    pyogclr.print_pass('opening figure . . .')
    print('From : x = ', x)
    print('       n = ', n)
    grafis(n, x)


def yogiAsk():
    yogiwhatdo = input('\nfor try again other program [y/n] for exit : ')
    if yogiwhatdo == 'y':
        start()
    else:
        print(
            "\n[!] By ...: thanks for use my code (c) 2019 github.com/yogithesymbian")
        sys.exit(0)


def yoFourier():
    w1 = 100
    w2 = 150  # frequency asli
    w3 = 300  # frequency asli
    w4 = 400  # frequency asli
    N = 1000
    T = 1.0/1000
    t = np.linspace(0, N*T, N)
    y = 1*(np.sin(w1*2*np.pi*t)+np.cos(w2*2*np.pi*t) +
           np.sin(w3*2*np.pi*t)+np.cos(w4*2*np.pi*t))
    yf = scipy.fftpack.fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    plt.subplot(211)
    plt.plot(t, y)
    plt.title('Signal')
    plt.subplot(212)
    plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.title('Frekuensi')
    plt.show()


def ioGrafis():
    print("panjang isi variable x dan n adalah 6 / arr[6] ")
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
        print(
            "\n[!] By ...: thanks for use my code (c) 2019 github.com/yogithesymbian")
        sys.exit(0)
