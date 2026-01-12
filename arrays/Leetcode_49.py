from typing import List

class Solution:

    def groupAnagrams_UsingSort(self, strs: List[str]) -> List[List[str]]:

        str_hash = {}

        for i in range(len(strs)):

            key = "".join(sorted(strs[i]))

            if key in str_hash.keys():

                str_hash[key].append(strs[i])
            
            else:
                    
                str_hash[key] = [strs[i]]

        res = []
        for key, value in str_hash.items():

            res.append(value)

        return res
    
    def groupAnagrams_UsingCharWeight(self, strs: List[str]) -> List[List[str]]:

        str_hash = {}

        for i in range(len(strs)):

            alpha_keys = [0] * 26
            
            for alpha in strs[i]:
                
                ch_weight = ord(alpha) - ord("a")
                
                alpha_keys[ch_weight] += 1

            if tuple(alpha_keys) in str_hash.keys():

                str_hash[tuple(alpha_keys)].append(strs[i])
            else:

                str_hash[tuple(alpha_keys)] = [strs[i]]
        
        res = []
        
        for key, value in str_hash.items():

            res.append(value)

        return res
