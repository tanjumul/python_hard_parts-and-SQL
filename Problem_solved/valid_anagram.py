class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
            if len(s) != len(t): 
                return False 
        
            return sorted(s) == sorted(t)
        
        """ In this porblem i compared the length of the two strings then i sorted te strings so that it can match in sorted way also otherwise it's not the anagram  """