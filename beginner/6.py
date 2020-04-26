import string
cipher="igxk{fmovhh_gsvb_ziv_nvzm}"

alphabet = string.ascii_lowercase
rev_alphabet = alphabet[::-1]

res = ""
for c in cipher:
    if c in alphabet:
        offset = ord(c) - 97
        res += rev_alphabet[offset]
    else:
        res += c

print(res)
