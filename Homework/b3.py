import re
ciphertext = '05041874034705152088235607360468'
def decode(C, d, n):
    output = ""
    for c_i in re.findall('..?.?.?', C):
        c_i = str((int(c_i)**d)%n).zfill(4)
        output += chr(int(c_i[:2])+ord('a'))
        output += chr(int(c_i[2:])+ord('a'))
    return output
print decode(ciphertext, 1109, 2881)


