class Palindrome :
    def isPalindrome(self, word) :
        word = word.lower()
        backwards = word[::-1]
        # word[::-1] provides the reverse of the word

        if word == backwards :
            print(f"'{word}' is a Palindrome")
            # "f" here is f-string, it denotes a formatted string literal
        else : 
            print(f"'{word}' is not a Palindrome")

p = Palindrome()
text = "TooT"
p.isPalindrome(text)