import random
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class Matte():

    def __init__(self, my_math,p_max,n_st,my_sign):
        #inputs
        x = Symbol('x')
        self.my_math = my_math
        self.p_max = p_max
        self.n_st = n_st
        self.my_sign = my_sign
        #outputs
        self.p_txt = ''
        self.n = 0
        self.edu_txt = ''
        self.pyperclip_txt = ''
        self.y = ''
        self.y_diff = ''
        self.y_integrate = ''

    def hel_polynom(self):
        #educational mode text
        self.edu_txt = 'y = x => y'' = x^(n-1), e.g. y = 5*x^3 => y'' = 5*3*x^2'
        # Store convenient text in Clipboard
        self.pyperclip_txt = '*x**'
        # Slumpa polynomordningen
        self.n = random.randint(0, self.n_st - 1) + 2
        # print(self.n)
        for i in range(0, self.n):
            px = random.randint(0, self.p_max)
            # bygg texten
            if self.my_sign == False:
                self.p_txt = self.p_txt + ' ' + str(px) + '*x**' + str(i)
            if self.my_sign == True:
                self.p_txt = self.p_txt + ' ' + str(random.choice((-1, 1))) + '*' + str(px) + '*x**(' + str(
                    random.choice((-1, 1))) + '*' + str(i) + ')'
            if i < self.n - 1:
                self.p_txt = self.p_txt + ' + '
        #
        #print(self.p_txt)
        # skapa varaiabeln x
        x = Symbol('x')
        self.y = parse_expr(self.p_txt)
        #derivatan
        self.y_diff = diff(self.y)
        #Integrera
        self.y_integrate = integrate(self.y)
        # sprint(y)
        return self.p_txt, self.n, self.edu_txt, self.pyperclip_txt,  self.y, self.y_diff, self.y_integrate

    def kedjeregeln(self):
        #educational mode text
        self.edu_txt = '(a-b)*(c+d) = a*c + a*d - b*c - b*d'
        # Store convenient text in Clipboard
        self.pyperclip_txt = '*'
        # Slumpa polynomordningen
        self.n = random.randint(0, self.n_st - 1) + 1
        # print(self.n)
        for i in range(0, self.n):
            px = random.randint(0, self.p_max)
            # bygg texten
            if self.my_sign == False:
                self.p_txt = self.p_txt + ' ' + '(' + str(px) + '+' + str(random.choice((-1, 1))) + '*' + str(px) + '*x**' + str(px) + ') *'
            if self.my_sign == True:
                self.p_txt = self.p_txt + ' '
            if i == self.n-1:
                self.p_txt = self.p_txt[:-1]
        #
        print(self.p_txt)
        #y = parse_expr(self.p_txt)
        #print(y)
        x = Symbol('x')
        self.y = parse_expr(self.p_txt)
        # derivatan
        print(self.y)
        self.y_diff = self.y
        # Integrera
        self.y_integrate = expand(self.y)
        # sprint(y)
        return self.p_txt, self.n, self.edu_txt, self.pyperclip_txt,  self.y, self.y_diff, self.y_integrate

    def halv_polynom(self):
        self.edu_txt = 'y = x => y'' = x^(n-1), e.g. y = 5*x^3 => y'' = 5*3*x^2'
        # Store convenient text in Clipboard
        self.pyperclip_txt = '*x**'
        # Slumpa polynomordningen
        self.n = random.randint(0, self.n_st - 1) + 2
        # print(self.n)
        for i in range(1, self.n):
            px = random.randint(0, self.p_max)
            # bygg texten
            if self.my_sign == False:
                self.p_txt = self.p_txt + ' ' + str(px) + '*x**(1/' + str(i) + ')'
            if self.my_sign == True:
                self.p_txt = self.p_txt + ' ' + str(random.choice((-1, 1))) + '*' + str(px) + '*x**(' + str(
                    random.choice((-1, 1))) + '*1/' + str(i) + ')'
            if i < self.n - 1:
                self.p_txt = self.p_txt + ' + '
        #
        # print(p_txt)
        # skapa varaiabeln x
        x = Symbol('x')
        self.y = parse_expr(self.p_txt)
        #derivatan
        self.y_diff = diff(self.y)
        #Integrera
        self.y_integrate = integrate(self.y)
        # sprint(y)
        return self.p_txt, self.n, self.edu_txt, self.pyperclip_txt,  self.y, self.y_diff, self.y_integrate


    def e_exp(self):
        self.edu_txt = 'y = x => y'' = x^(n-1), e.g. y = 5*x^3 => y'' = 5*3*x^2'
        # Store convenient text in Clipboard
        self.pyperclip_txt = '*x**'
        #pyperclip.copy('*exp(x*')
        # Slumpa polynomordningen
        self.n = random.randint(0, self.n_st - 1) + 2
        # print(n)
        for i in range(0, self.n):
            px = random.randint(0, self.p_max)
            # bygg texten
            if self.my_sign == False:
                self.p_txt = self.p_txt + ' ' + str(px) + '*exp(' + str(i) + '*x)'
            if self.my_sign == True:
                self.p_txt = self.p_txt + ' ' + str(random.choice((-1, 1))) + '*' + str(px) + '*exp(' + str(
                    random.choice((-1, 1))) + '*' + str(i) + '*x)'
            if i < self.n - 1:
                self.p_txt = self.p_txt + ' + '
        #
        # skapa varaiabeln x
        x = Symbol('x')
        self.y = parse_expr(self.p_txt)
        #derivatan
        self.y_diff = diff(self.y)
        #Integrera
        self.y_integrate = integrate(self.y)
        # sprint(y)
        return self.p_txt, self.n, self.edu_txt, self.pyperclip_txt,  self.y, self.y_diff, self.y_integrate


    def n_exp(self):
        self.edu_txt = 'y = x => y'' = x^(n-1), e.g. y = 5*x^3 => y'' = 5*3*x^2'
        # Store convenient text in Clipboard
        self.pyperclip_txt = '*x**'
        # STore convenient text in Clipboard
        #pyperclip.copy('*exp(x*')
        self.n = random.randint(0, self.n_st - 1) + 2
        # Slumpa basen a
        a = random.randint(1, 11)
        # print(n)
        # Skapa polynomet med ordning n
        for i in range(0, self.n):
            px = random.randint(0, self.p_max)
            # bygg texten
            if self.my_sign == False:
                self.p_txt = self.p_txt + ' ' + str(px) + '*' + str(a) + '**(' + str(i) + '*x)'
            if self.my_sign == True:
                self.p_txt = self.p_txt + ' ' + str(random.choice((-1, 1))) + '*' + str(px) + '*' + str(a) + '**(' + str(
                    random.choice((-1, 1))) + '*' + str(i) + '*x)'
            if i < self.n - 1:
                self.p_txt = self.p_txt + ' + '
        #
        # skapa varaiabeln x
        x = Symbol('x')
        self.y = parse_expr(self.p_txt)
        #derivatan
        self.y_diff = diff(self.y)
        #Integrera
        self.y_integrate = integrate(self.y)
        # sprint(y)
        return self.p_txt, self.n, self.edu_txt, self.pyperclip_txt,  self.y, self.y_diff, self.y_integrate
