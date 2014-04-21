cipher = "KYVMR", "CLVFW", "KYVBV", "PZJJV", "MVEKV", "VE"
freq = {}
for c in ''.join(cipher):
    if c in freq.keys():
        freq[c] += 1
    else:
        freq[c] = 1
print freq
def rot(w, i):
    return ''.join(chr(((ord(c)-ord('A')+i)%26) + ord('A')) for c in w)
for i in xrange(26):
    print ' '.join(rot(w, i) for w in cipher)
