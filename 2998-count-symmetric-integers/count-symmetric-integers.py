class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low,high+1):
            numstr = str(num)
            numlen = len(numstr)
            if numlen %2 == 0:
                half1 = numstr[:numlen//2]
                half2 = numstr[numlen//2:]
                h1sum = 0
                h2sum = 0
                for i in range(numlen//2):
                    h1sum+=int(half1[i])
                    h2sum+=int(half2[i])
                print(num, half1," ", half2, " ", h1sum,h2sum)
                if h1sum == h2sum:
                    count += 1

        return count