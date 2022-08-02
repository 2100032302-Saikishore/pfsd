while True:
    try:
        n=int(input("Please enter any integer: "))
        break
    except IOError:
        print("not an integer")
    except ValueError:
        print("not an integer error")
print("n")




