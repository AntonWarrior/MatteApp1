from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, OptionProperty, ObjectProperty, BooleanProperty
from kivy.graphics import RenderContext
from kivy.clock import mainthread
from matte import Matte
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from kivy.clock import Clock
from kivy.core.window import Window
import requests
import json
from datetime import datetime
import pickle

class My_Widget(Widget):

    def __init__(self):
        super(My_Widget,self).__init__()
        self.my_txt = ''

    def change_text(self):
        self.my_txt = RaknaScreen.edu_txt


#skicka över variabler till skärmarna
def start_loop(self,edu_mode):

    RaknaScreen.edu_txt = self.edu_txt
    RaknaScreen.my_math = self.problem_text
    RaknaScreen.my_math_txt = self.problem_text
    RaknaScreen.my_sign = self.my_sign
    RaknaScreen.n_st = self.n_st
    RaknaScreen.n = self.n
    RaknaScreen.antal = self.antal


#tar in data från alla knappar
class ButtonData:

    def __init__(self, problem_typ, minuter_ova_regel, felproc_ova_regel, n_st, TB0_state, TB11_state, TB12_state, antal):
        self.problem_typ = problem_typ
        self.minuter_ova_regel = minuter_ova_regel
        self.felproc_ova_regel = felproc_ova_regel
        self.n_st = n_st
        self.TB0_state = TB0_state
        self.TB11_state = TB11_state
        self.TB12_state = TB12_state
        self.antal = antal

        #        super(HomeScreen,self).__init__(problem_typ,minuter_ova_regel,felproc_ova_regel,n_st,TB0_state,TB1_state,TB2_state)

    @classmethod
    def update_button_values(cls, TB0_state, TB11_state, TB12_state, n_st, antal):
        cls.TB0_state = TB0_state
        cls.TB11_state = TB11_state
        cls.TB12_state = TB12_state
        cls.n_st = n_st
        cls.antal = antal

        return cls(TB0_state, TB11_state, TB12_state, n_st, antal)


