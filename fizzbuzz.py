# Fizzbuzz is program that prints fizz for the number divisible by 3 and buzz for the number divisible by 5

class Fizzbuzz :
    def __init__(self, list):
        self.numbers = list

    
    def fizz_or_buzz(self) :
        for n in self.numbers :
            if n % 3 == 0 and n % 5 == 0 :
                print("Fizzbuzz")
            elif n % 3 == 0 :
                print("Fizz")
            elif n % 5 == 0 :
                print("Buzz")
            else :
                print(f"{n}")


numbers = [2,3,5,15,23]
fizzbuzz = Fizzbuzz(numbers)
fizzbuzz.fizz_or_buzz()