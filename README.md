# durote
controllo dei motori di una macchinina attraverso il componente L298N e una Adafruit HUZZAH32. Il linguaggio utilizzato è micropython

collegamenti tra HUZZAH32 e L298N

HUZZAH32 | L298N
------------ | -------------
GND | GND  
USB(pin)  | 5V (con jumper inserito)  
D5 | EnA  
D21 | EnB  
D18 | IN1
D19 | IN2
D16 | IN3
D17 | IN4


### link
https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/
https://github.com/blynkkk/lib-python/tree/master/examples/esp32
