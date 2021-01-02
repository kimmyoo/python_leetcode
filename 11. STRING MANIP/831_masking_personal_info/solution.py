class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S[-1].isalpha():
            email = S.split("@")
            email[0] = email[0][0].lower() + "*****" + email[0][-1].lower()
            email[1] = email[1].lower()
            return email[0]+"@"+email[1]
        
        tel = [ch for ch in S if ch.isnumeric()]
        last4Digits = "".join(tel[-4:])
        local = "***-***-" + last4Digits
        if len(tel) == 10:
            return local
        else:
            l = len(tel)-10
            areaCode = "+" + "*"*l + "-"
            phoneNum = areaCode + local
        return phoneNum
    
    def maskPIIB(self, S):
        at = S.find('@')
        if at >= 0:
            return (S[0] + "*" * 5 + S[at - 1:]).lower()
        S = "".join(i for i in S if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(S) - 10] + "***-***-" + S[-4:]