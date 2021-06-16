class person:
    def call(self,name = "none" ,age = "none"):
        if (name is not "none" and age is not "none"):
            print("hellow"+name+"age is "+age)
        elif(name is not "none" and age is "none"):
            print("hellow"+name)