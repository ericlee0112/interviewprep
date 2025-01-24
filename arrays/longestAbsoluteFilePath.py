'''
https://leetcode.com/problems/longest-absolute-file-path/description/

dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext

dir
    \n\tsubdir1
        \n\t\tfile1.ext
        \n\t\tsubsubdir1
    \n\tsubdir2
        \n\t\tsubsubdir2
            \n\t\t\tfile2.ext

'''
import collections
import heapq
class Solution:
    def longestAbsoluteFilePath(self, s):
        # write your code here
        maxlen = 0
        pathlen = collections.defaultdict(int)
        tokens = s.split("\n")
        for token in tokens:
            fileOrDirName = token.lstrip('\t')
            depth = len(token) - len(fileOrDirName)
            if '.' in fileOrDirName:
                maxlen = max(maxlen, pathlen[depth] + len(fileOrDirName))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(fileOrDirName) + 1
        return maxlen

        

s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
sln = Solution()
print(sln.lengthLongestPath(s))

