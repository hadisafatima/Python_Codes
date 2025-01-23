# This program checks if a number is prime or not

class Prime_number :
    def __init__(self, number):
        self.num = number 


    def is_a_prime(self) :
        count = 0
        for n in range(1,self.num + 1,1) :
            if self.num % n == 0 :
                count += 1
        
        if count == 2 :
            print(f"{self.num} is a Prime Number")
        else :
            print(f"{self.num} is NOT a Prime Number")

num = int(input("Enter any number that want to check is prime or not : "))
prime = Prime_number(num) 
prime.is_a_prime()