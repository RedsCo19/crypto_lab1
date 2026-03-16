from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

data = b"This is a top secret."
ciph = "c34c12baffcb609d5b63da20d2cbf058c8e26f3903ab070b99f18d6fbcdfcd19"
known_iv = bytes.fromhex('00000000000000000000000000000000')

counter = 0
with open("Lab1/words.txt", "r") as f:
    for line in f:
        word = line.strip()
        if(len(word) >= 16): continue
        for i in range(len(word), 16):
            word += ' '
        key = word.encode()
        
        cipher = AES.new(key, AES.MODE_CBC, iv=known_iv)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        ct = ct_bytes.hex()

        if ct == ciph: 
            print(f"Found key: {word}")
            break