from flask import Flask, render_template
import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')

class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, msg ):
        msg = pad(msg)
        iv =  b'\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef'#16 * b'\x00'
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode(cipher.encrypt( msg ) )


key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\x01\x23\x45\x67\x89\xab\xcd\xef'
key_js = "0123456789abcdef0123456789abcdef"
iv_js = "0123456789abcdef0123456789abcdef"
#hex_key = hex + key[0] + key[1] + hex + key[2] + key[3] + hex + key[4] + key[5] + hex + key[6] + key[7] + hex + key[8] + key[9] + hex + key[10] + key[11] + hex + key[12] + key[13] + hex + key[14] + key[15]
msg = "y"

cipher = AESCipher(key)
encrypted = cipher.encrypt(msg).decode('utf8') #se pasa el mensaje criptografia en utf-8
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('desciframe.html', msg = encrypted, iv = iv_js, key = key_js)

if __name__ == '__main__':
    app.run(debug=True)
