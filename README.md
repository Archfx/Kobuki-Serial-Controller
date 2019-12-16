# Kobuki-Serial-Controller
Serial raw python implementation for controlling Kobuki Robot base




# Overview

The  [kobuki driver](http://yujinrobot.github.io/kobuki/classkobuki_1_1Kobuki.html)  communicates with the robot by using predefined protocol. In general, the driver sends the commands to the robot and the robot sends some feedback data or sensor readings. These commands and feedback data are converted into bytestreams for communication via serial interface. The protocol specifies that rules and forms of bytestreams.

# Structure of Bytestream

A bytestream can be divided into 4 fields; Headers, Length, Payload and Checksum.

Name | Header 0 | Header 1 | Length | Payload | Checksum
|--|--|--|--|--|--|
Size | 1 Byte | 1 Byte | 1 Byte | N Bytes | 1 Byte
Description | 0xAA (Fixed) | 0x55 (Fixed) | Size of payload in bytes | Described below | XOR'ed value of every bytes of bytesream except headers



Name | Header 0 | Header 1 | Length | Payload | Checksum
Size | 1 Byte | 1 Byte | 1 Byte | N Bytes | 1 Byte
Description | 0xAA (Fixed) | 0x55 (Fixed) | Size of payload in bytes | Described below | XOR'ed value of every bytes of bytesream except headers
