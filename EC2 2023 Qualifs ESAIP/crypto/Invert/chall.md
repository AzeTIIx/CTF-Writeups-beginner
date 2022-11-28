# Invert

## Ma solution

Voici le code d'origine
```python

def encrypt(input):
    out = ''.join(chr(c ^ ord("o")) for c in input)
    return out[::-1]


def decrypt(cypher):
    return


if __name__ == '__main__':


    with open(flag.txt,"rb") as file:
        content = file.read()

    flag_enc = encrypt(content)

    with open("flag_enc","w") as file:
        file.write(flag_enc)
```

Ce qui est pratique avec le chiffrement XOR, c'est qu'il suffit de faire un XOR entre le message chiffré et la clé pour trouver le texte en clair !

```
A = XOR(B, KEY)
B = XOR(A, KEY)
```

On implémente alors une solution simple :

```python

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
```

On obtient alors le flag dans notre fichier test.txt : 
``
EC2{Ez_CrYpt0_MaD3_IN_Es4iP}
``



