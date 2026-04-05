import time
import serial
from crc import append_crc

#defining the port connection and opening it
ser = serial.Serial(
    port ='COM7',         #port name
    baudrate = 115200,      #rate of communication or sending data (bits/sec)
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout = 1           #wait time for reading
)
try:
    if ser.is_open:
        print("Connected to " + ser.port)
        #print("marco".encode('utf-8'))
    while True:
        status=input("Send request?(y/n) '/exit': ").lower()
        if status=='y':
            #data = input("Enter hex values (space seperated): ").split()
            data=[161, 3, 00, 15, 0, 15]

            #print(data)
            #data = [int(x, 16) for x in data]
            #raw_payloads=bytes(data)  #converting data to bytes

            packet=append_crc(data) #adding crc to data

            bytes_sent=ser.write(packet)   #sending bytes packet and storing no. of bytes in bytes_sent
            print(f"Sent: {packet}")
            print(packet)
            print(f"sent: {packet.hex(' ')}")
            open('data_sent.txt', 'w').write('Hello')
            print(f"Total bytes written: {bytes_sent}")

            time.sleep(0.5)  # even if data not received the program will not shut for this amount of time

            #line = ser.read(90)  

            line = ser.readline(35).decode('utf-8').rstrip() #will read upto 35 values of input
            line_length = len(line)

            print(line_length)
            for w in line:
                print(f"{w:02x}")
                print(f"{w:016b}")
            print(line)

            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                open('data_recieved.txt', 'w').write(data)
                print("Received : " + line)
        elif status=='/exit':

            break

except Exception as e:
    print(f"Erorr: {e}")
