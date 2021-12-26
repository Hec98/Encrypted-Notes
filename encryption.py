from rsa import newkeys, encrypt, decrypt
from rsa.key import PublicKey, PrivateKey

from tkinter.messagebox import showinfo, askyesno

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
        showinfo('Info','New keys generated')

    if isfile('db/public.json') or isfile('db/private.json'):
        res = askyesno('Are you sure?', 'It will remove the existing keys, in addition to removing the current database')
        if res is True:
            remove('db/public.json')
            remove('db/private.json')
            save()
    else: save()
