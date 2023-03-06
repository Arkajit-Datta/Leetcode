from ast import List


class Solution:
    def decimalToBinary(self, n) -> list:
        binary_number, res = bin(n).replace("0b", ""), []
        res.extend(
            count
            for count, char in enumerate(reversed(binary_number))
            if char != "0"
        )
        return res
    def check(self, store, binary_list):
        return all(index not in store for index in binary_list)
    
    def reInitialise(self, i,j,store, binary_list):
        while not self.check(store, binary_list):
            list_to_remove = self.nums_binary_res[self.nums[j]]
            for ele in list_to_remove:
                store.remove(ele)
            del self.nums_binary_res[self.nums[j]]
            j+=1
        return store, j, len(self.nums_binary_res)
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i, j, store, self.nums, max_so_far, curr_max, self.nums_binary_res = 0,0,set(), nums,-1, 0, {}
        while i < len(nums):
            binary_ones_list = self.decimalToBinary(nums[i])
            if not self.check(store, binary_list=binary_ones_list):
                max_so_far = max(max_so_far, curr_max)
                store, j, left = self.reInitialise(i,j,store)
                curr_max = left

            self.nums_binary_res[nums[i]] = binary_ones_list
            for ones in binary_ones_list:
                store.add(ones)
            curr_max+=1
            i+=1
        return max(max_so_far, curr_max) 
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.decimalToBinary(2))