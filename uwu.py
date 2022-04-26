import pyautogui as pg, time
import random

f = open("xd.txt","r")

def spam():
  f = open("ocupado.txt","r")
  for linea in f:
    pg.write(linea)
    pg.press('enter')
    time.sleep(random.randint(1,8))    
  f.close()


def repeticiones(num):
  for x in range(0,num):
    spam()

rep = int(input("Cuántas veces quieres enviar este regalo al José? :"))
time.sleep(10)
repeticiones(rep)


'''

ZONA DE PRUEBAS.EXE

'''









