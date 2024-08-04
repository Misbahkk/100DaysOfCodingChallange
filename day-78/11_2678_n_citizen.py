class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """

        count = 0
        for det in details:
            # for char in range(len(det)):
            age = det[11]+det[12]

            if age > '60':
            
                print(age)
                count=count+1
        return count

        



obj = Solution()
details = ["1313579440F2036","2921522980M5644"]
over_60 = obj.countSeniors(details)
print(over_60)
