class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorteds = "".join(sorted(s))
            if sorteds not in res:
                res[sorteds] = [s]
            else:
                res[sorteds].append(s)
        return list(res.values())