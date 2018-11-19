from zxcvbn import zxcvbn
results = []
fileInput = input("Enter File Path : ")
unencrypted = open(fileInput,"r")
words = []
for elem in unencrypted:
    elem = elem.split("\n")
    words.append(elem[0])
unencrypted.close()
for elem in words:
    result = zxcvbn(elem)
    results.append(result)
scores = results['score']
import statistics
mean = statistics.mean(scores)
