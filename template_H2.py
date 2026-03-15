# Do not change the filename or function headers
# You are free to add helper functions
# note: you will only have 5 attempts to run the autograder

import sys
import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


# ============================================================================
# Q1. Quick Sort
# ============================================================================
# Quick sort is a Divide and Conquer algorithm. Choose the last element as the
# pivot and partition the array around it, then recursively sort each partition.

# function header for Q1.1 (Auto & manual grading)
# input_list -> list of integers
# return -> sorted list (ascending order)
#
# Implement partition and quick_sort using the pseudocode from lecture slides.
# Choose the pivot as the last element of the input array.
#
# Include comments on key lines of code (for, while, if, etc.) to demonstrate
# your comprehension of the implementation.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def quick_sort(input_list):
    return ...


# function header for Q1.2 (Manual grading)
# Sort 1000 randomly generated integers and print the running time.
# Generate input using np.random.randint(0, 1000, 1000).
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_2():
    input = np.random.randint(0, 1000, 1000)
    ''' write your answers (codes/texts) from here '''




    ''' end your answers '''


# function header for Q1.3 (Manual grading)
# Sort 1000 integers in ascending order and print the running time.
# Generate input using np.arange(0, 1000).
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_3():
    input = np.arange(0, 1000)
    ''' write your answers (codes/texts) from here '''




    ''' end your answers '''


# function header for Q1.4 (Manual grading)
# Sort 1000 integers in descending order and print the running time.
# Generate input using np.arange(1000, 0, -1).
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_4():
    input = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''




    ''' end your answers '''


# Q1.5:
# Explain why the running time of Q1-(3) and Q1-(4) is greater than Q1-(2).
# Write your explanation below as a Python comment
# {here...}


# function header for Q1.6 (Auto & manual grading)
# Implement modified_quick_sort to improve performance on sorted/reverse-sorted
# inputs. (e.g., use median-of-three or random pivot selection.)
# input_list -> list of integers
# return -> sorted list (ascending order)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
# < 10 points - autograding >
def modified_quick_sort(input_list):
    return ...


# Print the running time of ascending and descending inputs using
# modified_quick_sort.
# < 5 points - manual grading >
def q1_6():
    input_A = np.arange(0, 1000)
    input_B = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''




    ''' end your answers '''


# ============================================================================
# Q2. Stable Priority Sort
# ============================================================================
# function header for Q2 (Auto & manual grading)
# input -> 2D list, each row = [value, priority]
#          priority: 0 = high, 1 = medium, 2 = low
# return -> 2D list sorted by priority (high → medium → low),
#           preserving original relative order within each priority level
#
# Do NOT use Python built-in sorting functions.
#
# Ex: input  = [[6,0],[212,1],[247,0],[352,1],[388,1],[633,2],[694,0],[779,1],[793,2],[859,0]]
#     output = [[6,0],[247,0],[694,0],[859,0],[212,1],[352,1],[388,1],[779,1],[633,2],[793,2]]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def priority_sort(input):
    return ...


# ============================================================================
# Q3. Subset Sum
# ============================================================================
# function header for Q3 (Auto & manual grading)
# nums   -> list of non-negative integers, e.g., [3, 2, 10, 4, 8, 9]
# target -> integer (target sum), e.g., 12
# return -> bool (True if any subset sums to target, else False)
#
# Hint: Use a DP approach (top-down or bottom-up).
#
# Ex: nums=[3,2,10,4,8,9], target=12 → True
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def subset_sum(nums, target):
    return ...


# ============================================================================
# Q4. Minimum Cost Path
# ============================================================================
# Given a 2D cost matrix cost[i][j], find the minimum cost to reach the
# bottom-right cell from the top-left cell (0, 0).
# Movement allowed: right (i, j+1), down (i+1, j), or diagonal (i+1, j+1).
#
# Optimal substructure:
#   minCost(m, n) = min(minCost(m-1,n-1), minCost(m-1,n), minCost(m,n-1))
#                  + cost[m][n]

# function header for Q4.1 (Auto & manual grading)
# Naïve recursive approach (NOT DP). Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_naive(costs, m_minus_one, n_minus_one):
    return ...


# function header for Q4.2 (Auto & manual grading)
# Top-down DP (memoization). Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_top_down(costs, m_minus_one, n_minus_one):
    return ...


# function header for Q4.3 (Auto & manual grading)
# Bottom-up DP. Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_bottom_up(costs, m_minus_one, n_minus_one):
    return ...


# function header for Q4.4 (Manual grading — printed output evaluated)
# Reconstruct and print the minimum cost path, e.g., (0,0)->(0,1)->...
# Re-use min_cost_bottom_up inside this wrapper.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> N/C
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_path_wrapper(costs, m_minus_one, n_minus_one):
    pass


# ============================================================================
# Q5. Matrix-Chain Multiplication
# ============================================================================
# Given dimension array q where matrix A_i has dimensions q[i-1] x q[i],
# find the most efficient way to multiply the chain to minimize total scalar
# multiplications.
#
# Recurrence:
#   m[i,j] = 0                                                    if i == j
#   m[i,j] = min_{i<=k<j} { m[i,k] + m[k+1,j] + q[i-1]*q[k]*q[j] }  if i < j

# function header for Q5.1 (Auto & manual grading)
# Top-down DP (memoized recursion). Return the minimum scalar multiplications.
# q -> list of matrix dimensions
# i -> start matrix index (1-indexed)
# j -> end matrix index (1-indexed)
# return -> integer (minimum number of scalar multiplications)
#
# Ex: q=[9,46,4,18,21,40,19,25,14,37,33], i=1, j=10 → 21012
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_top_down(q, i, j):
    return ...


