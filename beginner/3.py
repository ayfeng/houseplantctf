import numpy
import codecs
s="162 164 143 160 173 163 165 145 137 155 145 137 151 137 144 151 144 156 164 137 153 156 157 167 137 167 150 141 164 137 157 143 164 141 154 137 167 141 163 137 157 153 141 171 77 41 175".split()

h="723a18ce07b399d4ca5f36994be692f990d264371d0be6b371bcee5f3b9a0c2742f9bcc674309b0be77309ccbe6f35984f3fc27d"

def converter(number, base):
    #split number in figures
    figures = [int(i,base) for i in str(number)]
    #invert oder of figures (lowest count first)
    figures = figures[::-1]
    result = 0
    #loop over all figures
    for i in range(len(figures)):
        #add the contirbution of the i-th figure
        result += figures[i]*base**i
    return result

for c in s:
    print(chr(converter(c, 8)), end="")
print()
