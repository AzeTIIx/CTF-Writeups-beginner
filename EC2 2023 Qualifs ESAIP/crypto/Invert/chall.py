
#on remarque que c'est un chiffrement XOR on peut l'inverser facilement en faisant un xor entre le texte chiffré et la clé (à savoir ord("o"))
def encrypt(input):
    out = ''.join(chr(c ^ ord("o")) for c in input)
    return out[::-1]

#on fait l'inverse du chiffrement
def decrypt(cypher):
    out = ''.join(chr(i ^ ord("o")) for i in cypher)
    return out[::-1]


if __name__ == '__main__':

    my_str_1 = r'C:\Users\charl\Desktop\CTF\EC2 qualifs esaip 2022\crypto\test.txt'

    my_str_2 = r'C:\Users\charl\Desktop\CTF\EC2 qualifs esaip 2022\crypto\flag.enc'


    with open(my_str_1,"rb") as file:
        content = file.read()

    flag_enc = encrypt(content)

    with open("flag_enc","w") as file:
        file.write(flag_enc)


    with open(my_str_2,"rb") as file:
            Todecrypt = file.read()

    flag_dec = decrypt(Todecrypt)

    with open(my_str_1,"w") as file:
        file.write(flag_dec)
