class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers)<2:
            return None
        pair_dict={}
        for i in range(len(numbers)):
            if (target-numbers[i]) in pair_dict:
                return [pair_dict[target-numbers[i]],i]
            else:
                pair_dict[numbers[i]]=i
        return None
