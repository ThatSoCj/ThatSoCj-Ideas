import pyautogui
import pynput

def test():
    print(pyautogui.size())
    for i in range(2): # Move mouse in a square.
        pyautogui.moveTo(1400, 890, duration=0.25)
    #2560 × 1664)


def test2():
    x = 15
    pyautogui.alert(f"you need {x}")



def calculation():
    oneLogo = int(input("How many logos are there?"))
    goal = int(input("How much you need to make?"))
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
            

def logosDictionary():
    d = {} # logos and amount
    L = [] #goal
    A =[] # how many for goal
    logo = []
    difLog = checker("How many different logos are there? ")  # user input
    if difLog > 0:
        for i in range(1, difLog + 1):
            logos = checker(f"How many logos are there for logo {i}? ")# user input
            d[i] = logos # add things to dictionary
            print(d)
            answer = checker("goal?") # user input
            L.append(int(answer)) # add things to list
            print(L)
            print(L[i -1:])
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
            print(f"logo({i}) you need {answer} sheets")
            A.append(float(math))
        elif 0 <remainder< 5:
            print(f"logo({i}) you need {answer} and less then an half of sheet")
            A.append(float(math))
        elif remainder == 5:
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
    for i in L:
        for z in d:
            if d[z] < i:
                print("hi")
            else:
                print("no")





def start1():
    #d = {}  logos and amount
    #L = [] goal
    #A =[]  how many for goal
    d,L,A = logosDictionary()
    amount = 0
    print(d,L,A)
    for i in d:
        amount = d[i]
        print(amount)





        
        
      

    

    
    
def math():
    difLog = int(input("what is it"))
    A = int(input("what is it"))
    if difLog > 0 and A > 0:
        return [difLog, A]

def test():
    math()
    difLog = math([0])
    A = math([1])

#logosDictionary()