#root
class HomeScreen(Screen):
    practice_loop = BooleanProperty(False)
    practice_loop = False
    antal = NumericProperty(0)

    try:
        #
        #outfile = open('data.txt', 'r')
        #allt = json.load(outfile)
        #outfile.close()

        with open('data.txt', 'r') as outfile:
            allt = json.load(outfile)
        outfile.close()
        #outfile.flush()

        #
        data = allt['PolynomHel']
        knapp_poly_hel = ButtonData(problem_typ='PolynomHel', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(int(100*(1-sum(data['felprocent'])/len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #
        data = allt['PolynomHel']
        knapp_poly_hel = ButtonData(problem_typ='PolynomHalv', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(int(100*(1-sum(data['felprocent'])/len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #
        data = allt['PolynomHel']
        knapp_poly_hel = ButtonData(problem_typ='ExponentialE', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(int(100*(1-sum(data['felprocent'])/len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #
        data = allt['PolynomHel']
        knapp_poly_hel = ButtonData(problem_typ='Exponentialn', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(int(100*(1-sum(data['felprocent'])/len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #
        data = allt['Kedjeregeln']
        knapp_kedjeregeln = ButtonData(problem_typ='Kedjeregeln', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(int(100*(1-sum(data['felprocent'])/len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #

    except:
        allt = dict()
        # Definiera default data för varje knapp. Ova och felprocent avses läsas från en dict
        knapp_poly_hel = ButtonData(problem_typ='PolynomHel', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=0)
        #
        knapp_poly_halv = ButtonData(problem_typ='PolynomHalv', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=0)
        #
        knapp_exp_e = ButtonData(problem_typ='ExponentialE', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=0)
        #
        knapp_exp_n = ButtonData(problem_typ='Exponentialn', minuter_ova_regel=str(0), felproc_ova_regel=str(10),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=0)
        #
        knapp_kedjeregeln = ButtonData(problem_typ='Kedjeregeln', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=0)
        #
        #dummy = ButtonData(problem_typ='none', minuter_ova_regel=str(0), felproc_ova_regel=str(10),
                      #     n_st=5, TB0_state='normal', TB11_state='normal', TB12_state='normal')

    button_homescreen = OptionProperty("None", options=["down", "normal", "None"])





    def selected_method(self, method1, method2, edu_sign):
 #       process_state = 'dummy'
#        self.my_case = HomeScreen.dummy
#        print(method1.TB0_state)
#        print(method2.TB0_state)
        #Metod 1

        if method1.TB0_state == 'down':
            self.problem_typ = method1.problem_typ
            self.minuter_ova_regel = method1.minuter_ova_regel
            self.felproc_ova_regel = method1.felproc_ova_regel
            self.TB0_state = method1.TB0_state
            self.TB11_state = method1.TB11_state
            self.TB12_state = method1.TB12_state
            self.n_st = method1.n_st
            self.antal = method1.antal
            if method1.TB11_state == 'down':
                process_state = 'Förenkla'
            if method1.TB12_state == 'down':
                process_state = 'Expandera'
            try:
                RaknaScreen.data = RaknaScreen.allt['Kedjeregeln']
                print('apa')
            except:
                try:
                    RaknaScreen.allt = HomeScreen.allt
                    RaknaScreen.data = HomeScreen.allt['Kedjeregeln']
                except:
                    print('röva')
                    RaknaScreen.data = {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}
                    RaknaScreen.allt['Kedjeregeln'] =  {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}

        #Metod 2
        if method2.TB0_state == 'down':
            self.problem_typ = method2.problem_typ
            self.minuter_ova_regel = method2.minuter_ova_regel
            self.felproc_ova_regel = method2.felproc_ova_regel
            self.TB0_state = method2.TB0_state
            self.TB11_state = method2.TB11_state
            self.TB12_state = method2.TB12_state
            self.n_st = method2.n_st
            self.antal = method2.antal
            if method2.TB11_state == 'down':
                process_state = 'Derivera'
            if method2.TB12_state == 'down':
                process_state = 'Integrera'
            try:
                RaknaScreen.data = RaknaScreen.allt['PolynomHel']
            except:
                try:
                    RaknaScreen.allt = HomeScreen.allt
                    RaknaScreen.data = HomeScreen.allt['PolynomHel']
                except:
                    RaknaScreen.data = {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}
                    RaknaScreen.allt['PolynomHel'] = RaknaScreen.data



        self.edu_sign = edu_sign
        # print(self.my_case.__dict__)
        # Skicka data till RaknaScreen


        RaknaScreen.my_math_text = self.problem_typ
        RaknaScreen.my_math = self.problem_typ
        RaknaScreen.edu_sign = self.edu_sign
        RaknaScreen.n_st = self.n_st
        RaknaScreen.antal = self.antal
        print(self.antal)
        #
        print(self.n_st)
        #
        self.process_state = process_state
        RaknaScreen.process_state = process_state




    def animate_text(self):
        Clock.schedule_interval(self.update_button, 0.1)
    #kolla label
    def update_button(self, dt):
        #TB11
        self.button_homescreen = self.knapp_kedjeregeln
        self.ids.TB11.on_press = self.button_homescreen
        self.button_homescreen = self.knapp_kedjeregeln
        self.ids.TB12.on_press = self.button_homescreen
        self.button_homescreen = self.knapp_poly_hel
        self.ids.TB11.on_press = self.button_homescreen
        self.button_homescreen = self.knapp_poly_hel
        self.ids.TB12.on_press = self.button_homescreen

        self.ids.antal.text = str(self.antal)

    @mainthread
    def update(self, *largs):

        return

    pass



class RaknaScreen(Screen):
    #
    problem_text = StringProperty('')
    my_math_text = StringProperty('')
    edu_txt = StringProperty('')
    correct_answer = StringProperty('')
    string_raknascreen = StringProperty('')
    enter_answer = ObjectProperty('')
    ratt_svar_text = StringProperty('')
    antal = NumericProperty(0)

#    problem_text = ''
#    my_math_text = ''

    #
    my_math = ''
    process_state = ''
    edu_sign = False
    my_sign = False
    n_st = 0
    n = 0
    antal = 0
    tic = 0
    toc = 0
    try:
        allt
    except:
        #Tom data dict
        data = {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}
        allt = dict()


        #allt['Kedjeregeln'] = data
        #allt['PolynomHel'] = data

    #    def __init__(self, problem_text, my_math_text, edu_txt, my_math, my_sign, n_st, n):
#        self.problem_text = problem_text
#        self.my_math_text = my_math_text
#        self.edu_txt = edu_txt
#        self.my_math = my_math
#        self.my_sign = my_sign
#        self.n_st = n_st
#        self.n = n
#        super(RaknaScreen,self).__init__(problem_text, my_math_text, edu_txt, my_math, my_sign, n_st, n)

    def tictoc(self,my_type):
        if my_type=='tic':
            RaknaScreen.tic = datetime.timestamp(datetime.now())
            round(RaknaScreen.tic, 1)

        if my_type=='toc':
            RaknaScreen.toc = datetime.timestamp(datetime.now())
            round(RaknaScreen.toc, 1)


    def do_math(self):
        # Konvertera text till integer
        n_st = int(self.n_st)
        #
        #edu_mode = True
        # Max tal för Pn
        p_max = 10
        n_st = 10
        t0 = 0

        #print(self.my_matte)
        print(self.my_math)
        print(self.my_sign)
        print(self.n_st)

        # Mata in indata till klassen
        my_matte = Matte(my_math=self.my_math, my_sign=self.my_sign, p_max=p_max, n_st=self.n_st)



        print(my_matte.__dict__)


        # skapa text förpolynomet genom att köra lämplig funktion
        if self.my_math == 'PolynomHel':
            my_matte.hel_polynom()
        if self.my_math == 'PolynomHalv':
            my_matte.halv_polynom()
        if self.my_math == 'ExponentialE':
            my_matte.e_exp()
        if self.my_math == 'Exponentialn':
            my_matte.n_exp()
        if self.my_math == "Kedjeregeln":
            my_matte.kedjeregeln()

        if self.process_state == 'Derivera':
            self.my_math_text = 'Derivera'
            self.problem_text = str(my_matte.y)
            self.correct_answer = str(my_matte.y_diff)

        if self.process_state == 'Integrera':
            self.my_math_text = 'Integrera'
            self.problem_text = str(my_matte.y)
            self.correct_answer = str(my_matte.y_integrate)

        elif self.process_state == 'Förenkla':
            self.my_math_text = 'Förenkla'
            #Specialfall
            self.problem_text = str(my_matte.y_integrate)
            self.correct_answer = str(my_matte.y_diff)

        elif self.process_state == 'Expandera':
            self.my_math_text = 'Expandera'
            self.problem_text = str(my_matte.y)
            self.correct_answer = str(my_matte.y_integrate)

        #print(self.my_sign)

        if self.edu_sign == True:
            self.edu_txt = str(my_matte.edu_txt)
        else:
            self.edu_txt = ''

        #print(my_math_text)
        print(my_matte.p_txt)

        # antal steg i problemet
        self.n = my_matte.n

        RaknaScreen.correct_answer = self.correct_answer
        correct_answer = self.correct_answer
        #print(str(correct_answer))

        RaknaScreen.problem_text2 = self.problem_text
        RaknaScreen.my_math_text = self.my_math_text
        RaknaScreen.edu_txt = self.edu_txt
        # self.compound_text = my_math_text + ": y = " + problem_text

        RaknaScreen.my_math = self.my_math
        RaknaScreen.my_sign = self.my_sign
        RaknaScreen.n_st = self.n_st
        RaknaScreen.n = self.n
        RaknaScreen.antal = self.antal

        problem_text = self.problem_text
        my_math_text = self.my_math_text
        edu_txt = self.edu_txt
        # self.compound_text = my_math_text + ": y = " + problem_text

        my_math = self.my_math
        my_sign = self.my_sign
        n_st = self.n_st
        n = self.n
        self.antal += 1
        antal = self.antal
        print(antal)

        #data = {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}
        #with open('data.txt', 'w') as outfile:
        RaknaScreen.data['antal'].append(antal)
        RaknaScreen.data['timestamp'].append(RaknaScreen.tic)
        RaknaScreen.data['dt'].append((RaknaScreen.toc - RaknaScreen.tic)/n_st/60)

        if RaknaScreen.ratt_svar_text== 'Rätt Svar!':
            RaknaScreen.data['felprocent'].append(1)
        else:
            RaknaScreen.data['felprocent'].append(0)

        print(self.my_math)
        try:
            RaknaScreen.allt[self.my_math]['antal'].append(RaknaScreen.data['antal'].pop(len(RaknaScreen.data['antal'])))
            RaknaScreen.allt[self.my_math]['timestamp'].append(RaknaScreen.data['timestamp'].pop(len(RaknaScreen.data['timestamp'])))
            RaknaScreen.allt[self.my_math]['dt'].append(RaknaScreen.data['dt'].pop(len(RaknaScreen.data['dt'])))
            RaknaScreen.allt[self.my_math]['felprocent'].append(RaknaScreen.data['felprocent'].pop(len(RaknaScreen.data['felprocent'])))
        except:
            #RaknaScreen.allt[self.my_math] = dict()
            RaknaScreen.allt[self.my_math]['antal'] = list(RaknaScreen.data['antal'])
            RaknaScreen.allt[self.my_math]['timestamp'] = list(RaknaScreen.data['timestamp'])
            RaknaScreen.allt[self.my_math]['dt'] = list(RaknaScreen.data['dt'])
            RaknaScreen.allt[self.my_math]['felprocent'] = list(RaknaScreen.data['felprocent'])

        #print(RaknaScreen.data)
        print(RaknaScreen.allt)
        #json.dump(data, outfile)

        #bugkoll
        print(self.my_math)
        print(self.my_math_text)
        print('y = ', my_matte.y)
        print('correct answer = ', self.correct_answer)
        print(my_matte.y_integrate)
        print(my_matte.y_diff)

        # print(self.my_sign)



        return problem_text, my_math_text, edu_txt, my_math, my_sign, n_st, n, correct_answer, antal


  #  def __init__(self,**kwargs):
   #     super(RaknaScreen.correct_answer_text, self).__init__(**kwargs)
    #   Window.bind(on_key_down=self._on_keyboard_down)

   #def _on_keyboard_down(self, inantalance, keyboard, keycode, text, modifiers):
    #    if self.RaknaScreen.skriv_har and keycode == 40:  # 40 - Enter key pressed
     #       self.abc()

    #def abc(self):
     #   print('Test')

    def check_my_answer(self,my_answer_txt):
        #print(my_answer_txt)
        #print( RaknaScreen.correct_answer)
        x1 = parse_expr(RaknaScreen.correct_answer)
        x2 = parse_expr(my_answer_txt)
        print(x1 == x2)
        if x1 == x2:
            ratt_svar_text = 'Rätt Svar!'
        else:
            ratt_svar_text = 'Fel! - Rätt svar är: ' + RaknaScreen.correct_answer
        print(ratt_svar_text)
        RaknaScreen.ratt_svar_text = ratt_svar_text
        self.ratt_svar_text = ratt_svar_text
        RaknaScreen.antal = self.antal
        #
        #outfile = open('data.txt', 'w')
        #json.dump(RaknaScreen.allt, outfile)
        #print('Dump2: data.txt')
        #outfile.close()

        with open('data.txt', 'w') as outfile:
            json.dump(RaknaScreen.allt, outfile)

        print('Dump2: data.txt')


        #
        #print(HomeScreen.practice_loop)
        if HomeScreen.practice_loop==False:
            print('a')
            RaknaScreen.do_math(self)




    #klocka för att uppdatera label
    def animate_text(self):
        Clock.schedule_interval(self.update_label, 0.1)
        Clock.schedule_interval(self.focus_text_input, 0.1)
    # #
    #        Clock.schedule_interval(RaknaScreen.update_label(self,0.1), 0.1)

    #kolla label
    def update_label(self,dt):
        #edu text
        self.string_raknascreen = self.edu_txt
        self.ids.ED_1.text = self.string_raknascreen
        self.ids.raknare.text = 'Antal: ' + str(self.antal)

    def focus_text_input(self, dt):
        self.ids.ratt_svar_id.focus = True




   # def skicka_text(self, antal):

    #    antal = {'antal': '0' + antal}
#
 #       with open('data.pickle', 'wb') as handle:
  #          pickle.dump(antal, handle)

   #     with open('data.pickle', 'rb') as handle:
    #        b = pickle.load(handle)

     #   print(antal == b)
        #correct answer
 #       self.string_raknascreen = self.correct_answer
 #       self.ids.correct_answer.text = self.ratt_svar_text
 #       RaknaScreen.ratt_svar_text = self.ratt_svar_text

    @mainthread
    def update(self, *largs):
        return

    pass


#läs in Gui't
GUI = Builder.load_file("main.kv")
#app
class MainApp(App):

    canvas = RenderContext()
    felproc_ova_regel = 2
    antal = 1

    def build(self):
        return GUI

    def on_start(self):
        #hämta firebase datan
        result = requests.get("https://derivataapp1.firebaseio.com/" + str(self.antal) + ".json")
        print("was it okay?", result.ok)
        #dekoda binär data från firebase
        data = json.loads(result.content.decode())
        print(data)


    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        print(HomeScreen.practice_loop==False)

    def update_canvas(self):
        s = MainApp.canvas
        s.ask_update()




#run app
MainApp().run()
