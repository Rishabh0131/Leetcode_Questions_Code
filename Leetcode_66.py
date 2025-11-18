from typing import List, int

class Solution:


    def plusOneApprochOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 0:

            return []

        number = 0

        for i in digits:
            
            number = number * 10 + i

        number = number + 1

        return [ int(i) for i in str(number) ]
    
    def plusOneApproach_MostEfficient(self, digits: List[int]) -> List[int]:

        if len(digits) == 0:

            return []
        
        for i in range(len(digits)-1, -1, -1):

            if digits[i] + 1 != 10:

                digits[i] +=1
                return digits

            digits[i] = 0

        return [1] + digits