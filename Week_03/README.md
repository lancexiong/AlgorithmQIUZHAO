学习笔记
1.使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
思路：
（1）暴力法，遍历整个数组，找到第一个数值小于其前一位数的位置就是无序开始的地方
（2）二分查找，因为半有序数组是局部单调的，所以可以二分查找，看是哪一半的数组不单调
过程：[4, 5, 6, 7, 0, 1, 2]分成2部分，中点mid=3（即nums[3]=7）,比较左半部分第一个元素nums[left]和nums[mid]以及
nums[mid]和nums[mid+1]的关系，如果nums[mid+1]<nums[low]<=nums[mid]则表明nums[mid]后面开始就不是升序的了
则mid就是无序开始的地方；如果不满足关系，则继续往右查找nums[mid+1]~nums[high]

class Solution():
	def search(self,nums):
		if not nums:
			return None
		n=len(nums)
		low,high=0,n
		while low<high:
			mid=low+(high-low)//2
			if nums[mid+1]<nums[low]<=nums[mid] :
				return mid
			else:
				low=mid+1
		return -1  #查找不到返回-1

2. 一个问题该用递推、搜索还是动态规划，完全是由这个问题本身不同阶段状态转移方式决定的
每个阶段就1个状态——————>递归
每个阶段的最优状态都由上一个阶段的最优状态得到——————>贪心算法
每个阶段的最优状态由之前所有阶段的状态组合得到——————>搜索 
每个阶段的最优状态可以由之前某个阶段的某个或某些状态直接得到而不管之前这个状态如何得到——————>动态规划