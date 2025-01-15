import re
class Words :
    def wordsCounter(self, line) :
        line = line.lower()
        words = re.split(r'[.\s]+', line.strip()) 
        # in this split() will remove all "." and whitespaces in the sentence and then strip() will remove all 
        # the leading and trailing whitespaces from the sentence
        distinct_ele = []
        for i in words :
            distinct_ele.append(i)
            if distinct_ele.count(i) == 1 :
                print(i, "=", words.count(i))
      

words = Words()
sentence = "This is test . This Is just a test"
words.wordsCounter(sentence)