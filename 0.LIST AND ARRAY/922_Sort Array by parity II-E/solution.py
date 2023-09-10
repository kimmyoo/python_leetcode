class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        def getNextEvenIndex(curIndex):
            for i in range(curIndex+1, len(nums)):
                if nums[i] % 2 == 0:
                    return i
        
        def getNextOddIndex(curIndex):
            for i in range(curIndex+1, len(nums)):
                if nums[i] % 2 != 0:
                    return i
        
        for i in range(len(nums) - 1):
            # even index 
            if i % 2 == 0:
                if nums[i] % 2 != 0:
                    nums[i], nums[getNextEvenIndex(i)] = nums[getNextEvenIndex(i)], nums[i]
            # odd index
            else:
                if nums[i] % 2 == 0:
                    nums[i], nums[getNextOddIndex(i)] = nums[getNextOddIndex(i)], nums[i]
        
        return nums
    
    # extra memory
    def sortArrayByParityII_B(self, nums:list[int]) ->list[int]:
        evenInts = []
        oddInts =[]
        res = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evenInts.append(nums[i])
            else:
                oddInts.append(nums[i])
        

        for i in range(len(nums)//2):
            res.append(evenInts[i])
            res.append(oddInts[i])

        return res


    # two pointers optimal solution
    # 先把 两个指针摆到 奇数 index 和 偶数 index上
    # 不断的加2 看看是不是 他们相对应的 数组元素也是 分别对应的
    # 如果 index超越了 上限 （数组长度）
    # 就 break 要先看此条件
    # 当两个指针走到 有偏差的 位置的时候 相互调换位置
    def sortArrayByParityII_C(self, nums:list[int]) ->list[int]:
        indexE, indexO = 0, 1
        l = len(nums)

        while True:
            # first check indexE < l 
            # otherwise nums[indexE] can cause index out of range error
            while indexE < l and nums[indexE] % 2 == 0:
                indexE += 2
            while indexO < l and nums[indexO] % 2 == 1:
                indexO += 2
            if indexO >= l or indexE >= l:
                break
            
            nums[indexE], nums[indexO] = nums[indexO], nums[indexE]
            indexE += 2
            indexO += 2
        return nums