# function header for Q5.2 (Auto & manual grading)
# Bottom-up DP. Return TWO arrays as a tuple: the cost matrix m and the
# split index matrix s.
# q -> list of matrix dimensions
# return -> tuple (m, s)
#   m: 2D list where m[i][j] = min scalar multiplications for A_i..A_j
#   s: 2D list where s[i][j] = split index k that achieves m[i][j]
#
# Ex: q=[9,46,4,18,21,40,19,25,14,37,33] → m, s
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_bottom_up(q):
    return ...


# function header for Q5.3 (Auto & manual grading)
# Reconstruct the optimal full parenthesization as a string.
# Re-use matrix_chain_bottom_up inside this wrapper.
# q      -> list of matrix dimensions
# matrix -> list of matrix name strings, e.g., ['A1','A2',...,'A10']
# return -> string, e.g., "((A1A2A3)(A4A5))"
#
# Rules:
#   - Use '(' and ')' instead of '{' '}'
#   - Enclose the outermost product in parentheses
#   - No spaces between characters
#
# Ex: q=[9,46,4,18,21,40,19,25,14,37,33],
#     matrix=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_parenthesization(q, matrix):
    return ...


# ============================================================================
# Q6. Rod Cutting
# ============================================================================
# Given a rod of length n and price array p (p[i] = price for length i, p[0]=0),
# find the maximum revenue obtainable by cutting and selling the rod.
#
# Optimal substructure: r[n] = max_{1<=i<=n} (p[i] + r[n-i])

# function header for Q6.1 (Auto & manual grading)
# Top-down DP (memoized recursion). Return the maximum revenue for a rod of length n.
# p -> list, p[i] = price for rod of length i (p[0] = 0)
# n -> integer (rod length)
# return -> integer (maximum revenue)
#
# Ex: p=[0,1,5,8,9,10,17,17,20,24,30], n=4 → 10
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def rod_cut_top_down(p, n):
    return ...


# function header for Q6.2 (Auto & manual grading)
# Bottom-up DP. Return TWO arrays as a tuple: the revenue array r and
# the cuts array s.
# p -> list, p[i] = price for rod of length i (p[0] = 0)
# return -> tuple (r, s)
#   r: list where r[i] = max revenue for rod of length i
#   s: list where s[i] = size of the first cut for rod of length i
#
# Ex: p=[0,1,5,8,9,10,17,17,20,24,30] → r, s
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def rod_cut_bottom_up(p):
    return ...


# function header for Q6.3 (Auto & manual grading)
# Reconstruct and return the optimal list of cuts as a sorted Python list.
# Re-use rod_cut_bottom_up inside this wrapper.
# p -> list, p[i] = price for rod of length i (p[0] = 0)
# n -> integer (rod length)
# return -> sorted list of cut sizes
#
# Ex: p=[0,1,5,8,9,10,17,17,20,24,30], n=7 → [1, 6]
#     p=[0,1,5,8,9,10,17,17,20,24,30], n=5 → [2, 3]
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def rod_cut_reconstruct(p, n):
    return ...


# ============================================================================
# Q7. Slice, Sort, and Pick K-th
# ============================================================================
# function header for Q7 (Auto & manual grading)
# array    -> list of integers, e.g., [1, 5, 2, 6, 3, 7, 4]
# commands -> 2D list, each row = [i, j, k] (all 1-indexed)
# return   -> list of k-th elements, one per command
#
# For each command [i, j, k]:
#   1. Slice array from the i-th to j-th element (1-indexed, inclusive).
#   2. Sort the slice in ascending order (no built-in sort functions).
#   3. Return the k-th element (1-indexed) of the sorted slice.
#
# Ex: array=[1,5,2,6,3,7,4], commands=[[2,5,3],[4,4,1],[1,7,3]] → [5, 6, 3]
#
# Constraints:
#   1 <= len(array) <= 100,  1 <= array[i] <= 100
#   1 <= len(commands) <= 50
#   1 <= i <= j <= len(array),  1 <= k <= j-i+1
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def slice_sort_kth(array, commands):
    return ...


# ============================================================================
# Q8. Data Filtering and Sorting
# ============================================================================
# function header for Q8 (Auto & manual grading)
# data    -> 2D list, each row = [code, date, maximum, remain]
# ext     -> field name to filter on ("code", "date", "maximum", "remain")
# val_ext -> threshold; keep only rows where data[i][ext] < val_ext
# sort_by -> field name to sort the filtered result by (ascending)
# return  -> filtered and sorted 2D list
#
# Steps:
#   1. Filter: keep rows where data[i][ext] < val_ext.
#   2. Sort filtered rows by sort_by in ascending order.
#
# Ex: data=[[1,20300104,100,80],[2,20300804,847,37],[3,20300401,10,8]],
#     ext="date", val_ext=20300501, sort_by="remain"
#     → [[3,20300401,10,8],[1,20300104,100,80]]
#
# Constraints:
#   1 <= len(data) <= 500
#   ext and sort_by are each one of: "code", "date", "maximum", "remain"
#   No two rows share the same value for sort_by
#   At least one row always satisfies the filter condition
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <tool name or "None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def filter_and_sort(data, ext, val_ext, sort_by):
    return ...


# ============================================================================
# Main - Test Section
# ============================================================================
if __name__ == "__main__":
    # You can test your code here
    # This section will not be evaluated by Gradescope
    pass
