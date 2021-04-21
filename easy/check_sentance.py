class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        text='qwertyuiopasdfghjklzxcvbnm'
        for i in text:
            if len(sentence)<26:
                return False
            elif i not in sentence:
                return False    
        return True
