# pas un bon nom

> Le coffre-fort secret ne semble pas déchiffrer correctement. Corrigez-le pour obtenir des points. Il y a peut-être d'autres problèmes, qui sait !

## Ma solution

Voici le code d'origine
```golang
package main

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"os"
	"strings"
)

var bytes = []byte{53, 22, 66, 29, 75, 43, 14, 95, 34, 65, 82, 10, 23, 33, 17, 50}

const MySecret string = "\nsecret=Something_AbCdEfGhIjKlM\n"

func Encode(b []byte) string {
	return base64.StdEncoding.EncodeToString(b)
}

func Decode(s string) []byte {
	data, err := base64.StdEncoding.DecodeString(s)
	if err == nil {
		panic(err)
	}
	return data
}

// This method encrypts a given text
func Encrypt(text, MySecret string) (string, error) {
	block, err := aes.NewCipher([]byte(MySecret))
	if err != nil {
		return "", err
	}
	plainText := []byte(text)
	cfb := cipher.NewCFBEncrypter(block, bytes)
	cipherText := make([]byte, len(plainText))
	cfb.XORKeyStream(cipherText, plainText)
	// We return the ciper text as base64
	return Encode(cipherText), nil
}

// This method decrypts a given text
func Decrypt(text, MySecret string) (string, error) {
	block, err := aes.NewCipher([]byte(MySecret))
	if err != nil {
		return "", err
	}
	// We first decode the base64 input text
	cipherText := Decode(text)
	cfb := cipher.NewCFBDecrypter(block, bytes)
	plainText := make([]byte, len(cipherText))
	cfb.XORKeyStream(cipherText, plainText)
	return string(plainText), nil
}

func IsBase64(s string) bool {
	_, err := base64.StdEncoding.DecodeString(s)
	return err == nil
}

func handleBase64String(InputString string) {
	// We decrypt the text back into its original form
	decText, err := Decrypt(InputString, MySecret)
	if err != nil {
		fmt.Println("error decrypting your encrypted text: ", err)
	}
	fmt.Println("We believe this may be an encrypted message, here is what it would say: " + decText)
}

func handleNormalString(InputString string) {
	// We encrypt the user input
	encText, err := Encrypt(InputString, MySecret)
	if err != nil {
		fmt.Println("error encrypting your classified text: ", err)
	}
	fmt.Println("The message was successfully encrypted: " + encText)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Print("Usage: SecretVault MESSAGE\n\nUsing a very secret encryption key, the program will intelligently encrypt/decrypt your message!\n")
		return
	}
	InputString := strings.Join(os.Args[1:], " ")
	InputString = strings.Replace(InputString, '\n', "", -1)

	// If the input text is suspected to be an encrypted message, we decrypt it and display its content
	if IsBase64(InputString) {
		go handleBase64String(InputString)
	}
	handleNormalString(InputString)
}
```
On remarque dans la fonction main un premier problème qui bloque la compilation, on change :
```golang
InputString = strings.Replace(InputString, '\n', "", -1)
```
En : 
```golang
InputString = strings.Replace(InputString, "", "", -1)
```

Ensuite, il faut faire déchiffrer notre programme, pour cela on change la fonction Decrypt : 
```golang
func Decrypt(text, MySecret string) (string, error) {
	block, err := aes.NewCipher([]byte(MySecret))
	if err != nil {
		return "", err
	}
	// We first decode the base64 input text
	cipherText := Decode(text)
	cfb := cipher.NewCFBDecrypter(block, bytes)
	plainText := make([]byte, len(cipherText))
	cfb.XORKeyStream(cipherText, plainText)
	return string(plainText), nil
}
```

En : 
```golang
func Decrypt(text, MySecret string) (string, error) {
	block, err := aes.NewCipher([]byte(MySecret))
	if err != nil {
		return "", err
	}
	encText, _ := base64.StdEncoding.DecodeString(text)
	cfbdec := cipher.NewCFBDecrypter(block, bytes)
	cfbdec.XORKeyStream([]byte(encText), []byte(encText))
	return string(encText), nil
}
```

Et enfin la dernière erreur qui fait que le programme n'affiche pas le déchiffrement se trouve dans la fonction main, c'est la condition d'exécution de la fonction de 
déchiffrement : 

```golang
if IsBase64(InputString) {
		go handleBase64String(InputString)
	}
	handleNormalString(InputString)
```

En : 
```golang
	if IsBase64(InputString) == true {
		handleBase64String(InputString)
	}
	handleNormalString(InputString)
```
