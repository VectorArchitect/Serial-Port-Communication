x=19

eight_bit=f"{x:08b}"
lenE=len(eight_bit)

print(eight_bit)

i=lenE

for val in eight_bit:
    i-=1
    if val == '1':
        print(f'eight_bit[{i}]: on')
    # else:
    #     print(f"{val}: off")

print("------------")

sixteen_bit=f"{x:016b}"
def alarm(sixteen_bit):
    lenS=len(sixteen_bit)
    print(sixteen_bit)
    j=lenS
    for val in sixteen_bit:
        j-=1
        if val == '1':
            print(f'sixteen_bit[{j}]: on')
        # else:
        #     print(f"{val}: off")

