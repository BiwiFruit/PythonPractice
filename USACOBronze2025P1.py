def rounding(num, p):
    x = str(num)[-p]
    if int(x) >= 5:
        num += 10**p
        num -= int(str(num)[-p:])
        return num
    else:
        num -= int(str(num)[-p:])
        return num

def bessie_rounding(num):
    if str(num)[0] >= 5:
        num *= 0
        num += 10**len(num)
    else:
        num *= 0 
    return num

def chain_rounding(num, p):
    i = 1
    while i <= p:
        num = rounding(num, i)
        i += 1
    return num

def compare(end):
    i = 2
    count = 0
    while i <= int(end):
        for n in range(1, len(str(i))):
            if str(i)[:n] == "4" * (n) and int(str(i)[n]) >= 5:
                count += 1
                break
        i += 1
    return count

def main():
    initial = input()
    inputs = []
    for i in range(int(initial)):
        inputs.append(input())
    for i in inputs:
        print(compare(i))

main()