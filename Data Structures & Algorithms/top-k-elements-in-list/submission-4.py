class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countered = Counter(nums)

        listt = []

        for _ in range(k):
            max_key = max(countered, key=countered.get)
            listt.append(max_key)

            del countered[max_key]

        return(listt)




        