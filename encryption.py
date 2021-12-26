from rsa import newkeys, encrypt, decrypt
from rsa.key import PublicKey, PrivateKey

from os.path import isfile
from os import remove

from db import savePublicKey, savePrivateKey

def generateKeys():
    (publicKey, privateKey) = newkeys(512)

    (n, e) = publicKey['n'], publicKey['e']
    (d, p, q) = privateKey['d'], privateKey['p'], privateKey['q']
    
    def save():
        savePublicKey(n, e)
        savePrivateKey(n, e, d, p, q)

    if isfile('db/public.json') or isfile('db/private.json'):
        remove('db/public.json')
        remove('db/private.json')
        save()
    else: save()
