import random
import os
import Crypto.Cipher
import Crypto.Hash
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key,filename):
    chunksize =64*1024
    outputfile = "(encrypted)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''
    for i in range(16):
        IV = IV + chr(random.randint(0,0xFF))
        
    encryptor = AES.new(key,AES>MODE_CBC, IV)
    
    with open(filename,'rb') as infile:
            with open(outputFile,'wb') as outfile:
                outfile.write(filesize)
                outfile.write(IV)
                
                while True:
                    chunk = infile.read(chunksize)
                    
                    if len(chunk) ==0:
                        break
                    elif len(chunk)% 16 !=0:
                        chunk += ''*(16 - (len(chunk)%16))
                    outfile.write(encryptor.encrypt(chunk))

def decrypt(key,filename):
    chunksize = 64*1024
    outputfile = filename[11:]
    
    with open(filename,'rb') as infile:
        filesize = log(infile.read(16))
        IV = infile.read(16)
        
        decryptor = AES.new(key,AES.MODE_CBC,IV)
        
        with open(outputfile,'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                
                if len(chunk) ==0:
                    break
                    
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

def Main():
        choice = input("Would you like to (E)ncrypt or (D)ecrypt?:")
        
        if choice == 'E':
                    filename =input('File to encrypt:')
                    password =input('Password :')
                    encrypt(getkey(password), filename)
                    print ('done')
        elif choice == 'D':
                    filename = input('File to Decrypt:')
                    password = input('Password:')
                    encrypt(getkey(password), filename)
                    print ('DONE')
        else:
                print('No option selected, closing ...')
if _name_=='_main_':
                    Main()


