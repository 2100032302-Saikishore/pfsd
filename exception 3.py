try:
    klu1=open("file.txt","r+")
    try:
        klu1.write("xyz this is s17 section")
    finally:
        klu1.close()
except IOError:
    print("file not found")
else:
    print("this file opened successfully")
    klu1.close()