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

## Header

Two bytes of headers, header 0 and header 1, are fixed value for both bytestreams, commands and feedback data. This headers are used to detect the starting point of bytestream.

  

## Length

Length indicates the length of following bytes that single bytestream hold. Default size of this field is 1 byte. Length can be used to distinguish each bytestreams. Minimum value of this field is 3.

  

## Payload

Payload contains actual data of bytestream.

  

### Structure Of Payload

Payload is a consist of several sub-payloads.

 | Pa | yl | oa | d | | 
|--|--|--|--|--|
Sub-Payload 0 | Sub-Payload 1 | Sub-Payload 2 | ... | Sub-Payload N-1

  

### Structure Of Sub-Payloads

Sub-payload can be divided into three parts; Header, Length and Data.
| Name | Header | Length | Data | 
|--|--|--|--|
Size | 1 Byte | 1 Byte | N Byte(s)
Description | Predefined Identifier | Size of data in byte(s) | Described below

  

## Checksum

Checksum is XOR'ed value of entire bytestream except headers. Checksum process ensure the integrity of bytestreams.
