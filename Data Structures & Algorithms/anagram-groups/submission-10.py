class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for word in strs:
            arr = [0 for i in range(26)]
            for c in word:
                arr[ord('a') - ord(c)] += 1
            mapp[tuple(arr)].append(word)
        return list(mapp.values())

            
