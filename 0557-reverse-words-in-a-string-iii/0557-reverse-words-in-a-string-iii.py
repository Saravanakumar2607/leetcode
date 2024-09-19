class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(word): 
            return word[::-1]

        words = s.split()
        reversed_words = [reverse_word(word) for word in words] 
        return " ".join(reversed_words) 


s = "Let's take LeetCode contest"
result = Solution().reverseWords(s)
print(result) 