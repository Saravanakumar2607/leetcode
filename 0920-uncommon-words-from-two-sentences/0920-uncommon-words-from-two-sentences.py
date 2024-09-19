from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        count1 = Counter(s1.split())
        count2 = Counter(s2.split())
     
        uncommon_words = []
        
      
        for word in count1:
            if count1[word] == 1 and count2[word] == 0:
                uncommon_words.append(word)
        
        
        for word in count2:
            if count2[word] == 1 and count1[word] == 0:
                uncommon_words.append(word)
        
        return uncommon_words
