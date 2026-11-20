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

if __name__ == "__main__":
    UnitConverter()
    print("10")