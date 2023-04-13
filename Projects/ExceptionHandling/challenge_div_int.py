def intdiv(n1: int, n2: int):
    """Divides n1 by n2 and handles div/0 exception"""
    try:
        return n1/n2
    except ZeroDivisionError:
        n2 = int(input("You can't divide by zero, select a new number for the divisor: "))
        return n1/n2
    except TypeError:
        print("Inputs need to be in integer format. Converting to integers.")
        n1 = int(n1)
        n2 = int(n2)
        return n1/n2

mode = 1 # 0 = quit | 1 = run
if __name__ == "__main__":
    #print("*" * 60)
    print("Starting integer division program.")
    while True:
        print("*" * 60)
        n1 = int(input("Select dividend (n1): "))
        n2 = int(input("Select divisor (n2): "))
        result = intdiv(n1, n2)
        print("Result: ", result)
        print("*" * 60)
        mode = input("Select option:\n(1) Continue\n(0) Quit\n: ")
    
        if mode == str(0):
            break

        

        