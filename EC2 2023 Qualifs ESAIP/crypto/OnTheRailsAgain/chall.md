# On the Rails Again


## Ma solution

On nous fournit un fichier flag.enc qui contient la string : BLSIREEAEUSLINSREPVEADEUISNL

Entre l'allure de la string et le nom du challenge on déduit que c'est un rail fence cipher, on passe alors sur dcode : https://www.dcode.fr/rail-fence-cipher

Qui nous produit le résultat suivant : BIENVENUESURLESRAILSDELESAIP

On passe la string en minscule : 

```python

a = "BIENVENUESURLESRAILSDELESAIP"

b = a.lower()

print(b)

```

Et on peut flag : 

``
EC2{bienvenuesurlesrailsdelesaip}
``
