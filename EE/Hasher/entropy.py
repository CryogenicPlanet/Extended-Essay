from zxcvbn import zxcvbn
results = []
fileInput = input("Enter File Path : ")
unencrypted = open(fileInput,"r")
while True:
    line = unencrypted.readline()
    if not line:
        break
   	result = zxcvbn(line)
    results.append(result)
unencrypted.close()
scores = results['score']
import statistics 
mean = statistics.mean(scores)
