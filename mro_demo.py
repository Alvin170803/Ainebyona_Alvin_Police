class Device:
    def info(self):
        print("Device info")

class Phone(Device):
    def info(self):
        print("Phone info")

class Camera(Device):
    def info(self):
        print("Camera info")

class Smartphone(Phone, Camera):
    # pass
    def info(self):
        print('Touchscreen info')

# Demo
s = Smartphone()
s.info()  # Output: Phone info

# Check MRO
print(Smartphone.__mro__)
