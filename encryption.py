from rsa import newkeys, encrypt, decrypt
from rsa.key import PublicKey, PrivateKey

from tkinter.messagebox import showinfo, askyesno
from os.path import isfile
from os import remove

from tiny_db import save_public_key, save_private_key, get_keys
from mongodb import delete_db

def generate_keys():
    def save():
        (public_key, private_key) = newkeys(2048)
        (n, e) = public_key['n'], public_key['e']
        (d, p, q) = private_key['d'], private_key['p'], private_key['q']

        save_public_key(n, e)
        save_private_key(n, e, d, p, q)
        showinfo('Info','New keys generated')

    if isfile('db/public.json') or isfile('db/private.json'):
        res = askyesno('Are you sure?', 'It will remove the existing keys, in addition to removing the current database')
        if res is True:
            remove('db/public.json')
            remove('db/private.json')
            delete_db()
            save()
    else: save()

def keys():
    public_key, private_key = get_keys()
    public_key = PublicKey(int(public_key[0]), int(public_key[1]) )
    private_key = PrivateKey(int(private_key[0]), int(private_key[1]), int(private_key[2]), int(private_key[3]), int(private_key[4]))
    return public_key, private_key

def encryption(text):
    public_key, _ = keys()
    enc_text = encrypt(text.encode('utf8'), public_key)
    return enc_text

def decrypted(text):
    _, private_key = keys()
    dec_text = decrypt(text, private_key).decode('utf8')
    return dec_text
