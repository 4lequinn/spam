import pyautogui as pg, time

f = open("xd.txt","r")

def spam():
  f = open("xd.txt","r")
  for linea in f:
    pg.write(linea)
    pg.press('enter')
  f.close()


def repeticiones(num):
  for x in range(0,num):
    spam()
1
rep = int(input("Cuántas veces quieres enviar este regalo al José? :"))
time.sleep(10)
repeticiones(rep)


'''

ZONA DE PRUEBAS.EXE

'''









