def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
attack = input("Attack : ")
shFile = input("Location of shFile : ")
command = 'sh ' + shFile
attack = '../Data/'+ attack + '.csv'
import pexpect

child = pexpect.spawn(command) # Spawns child application
child.sendline('s')
print("Python output")
child.timeout = 5000
output = child.read()
output = output.decode('utf-8')
print(str(output))

decoded_string = bytes(output, "utf-8").decode("unicode_escape")

newLines = []
for line in decoded_string.split('\n'):
    newLine = [x.strip() for x in line.split('\t')]
    fixedNewLine = []
    for elem in newLine:
        if elem != '':
            for i in elem.split(' '):
                if is_number(i):
                    fixedNewLine.append(i)
    newLines.append(fixedNewLine)


with open(attack, 'w') as output_file:
    for elem in newLines:
        if elem:
            print(','.join(elem), file=output_file)
