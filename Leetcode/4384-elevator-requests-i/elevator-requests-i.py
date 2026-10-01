class Solution(object):
    def elevatorRequests(self, n, requests):
        res = requests[0]
        n =len(requests)
        for i in range(n-1):
            res+=abs(requests[i]-requests[i+1])
        return res    