# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')


result = Solution().defangIPaddr("1.1.1.1")
print(result)
