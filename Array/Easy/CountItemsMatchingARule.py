# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        if (ruleKey == 'type'):
            return len([i for i in items if i[0] == ruleValue])
        elif (ruleKey == 'color'):
            return len([i for i in items if i[1] == ruleValue])
        else:
            return len([i for i in items if i[2] == ruleValue])


result = Solution().countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], [
    "phone", "gold", "iphone"]], ruleKey="type", ruleValue="phone")
print(result)
