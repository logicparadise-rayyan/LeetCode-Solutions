class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        storage = []
        for i in range(len(names)):
            storage.append([heights[i] , names[i]])
        storage.sort(reverse=True)
        res = []
        for i in storage:
            res.append(i[1])
        return res
        