# Lecture 0
#f strings, string methods, input, named paramters, interactive mode, 
# multiple var assignement, functions, f string methods, main()
def tip_calc():
    cost = float(input("How much did the meal cost? ").replace('$', ''))
    percent = float(input("What percent would you like to tip? ").replace("%", ""))/100
    tip = round(percent * cost, 2)
    print(f"Your tip should be: ${tip}")

#Lecture 1 Conditionals
# match function, booleans (all compare have bollean value)
#x = int(input("Give me a number?"))
#y= int(input("What's y?"))

def compare():
    if x < y:
        print("Biwi")
    elif x >= y:
        print("RIIWIWWIIWI!")
    else:
        print("no")

def parity(a):
    return "Even" if a % 2 == 0 else "Odd"

def The_Question(a):
    cleaned = a.lower().strip()
    match cleaned:
        case "42":
            print("Yes")
        case "forty two":
            print("Yes")
        case "forty-two":
            print("Yes")
        case _:
            print("No")

def HelloCash(a):
    cleaned = a.strip().lower()
    if a == "hello":
        print("$100")
    elif a[0] == "h":
        print("$20")
    else:
        print("$0")

def FileFinder(a):
    dot = a.find(".")
    cleaned = a[dot:].strip().lower()
    match cleaned:
        case ".gif":
            return "image/gif"
        case ".jpg" | ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/txt"
        case ".zip":
            return "text.zip"
        case _:
            return "application/octet-stream"

def interpreter(a):
    list  = a.split(sep = " ")
    if list[1] == "/":
        return(f"{float(list[0])/float(list[2]): .1f}")
    elif list[1] == "+":
        return(f"{float(list[0])+float(list[2]): .1f}")
    elif list [1] == "-":
        return(f"{float(list[0])-float(list[2]): .1f}")
    else:
        return(f"{float(list[0])*float(list[2]): .1f}")
def main0():
    x = input('what time is it now? ')
    time =  convert(x)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(a):
    list = a.replace(":", " ").split()
    if list[2] == "am" or list[2] == "a.m.":
        number = float(list[0]) + float(list[1])/60
        return number
    elif list[2] == "pm" or list[2] == "p.m.":
        number = float(list[0]) + float(list[1])/60
        return number + 12

def BillSplitter():
    print(f"Total: {total}")
    print(f"People: {people}")
    print(f"Each person pays: {float(total)/float(people)}")

def UnitConverter():
    option = input("Convert what? (1) unit into miles (2) C to F ")
    if int(option) == 1:
        kmdistance = input("Input distance in km: ")
        print(f"{kmdistance} km = {float(kmdistance)*0.621: .2f} miles")
    elif int(option)== 2:
        celsius = input("Input degrees celsius: ")
        print(f"{celsius} C = {float(celsius) * 9 /5 + 32: .2f} F")
    else:
        print("Invalid choice")

#Lecture 2
# while loops, for loops, list
# _ notaiton for i in range when vairbale not important
# print("meow\n" * 3, end = "")
# infinite loops, condition while
# len()
# None varibale type, dictionaries, lists of dictionaries
#while True:
    #n = int(input("What's n? "))
   # if n > 0: break

#for _ in range(n):
    #print("meow")

students = ["Herminone", "Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", " Slytherin"]

def print_square(size):
    for i in range(size):
        print("#"*size)

def camel_to_snake_case(input):
    snake = ""
    for letter in input:
        if letter.isupper() == True:
            snake += "_" 
            snake += letter.lower()
        else:
            snake += letter
    print(snake)
  
def cokemachine():
    inside = 50
    while inside > 0:
        print("Amount Due:", inside, sep = " ")
        value = int(input("Insert Coin: "))
        if value in [5, 25, 10]:
            inside -= value
    print("Change Owed: ", inside*-1)

def vowelremover():
    insert = input("Input: ")
    outsert = ""
    for char in insert:
        if char.lower() in ["a", "e", "i", "o",'u']:
            continue
        else:
            outsert += char
    print(outsert)

def plates():
    plate  = input("Plate: ")
    if len(plate) > 6 or len(plate) < 2:
        print("Invalid")
        return False
    elif not plate[0].isalpha() or not plate[1].isalpha():
        print("Invalid")
        return False
    num = 0
    alpha = 0
    for i in range(len(plate)):
        if plate[i].isdigit():
             if num == 0 and plate[i] == "0":
                print("Invalid")
                return False
             else: 
                 num = i
        elif plate[i].isalpha():
             alpha = i
        else:
            print("Invalid")
            return False
    if num < alpha and num > 0:
        print("Invalid")
        return False
    print("Valid")

def nutrition():
    fruits = {"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90, "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15, "Lime": 20, "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100, "Pineapple": 50, "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100, "Tangerine": 50, "Watermelon": 80}
    item = input("Item: ").title()
    if item in fruits:
        print("Calories:", fruits[item])

