class Solution:
    def defangIPaddr1(self, address: str) -> str:
        l = address.split(".")
        delimiter = "[.]"
        res = delimiter.join(l)
        return res

    def defangIPaddr2(self, address: str) -> str:
        return address.replace(".", "[.]")
        
    

    # the .join() method is always a string method
    # not a list method  delimiter.join(iterable)
    # it is also recommended way to do string concatenation


