import time
import os.path
import sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
def z1():
    print_slow("Znak 1:")
    print()
    print_slow("Przysięgliśmy sobie wierność w samym środku bijatyki w pewnej karczmie. Cuchnęło tam rzygowinami, potem, krwią. Było taaak romantycznie...")
    clear()
def z2():
    print_slow("Znak 2:")
    print()
    print_slow("2+2*2 dla nieuków")
    clear()
def z3():
    print_slow("Znak 3:")
    print()
    print_slow("Żona syna Menojka")
    clear()
def z4():
    print_slow("Znak 4:")
    print()
    print_slow("Duża, dwunożna istota, podobna do człowieka, o gęstym futrze, żyjąca rzekomo w Himalajach")
    clear()
def z5():
    print_slow("Znak 5:")
    print()
    print_slow("...")
    clear()
def ze():
    print_slow("Przejscie do kolejnej zagadki:")
    print()
    names = next(os.walk("."), (None, None, []))[2]
    print_slow("Oblicz, ile jest wszystkich siedmiocyfrowych liczb naturalnych, w których zapisie dziesiętnym\nwystępują dokładnie trzy cyfry 1 i dokładnie dwie cyfry 2. ")
    print_slow("Wpisz odpowiedź:")
    x = input()
    if(x==names[0]):
        f = open(names[2], "r")
        print(f.read())
    else:
        print("Nope.")
    clear()
def logo():
    print_slow("Are you ready for adventure?")
    time.sleep(0.5)
    print()
    print_slow("      .~~~~`\\~~\\")
    print()
    print_slow("     ;       ~~ \\")
    print()
    print_slow("     |           ;")
    print()
    print_slow(" ,--------,______|---.")
    print()
    print_slow("/          \\-----`    \\")
    print()    
    print_slow("`.__________`-_______-'")
    print()
    clear()
def clear():
    time.sleep(3)
    clear = lambda: os.system('cls')
    clear()
if __name__ == "__main__":
    logo()
    z1()
    z2()
    z3()
    z4()
    z5()
    ze()
