class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = []
        i = 0

        while i < len(folder):
            if folder[i] not in res:
                res.append(folder[i])
                # need to add "/" to indicate that we are looking for a folder path
                # to avoid deleting non-subfolders like  /a/b, /a/bc
                curFolder = folder[i] + "/"
                if i == len(folder) - 1:
                    break
                while folder[i+1].find(curFolder) == 0:
                    i+=1
                    if i == len(folder) - 1:
                        break
                i+=1
        return res

# rest code
s = Solution()
folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
res = s.removeSubfolders(folders)
print(res)
