import random

print("Welcome to my guess of number game. The rool is simple , the program will give you a number and you'll try to guess.")

print("1 '-' symbol is mean , in the number can be any digit is true but place is wrong.\n2 '+' symbol is mean , in the number can be any digit is true and also place is true ")

print('Can be max 5 digit.If you want to exit the game please press "E" ')
digitnumber = input("How many digit do you want ? : ")
if digitnumber > '5' : 
    raise KeyError ('Please write lower than 5 digit.')

def randomnumber (): #Making random number
    random_num = random.randint(numbersdic1[digitnumber],numbersdic2[digitnumber])
    random_num = str(random_num)
    return random_num
def checksamedigits(random_num):
    for i in random_num : #Checking same digits. if we have , it will change all number again until distinct digits.
        counter = 0
        for k in random_num : 
            if k == i :
                counter +=1
        if counter > 1:
            random_num = randomnumber()
            checksamedigits(random_num)
    return (random_num)

#Is this really working?
numbersdic1 = {'1':1,'2':10,'3':100,'4':1000,'5':10000}
numbersdic2 = {'1':9,'2':99,'3':999,'4':9999,'5':99999}
random_num = randomnumber()
random_num = checksamedigits(random_num)
while True :
    result = list()
    guessnumber = str(input("Guess Number : ")) 
    if guessnumber == "e" : 
        print('Bye')
        break
    elif len(str(guessnumber)) != digitnumber:
        raise ValueError ('Please enter suitable Value ')
        continue
    for i in guessnumber:
        for j in random_num:
            if i == j :
                if guessnumber.index(i) == random_num.index(j):
                    result.append('+')
                elif guessnumber.index(i) != random_num.index(j):
                    result.append('-')
    
    if result == (list('+') * int(digitnumber)): 
        print('congats your number was ',random_num)
        break
    elif len(result) == 0 : 
        print('Go gO go')
    else :
        print(result)