class Fibonacci :
    def fibonacci(self, num) :
        if num <=1 :
            return num
        else :
            return num * self.fibonacci(num - 1)
    
fibonacci = Fibonacci()
print(fibonacci.fibonacci(5))