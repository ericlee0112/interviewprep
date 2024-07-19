class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            token = str(len(s)) + "#" + s
            res += token
        return res

    def decode(self, s):
        nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        i = 0
        listOfStrings = []

        while i < len(s):

            stringLengthInString = ""
            while s[i] in nums:
                stringLengthInString += s[i]
                i += 1
            
            stringLength = int(stringLengthInString)
            i += 1
            # the following string is s[i:stringLength + i]
            token = s[i:stringLength + i]
            listOfStrings.append(token)
            i += stringLength
        return listOfStrings
