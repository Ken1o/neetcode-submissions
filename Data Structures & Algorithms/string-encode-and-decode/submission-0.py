class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        len_str = []
        for i in strs:
            len_str.append(len(i))
        res = []
        for s in len_str:
            res.append(str(s))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        len_str, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            len_str.append(int(s[i:j]))
            i = j + 1

        i += 1
        for k in len_str:
            res.append(s[i:i + k])
            i += k
        return res


