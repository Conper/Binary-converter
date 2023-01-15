
import time

final_list = []
result_list = []
out = []

# --------------- The beginning --------------- #
def begin():
    print(" ")
    print("1.Decimal to Binary          2.Binary to Decimal")
    print(" ")
    option = input("Option: ")

    if option == "1":
        to_binary()

    elif option == "2":
        to_number()

    else:
        print(" ")
        print("Sorry, that option doesn't exist")
        print(" ")
        time.sleep(1)
        begin()


# --------------- Decimal to Binary function --------------- #
def to_binary():
    final_list.clear()
    n = 0
    x = input("Decimal number: ")
    len_x = len(x)
    for n in range(len_x):
        if (x[n] == '0') or (x[n] == '1') or (x[n] == '2') or (x[n] == '3') or (x[n] == '4') or (x[n] == '5') or (x[n] == '6') or (x[n] == '7') or (x[n] == '8') or (x[n] == '9'):
            pass

        else:
            print(" ")
            print("Sorry, it's not a decimal number")
            print(" ")
            begin()
    x = int(x)
    while x > 0:
        y = x % 2
        x = x // 2

        final_list.insert(0, y)

    print(" ")
    print("--------- The result is: " + str(final_list) + " ---------")
    time.sleep(1.5)
    print(" ")
    print(" ")
    begin()


# --------------- Binary to Decimal function --------------- #
def to_number():
    result = 0
    final_list.clear()
    result_list.clear()

    i, r, w, n = 0,0,0,0

    x = input("Binary number: ")
    len_x = len(x)
    for n in range(len_x):
        if (x[n] == '1') or (x[n] == '0'):
            pass

        else:
            print(" ")
            print("Sorry, it's not a binary number")
            print(" ")
            begin()

    while i < len_x:
        final_list.insert(0, x[i])
        i += 1

    if len(final_list) == 0:
        if final_list[0] == '1':
            result = 1

        elif final_list[0] == '0':
            result = 0

    else:
        for r in range(len_x):
            if final_list[r] == '1':
                a = 0
                w = 2**r
                result_list.append(w)
                len_x = len(result_list)
                for u in range(len_x):
                    result = a + result_list[u]
                    a = result_list[u]
                
            else:
                pass
                

    print(" ")
    print("--------- The result is: " + str(result) +" ---------")
    time.sleep(1.5)
    print(" ")
    print(" ")
    begin()






begin()