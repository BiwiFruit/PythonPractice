def compare(end):
    i = 2
    count = 0
    while i <= int(end):
        if str(i)[0] == "4":
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