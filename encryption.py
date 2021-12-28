from rsa import newkeys, encrypt, decrypt
from rsa.key import PublicKey, PrivateKey

from tkinter.messagebox import showinfo, askyesno, showwarning

from os.path import isfile
from os import remove

from tinyDB import savePublicKey, savePrivateKey, getKeys
from mongoDB import deleteDB

def generateKeys():
    def save():
        (publicKey, privateKey) = newkeys(512)
        (n, e) = publicKey['n'], publicKey['e']
        (d, p, q) = privateKey['d'], privateKey['p'], privateKey['q']

        savePublicKey(n, e)
        savePrivateKey(n, e, d, p, q)
        showinfo('Info','New keys generated')

    if isfile('db/public.json') or isfile('db/private.json'):
        res = askyesno('Are you sure?', 'It will remove the existing keys, in addition to removing the current database')
        if res is True:
            remove('db/public.json')
            remove('db/private.json')
            deleteDB()
            save()
    else: save()

def keys():
    publicKey, privateKey = getKeys()
    publicKey = PublicKey(int(publicKey[0]), int(publicKey[1]) )
    privateKey = PrivateKey(int(privateKey[0]), int(privateKey[1]), int(privateKey[2]), int(privateKey[3]), int(privateKey[4]))
    return publicKey, privateKey

def encryption(text):
    publicKey, _ = keys()
    encText = encrypt(text.encode('utf8'), publicKey)
    return encText

def decrypted(text):
    _, privateKey = keys()
    decText = decrypt(text, privateKey).decode('utf8')
    return decText
