try:
    a=int(input())
    b=int(input())
    c=a/b
    print("c")
except Exception as e:
    print(e)
except IOError:
    PRINT("IOError")
else:
    print("printing from else block")

