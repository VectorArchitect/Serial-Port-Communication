import streamlit as st
from crc import append_crc, verify_packet
import time
import os


###############################################################################################################################
container=st.container()  # Create a container to hold the content
try:
    st.set_page_config(page_title="AP4C communication", layout="wide")
    st.write("### Server Connected")
    # st.text("Send Request to check data")
    # if st.button("Send Request"):

    #     status='y'
    #     # def clear_screen():
    #     #     # Windows ke liye 'cls', Mac/Linux ke liye 'clear'
    #     #     os.system('clear' if os.name == 'nt' else 'clear')
    #     i=0
    #     if status=='y':

    data_spot = st.empty()
    if 'i' not in st.session_state:
        st.session_state.i = 0   
    @st.fragment(run_every=5)    
    def func():
        st.write(st.session_state.i)
        st.session_state.i += 1
        with data_spot.container():     
            data=[161, 3, 00, 15, 0, 15]

            packet=append_crc(data) #adding crc to data

            #bytes_sent=ser.write(packet)   #sending bytes packet and storing no. of bytes in bytes_sent
            print(f"Sent: {packet}")
            print(packet)
            # print(f"sent: {packet.hex(' ')}")
            # print(f"Total bytes written: {data}")

            time.sleep(0.5)  # even if data not received the program will not shut for this amount of time

            #line = ser.read(90)

            #line = ser.readline(35).rstrip()
            line=(161, 3, 30, 0, 0,3,4,234,4,435,6,675,445,23,3,2,43,4,23,67,2,5,8,23,5,8,0,2,2,5,7,223,45,6,89)
            line_length = len(line)

            print(line_length)
            for w in line:
                print(f"{w:02x}")
                print(f"{w:016b}")
            print(line)

            var = ['res_0', 'res_1', 'CH_con', 'As_con', 'CN_con', 'Ph_con', 'Sol_con', 'Alarm', 'Status']
            byte_array = line  # decimal array of 35 inputs
            byte = byte_array[3:33]
            print(byte)
            
            col1, col2, col3, col4=st.columns(4,gap='large',border=True)
            with col1:  ########33333333333333333################
            #     col1_content = st.empty()
            #     with col1_content.container():
                j = 0
                for i in range(0, 4, 2):
                    sum = (byte[i] * 256) + byte[i + 1]
                    # print(sum)
                    # print(f"{sum:016b}")
                    vari = var[j]

                    print(f"{var[j]}: {sum}")
                    st.write(f"##### {vari} ")
                    st.info(f"{sum}") #{sum: 04b}

                j += 1
                # time.sleep(5)
                # col1_content.empty()  
                j = 0

                print("----")
            
            with col2:  ########33333333333333333################
            #     col2_content = st.empty()
            #     with col2_content.container():
                j = 2
                for i in range(4, 13, 2):
                    sum = (byte[i] * 256) + byte[i + 1]
                    # print(sum)
                    # print(f"{sum:016b}")
                    vari = var[j]

                    print(f"{var[j]}: {sum}")
                    st.write(f"##### {vari} ")
                    st.info(f"{sum}") #{sum: 04b}
                    j += 1
                # time.sleep(5)
                # col2_content.empty()  # Clear the content of col2 after 5 seconds

            # for alarm and status
            with col3:   ####33333333333333333333333###############
            #     # Alarm
            #     col3_content = st.empty()
            #     with col3_content.container():
                sum = (byte[14])
                vari = var[7]
                print(f"Alarm: {sum}")
                print(f"{sum:04b}")
                st.write(f"##### Alarm: {sum:04b}")
                #st.info(f"Alarm: {sum: 04b}")
                sixteen_bit = f"{sum:04b}"
                lenS = len(sixteen_bit)
                k = lenS
                for val in sixteen_bit:
                    k -= 1
                    if val == '1':
                        print(f'Alarm[{k}]: on')
                        #st.write(f'->Alarm[{k+1}]:  on')
                        st.success(f"Alarm[{k + 1}]: ON")
                    elif val == '0':
                        st.error(f"Alarm[{k + 1}]: OFF")
                    # time.sleep(5)
                    # col3_content.empty()

                print("----")
            
            with col4:   ####33333333333333333333333###############
            #     # Status
            #     col4_content = st.empty()
            #     with col4_content.container():
                sum = (byte[15])
                vari = var[8]
                print(f"Status: {sum}")
                print(f"{sum:04b}")
                st.write(f"##### Status: {sum:04b}")
                #st.info(f"Status: {sum: 04b}")
                sixteen_bit = f"{sum:04b}"
                lenS = len(sixteen_bit)
                k = lenS
                for val in sixteen_bit:
                    k -= 1
                    if val == '1':
                        print(f'Status[{k}]: on')
                        #st.write(f'->Status[{k+1}]: on')
                        st.success(f"Status[{k+1}]: ON")
                    elif val == '0':
                        st.error(f"Status[{k + 1}]: OFF")
                # time.sleep(5)
                # col4_content.empty()
                        
            st.write(f"#### Data received:")
            st.info(f"{line}")
            st.write(f"length of data: {line_length}")
            
            st.write(f"#### Usable Data: ")
            st.info(f"{byte}")
    
    # time.sleep(2)
    # data_spot.empty()
# while True:
    
    func()
    # time.sleep(5)
    # st.rerun()

    

            # if ser.in_waiting > 0:
            #     line = ser.readline().decode('utf-8').rstrip()
            #     print("Received : " + line)
            # elif status=='/exit':
            #
            #     break

except Exception as e:
    print(f"Error: {e}")

