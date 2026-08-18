class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        name = strs[0]

        for word in strs[1:]:
            ans = ""

            for i, char in enumerate(word):
                if i >= len(name) or char != name[i]:
                    break
                ans += char

            name = ans

        return name

            