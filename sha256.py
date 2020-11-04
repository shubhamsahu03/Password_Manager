import hashlib as hb
from random import *
import string
import  pymysql
from tkinter import *
def generate_salt():
    table=string.printable
    password=""
    for i in range(randint(0,20)):
        x=randint(0,94)
        password+=string.printable[x]
    password_encoded=password.encode("utf-8")
    return password_encoded

def sha256_algo(s,a):


    m=hb.sha256()
    m.update(s.encode("utf-8")+a)
    return m.hexdigest()
import os,pbkdf2,binascii,secrets,pyaes,pymysql
def initialization_vector():
    iv =secrets.randbits(256)
    return iv
def key_salt():
    salt = os.urandom(32)
    return salt
"""def check(a):
    n=len(a)
    return n
print(check(str(initialization_vector())))"""
"""def encrypt(plaintext):

    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted:', binascii.hexlify(ciphertext).decode())
"""
"""
con=pymysql.connect(host="localhost",user="root",password='',database="password_database")
cur=con.cursor()
a=input("enter :")
c=input("enter password:")
cur.execute("select Password,salt from user where Username=%s",(a))
data_2=cur.fetchone()
salt_encoded=data_2[1].encode("utf-8")
b=sha256_algo(c,salt_encoded)
print(b)
"""






"""
def sha256_algo_2(s):
    x=s.encode("utf-8")

    m=hb.sha256()
    m.update(x)
    m.hexdigest()
    return m.hexdigest()
"""
#2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
