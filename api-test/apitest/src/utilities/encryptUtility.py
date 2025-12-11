from Crypto.Cipher import AES
from Crypto import Random
import binascii, os
import base64
import json 
import logging as logger 
from apitest.src.configs import IS_ENCRYPT,PRIVATE_KEY

class AESUtility(object): 
    def __init__(self):
        self.secretKey = base64.b64decode(PRIVATE_KEY)
        self.nonce_size = 12
    
    def encrypt(self, msg):
        nonce = Random.get_random_bytes(self.nonce_size)
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        return base64.b64encode(ciphertext+authTag+aesCipher.nonce)
    
    def decrypt(self, encryptedMsg):
        enc = base64.b64decode(encryptedMsg)
        nonce = enc[-self.nonce_size:]
        authTag = enc[-(self.nonce_size + 16): -self.nonce_size]
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce)
        cipherText = enc[:-(self.nonce_size + 16)]
        plaintext = aesCipher.decrypt_and_verify(cipherText, authTag)
        return plaintext.decode()
    
    def encrypt_payload(self, payload):
        if not IS_ENCRYPT: 
            return json.dumps(payload)
        
        body = self.encrypt(str(payload).encode())
        return json.dumps({'data': body.decode()})
    
    def decrypt_payload(self, body):
        # import requests
        # import pdb;pdb.set_trace()
        if not IS_ENCRYPT:
            return body.json()
        data = body.json()['data']
        if data == '': 
            return ''
        payload = self.decrypt(data) 
        return json.loads(payload)

# data_Json = b'{"loginname": "gsgsd", "password": "123456"}'
# encryptedMsg = AESUtility().encrypt(data_Json)
# print(encryptedMsg)

# decryptedMsg = AESUtility().decrypt(encryptedMsg)
# print("decryptedMsg", decryptedMsg)