cipher = "MJMZKCXUNMGWIRYVCPUWMPRRWGMIOPMSNYSRYRAZPXMCDWPRYEYXD"
freq = {}
for c in ''.join(cipher):
    if c in freq.keys():
        freq[c] += 1
    else:
        freq[c] = 1
print sorted(freq.items(), key=lambda x: x[1])
def decode(C, c, d):
    return ''.join(chr( ( c*((ord(i)-ord('A')-d) )%26) + ord('A')) for i in C)
print decode(cipher, 3, 2)

