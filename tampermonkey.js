// ==UserScript==
// @name         tarea3
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  tarea criptografia
// @author       You
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js
// @updateURL    https://github.com/JoacoVial/TAREA3/blob/main/tampermonkey
// @match        http://127.0.0.1:5000/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

function hex_to_ascii(str1)
 {
	var hex = str1.toString();
	var str = '';
	for (var n = 0; n < hex.length; n += 2) {
		str += String.fromCharCode(parseInt(hex.substr(n, 2), 16));
	}
	return str;
 }

var iv = document.getElementsByClassName("iv")[0].id;
var key = document.getElementsByClassName("key")[0].id;

iv = CryptoJS.enc.Utf8.parse(iv)
key = CryptoJS.enc.Utf8.parse(key);

const msg = document.getElementsByClassName("AES")[0].id;

var decrypt = CryptoJS.AES.decrypt(msg, key, {
  iv: iv,
  mode: CryptoJS.mode.CBC,
  padding: CryptoJS.pad.Pkcs7
});

document.getElementById("descifrado").innerHTML = hex_to_ascii(decrypt);
})();
