# break my db

## Ma solution

Ici, le but est de cracker la master key d'une base de données KeePass.

Dans un premier temps, on génère un hash de notre bash à l'aide de John the Ripper : 

``
keepass2john Databse.kdbx > test.txt.
``

Ensuite, on lance un bruteforce de ce hash avec hashcat en utilisant la wordlist rockyou.txt : 

![](./images/1.png)

On récupère alors la master key pour se connecter à la base, ici c'est motherandchild : 

![](./images/2.png)

Enfin on peut accéder à notre base et récupérer le flag : 

![](./images/3.png)

Flag: `EC2{K3ep4ss_Sucks_with_W3eak_P4ss}
`
