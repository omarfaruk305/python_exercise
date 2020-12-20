def perfectnumber (func) :
    def wrapper (number) : 
        perfectnumbers = []
        for num in number : 
            divisors = []
            total = 0
            tempdivisors = range (1,num)
            for div in tempdivisors :
                if num % div == 0  :
                    divisors.append(div)
            for div in divisors : 
                total += div
            if total == num : 
                if not total == 0 :
                    perfectnumbers.append(num)
        print("perfectnumbers : " ,perfectnumbers)
        func(number)
    return wrapper    

@perfectnumber
def prime_number(number) : 
    numbers = list()
    for num in number  : 
        divisors = range (2,num+1)
        counter = 0
        for div in divisors :
            if num % div == 0 :
                counter +=1
                continue
        if counter == 1 :
            numbers.append(num)
    print("prime numbers : ",numbers)
print(prime_number(range(1000)))