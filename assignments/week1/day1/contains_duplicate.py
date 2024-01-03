class Soulution(object):
    def containsDuplicate(self, nums):
        map1 = {}
        for i in nums:
            if i in map1:
                return True
            else:
                map1[i] = True
        return False        
    