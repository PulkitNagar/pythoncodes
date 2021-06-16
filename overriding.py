class Employee:
    def __init__(self):
        self.first=input("enter name")
        self.last=input("enter last")
        self.empid=input("enter empid")
        self.pay=int(input("pay"))
        self.display()
    
    def display(self):
        print(self.first)
        print(self.last)
        print(self.empid)

class Developer(Employee):
    def __init__(self):
        super().__init__()
        self.apply_raise()

    def apply_raise(self):
        amt=1.5
        self.netsal=self.pay*amt
        self.display()
    
    def display(self):
        super().display()
        