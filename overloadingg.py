while True:
    choice=int(input("Enter you choice for \n 1 - Integers \n 2 - Lists \n 0 - exit \n"))
    if (choice==1):
        def int_operations(a=-999,b=-999,c=-999):
            if(a==-999 and b==-999 and c==-999):
                print("no input parameter found hence no operation")
            elif(a!=-999 and b!=-999 and c==-999):
                ch=int(input("two parameters found enter your choice 1-ADD 2-MULTIPLY \n"))
                if(ch==1):
                    print(a+b)
                elif(ch==2):
                    print(a*b)
                else:
                    print("wrong choice entered")
            elif(a!=-999 and b!=-999 and c!=-999):
                ch=int(input("three parameters found enter your choice 1-ADD 2-MULTIPLY\n"))
                if(ch==1):
                    print(a+b+c)
                elif(ch==2):
                    print(a*b*c)
                else:
                    print("wrong choice entered")
        int_operations(10,10)#for 2 inputs same function
        int_operations(10,10,10)#for 3 inputs same function
        int_operations()#same function without inputs
    elif(choice==2):
        print("WELCOME TO LIST OVERLOAD")
        def listoverload(a=[],b=[]):
            if(len(a)==0 and len(b)==0):
                print("Either no Parameters passed or no values in list")
            elif(len(a)!=0 and len(b)==0):
                print("Only got 1 parameter or second parameter passed is empty")
                ans=[]
                for i in range(len(a)):
                    ans.append(a[i] + a[i])
                print(ans)
            elif(len(a)!=0 and len(b)!=0):
                print("found 2 parameters")
                if(len(a)!=len(b)):
                    print("length of lists dont match so no operation allowed")
                else:
                    ch=int(input("enter your choice 1- adding two lists \n 2-multiplying 2 lists \n"))
                    ans1=[]
                    if(ch==1):
                        for i in range(len(a)):
                            ans1.append(a[i] + b[i])
                        print(ans1)
                    elif(ch==2):
                        for i in range(len(a)):
                            ans1.append(a[i] * b[i])
                        print(ans1)
                    else:
                        print("wrong choice entered")
            else:
                print("wrong type parameter called")

        a=[1,2,3,4,5,6]
        b=[1,2,3,4,5,6]
        listoverload()#calling the function without parameters
        listoverload(a)#calling the function with just 1 parameter
        listoverload(a,b)#calling the function with 3 parameters
    elif(choice==0):
        print("program ends")
        break
    else:
        print("wrong choice entered")
