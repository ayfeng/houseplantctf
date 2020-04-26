import string
cipher="egpc{lnyy_orggre_cnegvpvcngr}"

for i in range(1, 80):
    res = ""
    for j,c in enumerate(cipher):
        if c != '{' and c != '}':
            tmp = chr(((ord(c) - i) % 26)+97)
            print("{} became {}, i={}, j={}".format(c,tmp,i,j))

            if (tmp.lower() != 'r' and j == 0): # if we don't see rtcp
                res = ""
                break
            elif tmp in string.printable:
                res += tmp
        else:
            res += c

        if len(res) > 0:
            print(res, "| i =", i)

