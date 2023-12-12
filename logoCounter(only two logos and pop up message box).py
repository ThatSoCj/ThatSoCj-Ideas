import pyautogui
import pynput
def test():
    print(pyautogui.size())
    for i in range(2): # Move mouse in a square.
        pyautogui.moveTo(1400, 890, duration=0.25)
    #2560 × 1664)





def calculation():
    oneLogo = int(pyautogui.prompt("How many logos are there?"))
    goal = int(pyautogui.prompt("How much you need to make?"))
    calc = goal // oneLogo
    remainder = goal % oneLogo
    if remainder >= 0.5:
        print(f"{calc} and a half sheets")
    if remainder <0.5:
        print(f"{calc} and almost a half sheet")
    else:
        print(calc, "sheets")
        

def checker(i):
    while True:
        user = input(i)
        if user.isdigit():
            user = int(user)
            return user
        if user ==0:
            return False
        else:
            print("not valid. Use a positive number")
            
d = {} # logos and amount
L = [] #goal
A =[] # how many for goal
logo = []
def logosDictionary():
    difLog = 2  # user input
    if difLog > 0:
        for i in range(1, difLog + 1):
            logos = checker(f"How many logos are there for logo {i}? ")# user input
            d[i] = logos # add things to dictionary
            #print(d)
            answer = checker("goal?") # user input
            L.append(int(answer)) # add things to list
            #print(L)
            #print(L[i -1:])
        #return [d,L]
    else:
        print("unvalid")
        logosDictionary()
        
        
    #-------------------------------------
    
    for i in d:
        math = L[i-1] / d[i]
        answer = L[i-1] // d[i]
        remainder = L[i-1] % d[i]
        
        if remainder ==0:
            print("-----------------------------------")
            print(f"logo({i}) you need {answer} sheets")
            A.append(float(math))
        elif 0 <remainder< 5:
            print("------------------------------------------------------------")
            print(f"logo({i}) you need {answer} and less then an half of sheet")
            A.append(float(math))
        elif remainder == 5:
            print("----------------------------------------------")
            print(f"logo({i}) you need {answer} and a half sheet")
            A.append(float(math))
        else: #5 <remainder< 9:
            print("the logos are higher then the goal.")
            print("Try to equal the logos with the goal.")
            print("this will restart!!")
            logosDictionary()

    
    #print(A)
    return d, L, A        



def start():
    #d = {}  logos and amount
    #L = [] goal
    #A =[]  how many for goal
    d,L,A = logosDictionary()
    for key, num in d.items():
        #print(f"There are {key}")
        stuff.append(int(key))
    logAmount = combind()
    #print("you can now press shift and s")

    #return logAmount
       
        



    #pyautogui.alert(f"you need {x}")

def combind():
    logAmount = dict(zip(stuff, A))
    return logAmount
    

#--------------



#--------------

goalcount = 0
stuff = []
def execute1():
    logAmount = combind()
    global goalcount
    goalcount +=1
    pyautogui.click()
    for i in logAmount:
        if logAmount[i] <= goalcount:
            print("--------------------")
            print(f"logo({i}) is finish")
            print(goalcount,"sheet")
        else:
            print("--------------------")
            print(f"logo({i}) is not done")
            print(goalcount,"sheet")
        

    #print(stuff)
        
    #print(f"Shift + S hotkey detected {goalcount}")
    #pyautogui.prompt('What is your name?')
    return goalcount






import tkinter as tk
import random
from bindglobal import BindGlobal

rng = random.SystemRandom()

def Draw():
    global text
    start()
    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=0)
    frame.place(relx = 0.5, rely = 0.5, anchor = 'center')
    text=tk.Label(frame,text='HELLO', font = "Helvetica 15 bold", justify='center')
    text.configure(text=" Welcome to the Logo Counter", fg ="white", bg = "black")
    text.pack()
    
    
    


def Refresher(e):
    global text
    logAmount = combind()
    global goalcount
    goalcount +=1
    
    if logAmount[1] > goalcount and logAmount[2] > goalcount:
        text.configure(text=f"logo(1) and logo(2) \n are not done\n \nsheet count({goalcount}) ", fg ="white", bg = "black")
        pyautogui.click()
    elif logAmount[1] <= goalcount and logAmount[2] > goalcount:
        text.configure(text=f"logo(1) is done \n logo(2) is not done\n\nsheet count({goalcount})", fg ="white", bg = "black")
        pyautogui.click()
    elif logAmount[1] > goalcount and logAmount[2] <= goalcount:
        text.configure(text=f"logo(1) is not done \n logo(2) is done\n\nsheet count({goalcount})", fg ="white", bg = "black")
        pyautogui.click()
    elif logAmount[1] <= goalcount and logAmount[2] <= goalcount:
        text.configure(text=f"Both logos are done\n\nsheet count({goalcount})", fg ="white", bg = "black")
        pyautogui.click()
    #text.configure(text=rng.randint(0,100), fg ="white", bg = "black")
    #execute1()

root = tk.Tk()

root.title("Logo Counter")
root["bg"] = "black"

Draw()

bob = BindGlobal()
bob.start()
bob.gbind("<Shift-S>", Refresher)


root.mainloop()


