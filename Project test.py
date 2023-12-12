import pyautogui
import pynput






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
    difLog = checker("How many different logos are there? ")  # user input
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
from pynput import keyboard
import threading

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='s')},
    {keyboard.Key.shift, keyboard.KeyCode(char='S')}
]

current = set()
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

def execute2():
    #currentMouseX, currentMouseY = pyautogui.position()
    #pyautogui.click(currentMouseX, currentMouseY) #this will click and move the mouse
    #print(currentMouseX, currentMouseY)'
    testtk()
   
    
    
    #1205 926
    

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute1()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        

# Create a separate thread for the listener
listenerThread = threading.Thread(target=start_listener)
listenerThread.start()
#listenerThread.join() # figure out what this is? nvm this is the reason why u can't ()











