# This program checks whether 2 strings contains the same alphabets or not (If the strings are Anagrams or not)
from collections import Counter

class Anagram :
    def are_anagrams(self, word1, word2) :
        w1 = word1.lower()
        w2 = word2.lower()

        if len(w1) != len(w2) :
            print(f"{w1} and {w2} are not Anagrams")
            return            
        
        if Counter(w1) == Counter(w2) :
            # this counter() counts whether both words has same characters for same number of times
            print(f"{w1} and {w2} are Anagrams")
            return


anagram = Anagram()
anagram.are_anagrams("hello", "listen")







# ALTERNATIVELY, THE APPROACH BELOW CAN ALSO BE USED


# class Anangram :
#     def are_anagrams(self, word1, word2) :
#         w1 = word1.lower()
#         w2 = word2.lower()

#         if len(w1) != len(w2) :
#             print(f"{w1} and {w2} are not Anagrams")
#             return
        
#         anagrams = sorted(w1) == sorted(w2)
#         if anagrams :
#             print(f"{w1} and {w2} are Anagrams")
#             return
#         else :
#             print(f"{w1} and {w2} are not Anagrams")

# anagram = Anangram()
# anagram.are_anagrams("silents", "silent")