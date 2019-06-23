from machine import Pin,PWM

#p1 = Pin(18, Pin.OUT)
#p2 = Pin(19, Pin.OUT)
#p3 = Pin(16, Pin.OUT)
#p4 = Pin(17, Pin.OUT)
#enA = PWM(Pin(5), freq=5000, duty=0)
#enB = PWM(Pin(21), freq=5000, duty=0)
#enA = PWM(Pin(5))
#enB = PWM(Pin(21))

class Durote():
    def __init__(self,pin1=18,pin2=19,pin3=16,pin4=17,pinA=5,pinB=21):
        self.p1 = Pin(pin1, Pin.OUT)
        self.p2 = Pin(pin2, Pin.OUT)
        self.p3 = Pin(pin3, Pin.OUT)
        self.p4 = Pin(pin4, Pin.OUT)
        self.enA = PWM(Pin(pinA))
        self.enB = PWM(Pin(pinB))
    
    def _cmd(self,p1,p2,p3,p4,enA=0,enB=0):
        self.p1.value(p1)
        self.p2.value(p2)
        self.p3.value(p3)
        self.p4.value(p4)
        self.p1.value(p1)
        self.enA.duty(enA)
        self.enB.duty(enB)

    def stop(self):
        self._cmd(0,0,0,0,0,0)
    
    def avanti(self,speed=512):
        self._cmd(0,1,0,1,speed,speed)

    def indietro(self,speed=512):
        self._cmd(1,0,1,0,speed,speed)
    
    def destra_avanti(self,speed=512):
        self._cmd(0,1,0,0,speed,0)
                
    def sinistra_avanti(self,speed=512):
        self._cmd(0,0,0,1,0,speed)

    def destra_indietro(self,speed=512):
        self._cmd(0,0,1,0,0,speed)
                
    def sinistra_indietro(self,speed=512):
        self._cmd(1,0,0,0,speed,0)
