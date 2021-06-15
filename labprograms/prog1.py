while True:
    print("1-STRING 2-TUPLE 0-EXIT")
    choice=int(input("ENTER CHOICE OF STRING AND TUPLE"))
    if (choice==1):
        print("1-to reverse a string \n 2-to count the numbers of characters \n 3-to convert to lower case \n  4- to print to upper case \n 5-to lower case \n 6-to concatenate two strings \n 7-print max \n 8-print minimum \n9-find a character \n 10-extract last character")
        strchoice=int(input("ENTER CHOICE"))
        if(choice==1):
            str=input("enter a string")
            print(str[::-1])
        elif(choice==2):
            str=input("entr a string")
            print(len(str))
        elif(choice==3):
            pass
    elif(choice==2):
        pass
    elif(choice==0):
        break
    else:
        print("wrong choice entered")
        break