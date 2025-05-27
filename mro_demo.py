class Device:
    def info(self):
        print("Device's info")

class Phone(Device):
    def info(self):
        print("Phone's info")

class Camera(Device):
    def info(self):
        print("Camera stats info")

class Smartphone(Phone, Camera):
     pass #prints the method of the first class it inherits from which is Phone because it doesn't have its own method
    # def info(self):
    #     print('Touchscreen info')

s = Smartphone()
s.info()  # Output: Phone info

# Checks Method resolution order
print(Smartphone.__mro__)
