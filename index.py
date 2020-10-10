from flask import Flask, render_template
import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key)

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = 16 * b'\x00'
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode(cipher.encrypt( raw ) )

key = 16
cipher = AESCipher(key)
iv = "00000000000000000000000000000000"
encrypted = cipher.encrypt('criptografia2020').decode('utf8') #se pasa el mensaje criptografia en utf-8
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('decode.html', variable = encrypted, variable2 = iv)

if __name__ == '__main__':
    app.run(debug=True)
