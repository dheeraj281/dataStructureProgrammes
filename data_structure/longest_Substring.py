
class Find_Substring:

    def unique_substring(self,newstr):
        length = 0
        subs = ""

        for char in newstr:

            if char not in subs:
                subs = subs+char
                length = max(length, len(subs))
            else:
                cut = subs.index(char)
                subs = subs[cut+1:]+char

        return length

    def palindrome_substring(self,mystr):
        res = ""
        for i in range(len(mystr)):
            odd = self.findPalindrome(mystr, i, i)
            even = self.findPalindrome(mystr, i, i+1)
            res = max(odd,even,res,key=len)
        return res

    def findPalindrome(self,mystr,left,right):
        while left>=0 and right<len(mystr) and mystr[left] == mystr[right]:
            left -= 1
            right += 1
        return mystr[left+1: right]


obj = Find_Substring()
print(obj.palindrome_substring("dbobjayadadradarredivider"))

