def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
    
def encrypt(string, key):
    ciphertext = []
    for i in range(len(string)):
        x = 97 + ((ord(string[i]) - 97) + (ord(key[i]) - 97))%26
        ciphertext.append(chr(x))
    return "".join(ciphertext)
     
def decrypt(ciphertext, key):
    plain = []
    for i in range(len(ciphertext)):
        x = 97 + ((ord(ciphertext[i]) - 97) - (ord(key[i]) - 97))%26
        plain.append(chr(x))
    return "".join(plain)