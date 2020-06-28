#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2020-6-28
# @Author: BaoRui
# @File: MiniSizeSubarray.py
# @Description: Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
#               subarray of which the sum >= s. If there is not one, return 0.

from typing import List
class Solution:
    # 滑动窗口求最接近目标值的子数组
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0 # 左侧索引
        resultLen = 0 # 返回的结果（长度）
        subSum = 0
        for j in range(len(nums)):
            subSum += nums[j]
            while subSum >= s:
                resultLen = j - i + 1 if resultLen == 0 else min(j - i + 1, resultLen)
                subSum -= nums[i]
                i += 1
        return resultLen

s = Solution()
print(s.minSubArrayLen(103, [44, 44, 44, 101, 1, 1, 1, 99]))
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))