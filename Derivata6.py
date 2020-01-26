from sympy import *
import random
import time
from sympy.parsing.sympy_parser import parse_expr
import pyperclip
from time import perf_counter
from matte import Matte
import main

# Settings
# Max polynomordning
n_st = 2
# Max tal för Pn
p_max = 10

my_math = 'Algebra'

ProblemTyp = main.ProblemTyp11

my_sign = True

edu_mode = False

#Derivata(my_math,p_max,n_st,my_sign)

print(ProblemTyp)

n_tal = 10
t0 = 0
for i in range(1, n_tal):

    # skapa varaiabeln x
    x = Symbol('x')
    #Mata in indata till klassen
    my_matte = Matte(my_math=my_math, my_sign=my_sign, p_max=p_max, n_st=n_st)

    # skapa text förpolynomet genom att köra lämplig funktion
    if ProblemTyp == 'PolynomHel':
        my_matte.hel_polynom()

    if ProblemTyp == 'PolynomHalv':
        my_matte.halv_polynom()

    if ProblemTyp == 'ExponentialE':
        my_matte.e_exp()

    if ProblemTyp == 'Exponentialn':
        my_matte.n_exp()

    if ProblemTyp == "Kedjeregeln":
        my_matte.kedjeregeln()


    #debug
    #print(my_matte.p_txt)
    #print(my_matte.n)
    #Råtext
    p_txt = my_matte.p_txt
    #antal steg i problemet
    n = my_matte.n


    if edu_mode==True:
        print('Formel')
        print(my_matte.edu_txt)
        print('')

    # läs in text, förenkla och gör om till Sympy ekvation
    y = parse_expr(p_txt)
    start = time.perf_counter()

    if my_math == 'Derivera':
        print('Derivera y(x)')
        # Skriv ut ekvationen i förenklad form
        print('y = ', y)
        # derivera y med avseende på x
        f_prime = y.diff(y)
        # Besvara frågan
        while 0 == 0:
            try:
                f_anton = parse_expr(input(str(i) + "/" + str(n_tal) + " Derivatan av y: "))
                break
            except:
                print('Typo')

    if my_math == 'Integrera':
        print('Integrera  y(x)')
        # Skriv ut ekvationen i förenklad form
        print('y = ', y)
        # integrera  y med avseende på x
        f_prime = integrate(y)
        # Besvara frågan
        while 0 == 0:
            try:
                f_anton = parse_expr(input(str(i) + "/" + str(n_tal) + " Integralen av y: "))
                break
            except:
                print('Typo')

    if my_math == 'Algebra':
        print('Utveckla y(x)')
        # Skriv ut ekvationen i förenklad form
        print('y(x) = ', y)
        # derivera y med avseende på x
        f_prime = expand(y)
        # Besvara frågan
        while 0 == 0:
            try:
                f_anton = parse_expr(input(str(i) + "/" + str(n_tal) + " : "))
                break
            except:
                print('Typo')


    if f_anton == f_prime:
        print("rätt")
    else:
        print("fel svar: " + str(f_anton))
        print('Rätt svar: ' + str(f_prime))
        break

    end = time.perf_counter()

    #snittid per problemsteg
    tid = end / n
    #total tid övad matte
    t0 = t0 + tid

print("Din tid per problemsteg:", tid)
