from simplecrypt import *
with open('enc.bin', 'rb') as i:
    encrypted = i.read()
with open('pass.txt', 'r') as pa:
    passes = pa.read().strip().split('\n')
for p in passes:
    print(p)
    try:
        a = decrypt(p, encrypted)
    except DecryptionException:
        pass
print(a)
pass