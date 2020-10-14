from flask import Flask, render_template
import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')

class AESCipher:

    def __init__( self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt( self, msg ):
        msg = pad(msg)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode(cipher.encrypt( msg ) )

app = Flask(__name__)

@app.route('/')
def home():
    aux = True
    while(aux):
        key = input("Ingrese la llave de 16 caracteres: ")
        iv = input("Ingrese el vector inicial de 16 caracteres: ")
        msg = input("Ingrese el mensaje: ")
        if(len(key) == 16 | len(iv) == 16):
            aux = False
        else:
            print("-----------------------------------\nLA LLAVE O EL VECTOR NO TIENEN 16 CARACTERES\n-----------------------------------")

    cipher = AESCipher( bytes(key, 'utf-8'), bytes(iv, 'utf-8'))
    encrypted = cipher.encrypt(msg).decode('utf8') #se pasa el mensaje criptografia en utf-8

    return render_template('index.html', msg = encrypted, iv = iv, key = key)

if __name__ == '__main__':
    app.run(debug=True)
