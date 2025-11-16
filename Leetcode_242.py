class Solution(object):


    def isAnagram_hashTable_notOptimised(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        n = len(s)

        countS = {}
        countT = {}

        for i in range(n):

            if s[i] not in countS.keys():

                countS[s[i]] = 1
            else:

                countS[s[i]] += 1

            if t[i] not in countT.keys():

                countT[t[i]] = 1
            else:

                countT[t[i]] += 1


        return countS == countT

    def isAnagram_hashTable_Optimised(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        
        countS = {}
        countT = {}

        for i in range(k=len(s)):

            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)

        
        return countS == countT