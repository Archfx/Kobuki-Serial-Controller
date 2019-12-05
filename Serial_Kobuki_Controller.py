import serial

##Kobuki Robot platform Python driver
##Protocol information available at : http://yujinrobot.github.io/kobuki/enAppendixProtocolSpecification.html
##<aruna.15@cse.mrt.ac.lk>

speed_1,speed_2 = 255,255
radius_1,radius_2 = 0,0
ser = serial.Serial('COM15', 115200, timeout=0,parity=serial.PARITY_EVEN, rtscts=1)
header1=0xAA
header2=0x55
#send=[header1, header2,3,4,1,4]  #Sound play
send=[header1, header2,0x5,0x1,0x4,speed_1,speed_2,radius_1,radius_2] # Motion Control
checksum=0

for x in range(len(send)-2):
    checksum=checksum^send[x+2]
    
send.append(checksum)
values = bytearray(send)
ser.write(values)
s = ser.read(7)
print (values)
print (s)
