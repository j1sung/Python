from tkinter import *
import random
import pygame


window = Tk()


Dalssak = ["가위", "바위","보"]

scissors = PhotoImage(file ="select.png")
rock = PhotoImage(file = "fist.png")
paper = PhotoImage(file = "hand.png")


def PrintChoice_S(pick):
    Label(window, text = "당신은 가위를 선택하셨습니다.", padx =20).pack()
    if(pick == "가위"):
        Label(window, text = "비겼으니까 다시해!!!", padx =20).pack()
        srp()
    elif(pick == "바위"):
        ending2()
    else:
        ending1()
    
def PrintChoice_R(pick):
    Label(window, text = "당신은 바위를 선택하셨습니다.", padx =20).pack()
    if(pick == "바위"):
        Label(window, text = "비겼으니까 다시해!!!", padx =20).pack()
        srp()
    elif(pick == "보"):
        ending2()
    else:
        ending1()

def PrintChoice_P(pick):
    Label(window, text = "당신은 보를 선택하셨습니다.", padx =20).pack()
    if(pick == "보"):
        Label(window, text = "비겼으니까 다시해!!!", padx =20).pack()
        srp()
    elif(pick == "가위"):
        ending2()
    else:
        ending1()

def ending1():
    Label(window, text = "You Win!", padx =20).pack()
    print("Happy Ending")

def ending2():
    Label(window, text = "You Died", padx =20).pack()
    print("Sad Ending")

    

def srp():
        window.title("가위바위보")
        choice= IntVar()
        pick = random.choice(Dalssak)
        
        Label(window, text = "가위 바위 보 중에서 고르시오", padx =20).pack()
        s_btn = Radiobutton(window, text = "가위", padx = 20, variable = choice, command = lambda: PrintChoice_S(pick),value = 1, image = scissors).pack(anchor=W)
        r_btn = Radiobutton(window, text = "바위", padx = 20, variable = choice, command = lambda: PrintChoice_R(pick),value = 2, image = rock).pack(anchor=W)
        p_btn = Radiobutton(window, text = "보", padx = 20, variable = choice, command = lambda: PrintChoice_P(pick),value = 3, image = paper).pack(anchor=W)
        

srp()  
window.mainloop()
