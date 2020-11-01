"""def rearrange(arr, n):


    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n


    for i in range(0, n):
        arr[i] = int(arr[i] / n)






    for i in range(0, n):
        print(arr[i], end=" ")




arr = [3, 2, 0, 1]
n=len(arr)



rearrange(arr, n)

"""
"""
def swapList(s):
    a = len(s)


    b = s[0]
    s[0] = s[a - 1]
    s[a - 1] = b

    return s


lst=[]
flag=True
while flag:
    x=int(input("Enter your value:"))
    lst.append(x)
    flag=bool(int(input("do you want to continue?")))
print(lst)

print(swapList(lst))"""

"""
def HowManyFunction(lst,val):
    a=len(lst)
    b=0
    for i in range(0,a):
       if lst[i]==val:
           b+=1
       else:
           pass
    print("the element appeared",b)
lst=[12,14,33,12,56,12,89]
val=int(input("enter:"))

HowManyFunction(lst,val)"""
"""
def increment(n):

    n. append([49])

    return n[0], n[1], n[2], n[3]

L = [23, 35, 47]

mi, m2, m3, m4 = increment (L)

print(L)

print(mi, m2, m3, m4)

print(L[3] == m4)"""

"""
import random
text = "CBSEONLINE"
count = random.randint(0,3)
c=9
while text[c] != 'L':
 print(text[c]+text[count]+'*',end=" ")
 count= count + 1
 c = c-1
 
i. EC* NB* IS*
ii. NS* IE* LO*
iii. ES* NE* IO*
iv. LE* NO* ON*"""
"""
L1 = [100,900,300,400,500]
START = 1
SUM = 0
for C in range(START,4):
 SUM = SUM + L1[C]
 print(C, ":", SUM)
 SUM = SUM + L1[0]*10
 print(SUM)"""
"""
TXT=["20","50","30","40"]
CNT=3
TOTAL=0
for C in [7,5,4,6]:
    T=TXT[CNT]
    TOTAL=float(T)+C
    print(TOTAL)
    CNT-=1
    """
"""
import random
NAV=["LEFT","FRONT","RIGHT","BACK"]
NUM=random.randint(1,3)
NAVG=""
for C in range(NUM,1,-1):
    NAVG+=NAV[C]
    print(NAVG)"""
"""def MSEARCH(STATES):
    for i in range(len(STATES)):
        if STATES[i][0]=="M":
           print(STATES[i])
        else:
            pass"""

"""
def mul(L, odd_L, even_L):
    for i in range(len(L)):
        if L[i] % 2 == 0:
            even_L.append(L[i])
        else:
            odd_L.append(L[i])
    print("The list L", L)
    print("the odd values of L:", odd_L)
    print("the even values of L:", even_L)"""

#gAAAAABfgCGFf4-mJYi13Xl6WYzeLQl6spNUj_03tU5EhR0wgoi64KfRYb374WRiuh9NUw6_W_0Xy_5kUMB4jpwOOcXe_G_fng==
a="gAAAAABfgCGndaZX8Sq2ma9j1cMVRIt1r76B7XB6RQtUOL5jZNkVFhMoeiCletCd3RgF5nJiGF0i_YRKMDPu3HiVp9o7q9Vhdg=="
#main
import os,pbkdf2,binascii,secrets,pyaes,pymysql
salt=os.urandom(32)
s=salt
password = "shubham"

key = pbkdf2.PBKDF2(password, s,1500).read(32)
print('AES encryption key:', (binascii.hexlify(key).decode()))
iv=secrets.randbits(256)
plaintext =input("enter text to be encrytped:")
#encrytion
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print(ciphertext)
print('Encrypted:', binascii.hexlify(ciphertext).decode())
#decryption

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('Decrypted:', decrypted.decode())
# wrongly derived key
key = os.urandom(32)   # random decryption key
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
print('Wrongly decrypted:', aes.decrypt(ciphertext))

#functions for encryption/decryption
"""def keygenerate(password,salt):
    key=
def encryption():"""

#testing for database
"""con = pymysql.connect(host="localhost", user="root", password='', database="test")
cur=con.cursor()
cur.execute("select * from testing where id=%s",(1))
data=cur.fetchone()
for i in data:
    print(i)
con.close()


"""

"""print(os.urandom(32).decode("latin1").encode("latin1"))"""









