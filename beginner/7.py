import binascii

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

bintext = "00110 01110 00100 00000 10011 00101 01110 01110 00011 00011 01110 01101 10011 10010 10011 00000 10001 10101 00100".split()
message = ""

k=0
dec=0
new=[]
item = bintext
for i in item:
    for j in reversed(i):
        if(j=="1"):
            dec=2**k+dec
            k=k+1
        else:
            k=k+1
    new.append(dec)
    dec=0
    k=0
for i in new:
    print(chr(i + 97),end="")
print()

# for x in bintext:
    # print(bits2string(x))
