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
        time.sleep(0.1)

        if ser.in_waiting > 0:
            data=ser.readline().decode('utf-16').rstrip()       #This reads the data from ser and decodes it via using utf-16 format and strips the extra space of empty line at last
            print(f"Data received : {data}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed.")