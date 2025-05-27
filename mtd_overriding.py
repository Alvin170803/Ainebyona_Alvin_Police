#simple real-world example of method overloading
class Parent:
    def study(self):
        print("Studied only in his home district.")

class Son(Parent):
    def study(self):
        print("The son is now studying overseas beyond his home.")

# created objects
p= Parent()
p.study() 

s = Son()
s.study()  
