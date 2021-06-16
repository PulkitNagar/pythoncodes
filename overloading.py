class person:
    def call(self,name = "none" ,age = 0):
        if (name is not "none" and age != 0):
            print("hellow "+name)
            print("my age is ",age)
        elif(name is not "none" and age == 0):
            print("hellow "+name)
        else:
            print("hellow")

ob=person()
ob.call("ansh")