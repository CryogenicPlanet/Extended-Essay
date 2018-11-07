from passlib.hash import md5_crypt ,sha1_crypt,sha256_crypt,sha512_crypt
import hashlib

fileInput = input("Enter File Path : ")
fileOutput = input("Enter Output File Path : ")
algo = input("Choose Algo: 1. MD5 2.SHA1 3. SHA256 4. SHA512 : ")
unencrypted = open(fileInput,"r")
encrypted = open(fileOutput,"w")
while True:
    line = unencrypted.readline()
    if not line:
        break
    if algo == "1":
        hash_object = hashlib.md5(line.encode()).hexdigest()
    elif algo == "2":
        hash_object = hashlib.sha1(line.encode()).hexdigest()
    elif algo == "3":
        hash_object = hashlib.sha256(line.encode()).hexdigest()
    elif algo == "4":
        hash_object = hashlib.sha512(line.encode()).hexdigest()
    encrypted.write(hash_object)
    encrypted.write("\n")
encrypted.close()
unencrypted.close()

