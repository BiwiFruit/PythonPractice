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
def main():
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
main()