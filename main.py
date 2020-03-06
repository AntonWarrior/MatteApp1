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
from kivy.core.clipboard import Clipboard

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



def i_do_startup():
    try:
        with open('data.txt', 'r') as outfile:
            allt = json.load(outfile)
            readfile = True
        outfile.close()
        # outfile.flush()
    except:
        allt = dict()

        allt['Kedjeregeln'] = {'antal': [0], 'timestamp': [0], 'felprocent': [0], 'dt': [0]}

        allt['PolynomHel'] = {'antal': [0], 'timestamp': [0], 'felprocent': [0], 'dt': [0]}

        allt['PolynomHalv'] = {'antal': [0], 'timestamp': [0], 'felprocent': [0], 'dt': [0]}

        allt['ExponentialE'] = {'antal': [0], 'timestamp': [0], 'felprocent': [0], 'dt': [0]}

        allt['Exponentialn'] = {'antal': [0], 'timestamp': [0], 'felprocent': [0], 'dt': [0]}
        readfile = False

    return allt, readfile

def update_values(allt,readfile):

    if readfile == True:
        try:
            data = allt['Kedjeregeln']
        except:
            data = {'antal': [0], 'timestamp': [0], 'felprocent': [100], 'dt': [0]}
        knapp_kedjeregeln = ButtonData(problem_typ='Kedjeregeln', minuter_ova_regel=str(round(sum(data['dt'], 1))),
                                       felproc_ova_regel=str(int(100 * (1 - sum(data['felprocent']) / len(data['felprocent'])))),
                                        n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                        antal=str(len(data['antal'])))
        #
        try:
            data = allt['PolynomHel']
        except:
            data = {'antal': [0], 'timestamp': [0], 'felprocent': [100], 'dt': [0]}
        knapp_poly_hel = ButtonData(problem_typ='PolynomHel', minuter_ova_regel=str(round(sum(data['dt']), 1)),
                                    felproc_ova_regel=str(int(100 * (1 - sum(data['felprocent']) / len(data['felprocent'])))),
                                    n_st=2, TB0_state='down', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        try:
            data = allt['PolynomHalv']
        except:
            data = {'antal': [0], 'timestamp': [0], 'felprocent': [100], 'dt': [0]}
        knapp_poly_halv = ButtonData(problem_typ='PolynomHalv', minuter_ova_regel=str(sum(data['dt'])),
                                     felproc_ova_regel=str(int(100 * (1 - sum(data['felprocent']) / len(data['felprocent'])))),
                                     n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                     antal=str(len(data['antal'])))
        #
        try:
            data = allt['ExponentialE']
        except:
            data = {'antal': [0], 'timestamp': [0], 'felprocent': [100], 'dt': [0]}
        knapp_exp_e = ButtonData(problem_typ='ExponentialE', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(int(100*(1-sum(data['felprocent'])/len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #
        try:
            data = allt['Exponentialn']
        except:
            data = {'antal': [0], 'timestamp': [0], 'felprocent': [100], 'dt': [0]}
        knapp_exp_n = ButtonData(problem_typ='Exponentialn', minuter_ova_regel=str(sum(data['dt'])),
                                    felproc_ova_regel=str(
                                        int(100 * (1 - sum(data['felprocent']) / len(data['felprocent'])))),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal',
                                    antal=str(len(data['antal'])))
        #
    elif readfile == False:
        # Definiera default data för varje knapp. Ova och felprocent avses läsas från en dict
        knapp_kedjeregeln = ButtonData(problem_typ='Kedjeregeln', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                       n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=str(0))

        knapp_poly_hel = ButtonData(problem_typ='PolynomHel', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=str(0))

        knapp_poly_halv = ButtonData(problem_typ='PolynomHalv', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=str(0))
        #
        knapp_exp_e = ButtonData(problem_typ='ExponentialE', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                    n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=str(0))
        #
        knapp_exp_n = ButtonData(problem_typ='Exponentialn', minuter_ova_regel=str(0), felproc_ova_regel=str(0),
                                  n_st=2, TB0_state='normal', TB11_state='down', TB12_state='normal', antal=str(0))
    #
    return  knapp_kedjeregeln, knapp_poly_hel, knapp_poly_halv, knapp_exp_e, knapp_exp_n

#root
class HomeScreen(Screen):
    practice_loop = BooleanProperty(False)
    practice_loop = False
    antal = NumericProperty(0)
    button_homescreen = OptionProperty("None", options=["down", "normal", "None"])

    #check if file is present, read it if so
    allt,readfile = i_do_startup()
    #update values of allt
    def i_do_a_method(self, method, method_name):
        self.problem_typ = method.problem_typ
        self.minuter_ova_regel = method.minuter_ova_regel
        self.felproc_ova_regel = method.felproc_ova_regel
        self.TB0_state = method.TB0_state
        self.TB11_state = method.TB11_state
        self.TB12_state = method.TB12_state
        self.n_st = method.n_st
        self.antal = method.antal
        process_state = 'None'
        if method_name == 'Kedjeregeln':
            if method.TB11_state == 'down':
                process_state = 'Förenkla'
            if method.TB12_state == 'down':
                process_state = 'Expandera'
        else:
            if method.TB11_state == 'down':
                process_state = 'Derivera'
            if method.TB12_state == 'down':
                process_state = 'Integrera'
        try:
            allt = RaknaScreen.allt
            data = RaknaScreen.allt[method_name]
        except:
            try:
                allt = HomeScreen.allt
                data = HomeScreen.allt[method_name]
            except:
                data = {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}
                allt = dict()
                allt[method_name] = data
        return data, allt, process_state

    def selected_method(self, method1, method2, method3, method4, method5, edu_sign):
        #Metod 1
        if method1.TB0_state == 'down':
            #print('method1')
            RaknaScreen.data, RaknaScreen.allt, process_state = HomeScreen.i_do_a_method(self, method1, 'Kedjeregeln')
            #
        #Metod 2
        if method2.TB0_state == 'down':
            #print('method2')
            RaknaScreen.data, RaknaScreen.allt, process_state = HomeScreen.i_do_a_method(self, method2, 'PolynomHel')
            #
        #Metod 3
        if method3.TB0_state == 'down':
            #print('method3')
            RaknaScreen.data, RaknaScreen.allt, process_state = HomeScreen.i_do_a_method(self, method3, 'PolynomHalv')
            #
        #Metod 4
        if method4.TB0_state == 'down':
            #print('method4')
            RaknaScreen.data, RaknaScreen.allt, process_state = HomeScreen.i_do_a_method(self, method4, 'ExponentialE')
            #
        #Metod 5
        if method5.TB0_state == 'down':
            #print('method5')
            RaknaScreen.data, RaknaScreen.allt, process_state = HomeScreen.i_do_a_method(self, method5, 'Exponentialn')
            #

        self.edu_sign = edu_sign

        # Skicka data till RaknaScreen
        RaknaScreen.my_math_text = self.problem_typ
        RaknaScreen.my_math = self.problem_typ
        RaknaScreen.edu_sign = self.edu_sign
        RaknaScreen.n_st = self.n_st
        RaknaScreen.antal = self.antal
        ##print(self.antal)
        #
        ##print(self.n_st)
        #
        ##print(self.problem_typ)
        #self.process_state = process_state
        RaknaScreen.process_state = process_state

    def verify_ids(self,knapp_kedjeregeln,knapp_poly_hel):
        go_on = False
        if knapp_poly_hel.TB0_state=='down':
            go_on = True
        if knapp_kedjeregeln.TB0_state=='down':
            go_on = True
        return go_on

    #klocka för att uppdatera label
    def on_enter(self, *args):
        HomeScreen.knapp_kedjeregeln, HomeScreen.knapp_poly_hel, HomeScreen.knapp_poly_halv, HomeScreen.knapp_exp_e, HomeScreen.knapp_exp_n  = update_values(HomeScreen.allt, HomeScreen.readfile)
        #
        Clock.schedule_once(self.update_label2, 1)

    #kolla label
    def update_label2(self,dt):

        self.ids.R1antal.text = str(HomeScreen.knapp_kedjeregeln.antal)
        self.ids.R1min.text = str(HomeScreen.knapp_kedjeregeln.minuter_ova_regel)
        self.ids.R1proc.text = str( HomeScreen.knapp_kedjeregeln.felproc_ova_regel)
        #
        self.ids.R2antal.text = str(HomeScreen.knapp_poly_hel.antal)
        self.ids.R2min.text = str(HomeScreen.knapp_poly_hel.minuter_ova_regel)
        self.ids.R2proc.text = str(HomeScreen.knapp_poly_hel.felproc_ova_regel)
        #
        self.ids.R3antal.text = str(HomeScreen.knapp_poly_halv.antal)
        self.ids.R3min.text = str(HomeScreen.knapp_poly_halv.minuter_ova_regel)
        self.ids.R3proc.text = str(HomeScreen.knapp_poly_halv.felproc_ova_regel)
        #
        self.ids.R4antal.text = str(HomeScreen.knapp_exp_e.antal)
        self.ids.R4min.text = str(HomeScreen.knapp_exp_e.minuter_ova_regel)
        self.ids.R4proc.text = str(HomeScreen.knapp_exp_e.felproc_ova_regel)
        #
        self.ids.R5antal.text = str(HomeScreen.knapp_exp_n.antal)
        self.ids.R5min.text = str(HomeScreen.knapp_exp_n.minuter_ova_regel)
        self.ids.R5proc.text = str(HomeScreen.knapp_exp_n.felproc_ova_regel)
        #

    @mainthread
    def update(self, *largs):

        return
    pass



class RaknaScreen(Screen):
    #
    problem_text = StringProperty('')
    my_math_text = StringProperty('')
    edu_txt = StringProperty('')
    pyperclip_txt = StringProperty('')
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
        allt = HomeScreen.allt
    else:
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

    def i_update_allt(self,allt_to_update):
        #print(allt_to_update)
        HomeScreen.allt = allt_to_update
        self.allt = allt_to_update
        update_values(allt_to_update,True)

    def tictoc(self,my_type):
        if my_type=='tic':
            RaknaScreen.tic = datetime.timestamp(datetime.now())

        if my_type=='toc':
            RaknaScreen.toc = datetime.timestamp(datetime.now())


    def do_math(self):
        # Konvertera text till integer
        n_st = int(self.n_st)
        #
        #edu_mode = True
        # Max tal för Pn
        p_max = 10
        n_st = 10
        t0 = 0

        ##print(self.my_matte)
        #print(self.my_math)
        #print(self.my_sign)
        #print(self.n_st)

        # Mata in indata till klassen
        my_matte = Matte(my_math=self.my_math, my_sign=self.my_sign, p_max=p_max, n_st=self.n_st)

        #print(my_matte.__dict__)

        # skapa text förpolynomet genom att köra lämplig funktion
        if self.my_math == 'Kedjeregeln':
            my_matte.kedjeregeln()
            pyperclip_txt = my_matte.pyperclip_txt
        if self.my_math == 'PolynomHel':
            my_matte.hel_polynom()
            pyperclip_txt = my_matte.pyperclip_txt
        if self.my_math == 'PolynomHalv':
            my_matte.halv_polynom()
            pyperclip_txt = my_matte.pyperclip_txt
        if self.my_math == 'ExponentialE':
            my_matte.e_exp()
            pyperclip_txt = my_matte.pyperclip_txt
        if self.my_math == 'Exponentialn':
            my_matte.n_exp()
            pyperclip_txt = my_matte.pyperclip_txt

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

        ##print(self.my_sign)

        if self.edu_sign == True:
            self.edu_txt = str(my_matte.edu_txt)
        else:
            self.edu_txt = ''

        ##print(my_math_text)
        #print(my_matte.p_txt)

        # antal steg i problemet
        self.n = my_matte.n

        #print(pyperclip_txt)
        Clipboard.copy(pyperclip_txt)
        self.pyperclip_txt = pyperclip_txt
        RaknaScreen.pyperclip_txt = pyperclip_txt

        RaknaScreen.correct_answer = self.correct_answer
        correct_answer = self.correct_answer
        ##print(str(correct_answer))

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
        #print(antal)

        #data = {'antal': [], 'timestamp': [], 'felprocent': [], 'dt': []}
        #with open('data.txt', 'w') as outfile:
        RaknaScreen.data['antal'].append(antal)
        RaknaScreen.data['timestamp'].append(RaknaScreen.tic)
        RaknaScreen.data['dt'].append(round((RaknaScreen.toc - RaknaScreen.tic)/n_st/60,1))

        if RaknaScreen.ratt_svar_text== 'Rätt Svar!':
            RaknaScreen.data['felprocent'].append(1)
        else:
            RaknaScreen.data['felprocent'].append(0)

        #print(self.my_math)
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

        ##print(RaknaScreen.data)
        #print(RaknaScreen.allt)
        #json.dump(data, outfile)

        #bugkoll
        #print(self.my_math)
        #print(self.my_math_text)
        #print('y = ', my_matte.y)
        #print('correct answer = ', self.correct_answer)
        #print(my_matte.y_integrate)
        #print(my_matte.y_diff)

        # #print(self.my_sign)



        return problem_text, my_math_text, edu_txt, my_math, my_sign, n_st, n, correct_answer, antal


  #  def __init__(self,**kwargs):
   #     super(RaknaScreen.correct_answer_text, self).__init__(**kwargs)
    #   Window.bind(on_key_down=self._on_keyboard_down)

   #def _on_keyboard_down(self, inantalance, keyboard, keycode, text, modifiers):
    #    if self.RaknaScreen.skriv_har and keycode == 40:  # 40 - Enter key pressed
     #       self.abc()

    #def abc(self):
     #   #print('Test')

    def check_my_answer(self,my_answer_txt):

        try:
            ##print(my_answer_txt)
            ##print( RaknaScreen.correct_answer)
            x1 = parse_expr(RaknaScreen.correct_answer)
            x2 = parse_expr(my_answer_txt)
            #print(x1 == x2)
            if x1 == x2:
                ratt_svar_text = 'Rätt Svar!'
            else:
                ratt_svar_text = 'Fel! - Rätt svar är: ' + RaknaScreen.correct_answer
            #print(ratt_svar_text)
            RaknaScreen.ratt_svar_text = ratt_svar_text
            self.ratt_svar_text = ratt_svar_text
            RaknaScreen.antal = self.antal
            #
            #outfile = open('data.txt', 'w')
            #json.dump(RaknaScreen.allt, outfile)
            ##print('Dump2: data.txt')
            #outfile.close()

            with open('data.txt', 'w') as outfile:
                json.dump(RaknaScreen.allt, outfile)

            #print('Dump2: data.txt')
            # #print(HomeScreen.practice_loop)
            if HomeScreen.practice_loop == False:
                RaknaScreen.do_math(self)
        except:
            RaknaScreen.ratt_svar_text = 'Skräptecken räknas inte'
            self.ratt_svar_text = 'Skräptecken räknas inte'
            RaknaScreen.antal = self.antal
        #


    #klocka för att uppdatera label
    def on_enter(self, *args):
        #print('rakna')
        allt = HomeScreen.allt
        RaknaScreen.do_math(self)
        RaknaScreen.tictoc(self,'tic')
        RaknaScreen.tictoc(self,'toc')
        Clock.schedule_interval(self.update_label, 0.1)
        Clock.schedule_interval(self.focus_text_input, 0.1)
        return allt
    # #
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

     #   #print(antal == b)
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
        #print("was it okay?", result.ok)
        #dekoda binär data från firebase
        data = json.loads(result.content.decode())
        #print(data)



    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        #print(HomeScreen.practice_loop==False)



  #  def home_refresh(zz):
   #     #print('home_refresh')
    #    HomeScreen.animate_text2(HomeScreen.__self__)

    #def rakna_refresh(xx):
     #   #print('rakna_refresh')
      #  #print(RaknaScreen.__self__)
       # RaknaScreen.animate_text(RaknaScreen.__self__)



#run app
MainApp().run()
