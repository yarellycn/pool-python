#TASK 2.1
#Compute the value of 1 + 11 + 111 + ... + 111111111.
# Then, compute this result power 2, power 3, power 4 and power 5.

nb = 1
total = 0

for i in range(9):                  #range(9) bc il y a 9 digits dans "111111111"
    total = total + nb              #0+1=1         1+11=12          12+111=123       ...
    nb = nb * 10 + 1                #1*10+1=11     11*10+1=111      111*10+1=1111   ...
print(total)

def power(nb: int, power:int):      #je definis ma fonction et comment je vais la rappeller + tard
    result = 1
    for i in range(power):
        result = result * nb
    return result                   #return bc je veux retourner le result

for i in range(2,6):
    print(power(total, i))