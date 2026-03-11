import time
import serial

#definig the port connection and opening
ser=serial.Serial(
    port='',
    baudrate=9600,
    timeout=1
)

try:
    if ser.is_open:
        print(f"Connected to {ser.port}")
        ser.write(b'Hello')
        print("Data sent: Hello")
        open('data_sent.txt', 'w').write('Hello')               #This writes the data into data_sent.txt file
        time.sleep(0.1)

        if ser.in_waiting > 0:
            data=ser.readline().decode('utf-16').rstrip()       #This reads the data from ser and decodes it via using utf-16 format and strips the extra space of empty line at last
            print(f"Data received : {data}")
            open('data_recieved.txt', 'w').write(data)     #This writes the data into data_recieved.txt file
except Exception as e:
    print(f"Error: {e}")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed.")