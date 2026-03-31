class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]

        hashMap = {}

        res = []

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        for key, value in hashMap.items():
            freq[value].append(key)

        for i in range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])

                if len(res) == k:
                    return res