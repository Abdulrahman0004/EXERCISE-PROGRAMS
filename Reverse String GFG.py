class Solution:
    def reverse_string(self, s):
        if s == "":
            return
        return s[::-1]

ob = Solution()
result = ob.reverse_string("Geeks")

if result is not None:
    print(result)