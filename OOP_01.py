class Car:
    colar = None
    def __init__(self,Car_type):
        print("Car :",Car_type)
        self.__speed = 0
    def Colar(self,colar):
        self.colar = colar
        print(self.colar)
    def SetSpeed(self,newspeed):
        if newspeed > 100 or newspeed < 0:
            print('speed out of range!! ')
        else:
            self.__speed = newspeed
    def get_speed(self):
        print(self.__speed)
    def boost(self,add_speed):
        self.__speed = self.__speed + add_speed
        print('boost.....now speed is: ',self.__speed)
    def step_break(self,sub_speed):
        self.__speed = self.__speed - sub_speed
        print('step break.....now speed is: ',self.__speed) 

A = Car(1)
A.Colar('Green')
A.SetSpeed(60)
A.get_speed()
