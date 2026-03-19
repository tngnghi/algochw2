# Do not change the filename or function headers
# You are free to add helper functions
# note: you will only have 5 attempts to run the autograder

import sys
import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

sys.setrecursionlimit(2000)

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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def partition(A, p, r):
    #chosing last index of list (in this iteration) to be pivot
    x = A[r]
    i = p-1
    #loop to compare with the rest element in this iteration, find the appropiate place of pivot
    for j in range(p, r):
        if A[j] <= x:
            i=i+1
            A[i], A[j] = A[j], A[i]
    #then put pivot at its place 
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quick(input_list, p, r):
    #recursively partion if the start index is larger than (or at least equalt to) the end index
    if p < r:
        q = partition(input_list, p, r)
        #apply quick for each part after partition
        quick(input_list, p, q-1)
        quick(input_list, q+1, r)
    return input_list

def quick_sort(input_list):
    # use helper function to track the index of each iteration easier
    return quick(input_list, 0, len(input_list) -1)


# function header for Q1.2 (Manual grading)
# Sort 1000 randomly generated integers and print the running time.
# Generate input using np.random.randint(0, 1000, 1000).
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_2():
    input = np.random.randint(0, 1000, 1000)
    ''' write your answers (codes/texts) from here '''
    start = timer()
    quick_sort(input)
    end = timer()
    print(f"Sort 1000 randomly generated integers and print the running time: {end-start}.")
    ''' end your answers '''


# function header for Q1.3 (Manual grading)
# Sort 1000 integers in ascending order and print the running time.
# Generate input using np.arange(0, 1000).
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_3():
    input = np.arange(0, 1000)
    ''' write your answers (codes/texts) from here '''
    start = timer()
    quick_sort(input)
    end = timer()
    print(f"Sort 1000 integers in ascending order and print the running time: {end-start}")
    ''' end your answers '''


# function header for Q1.4 (Manual grading)
# Sort 1000 integers in descending order and print the running time.
# Generate input using np.arange(1000, 0, -1).
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def q1_4():
    input = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''
    start = timer()
    quick_sort(input)
    end = timer()
    print(f"Sort 1000 integers in descending order and print the running time: {end-start}")
    ''' end your answers '''


# Q1.5:
# Explain why the running time of Q1-(3) and Q1-(4) is greater than Q1-(2).
# Write your explanation below as a Python comment
# {since quick_sort work as an divide-and-conquer algorithm, is the sequence is either descending or ascending, 
# quick-sort has to go through every items, and partition right at the front or end of the list, which will create more partition in between.
# However, with random sequences, partition can be the middle index, hence lessen the time that partition function iterates}


# function header for Q1.6 (Auto & manual grading)
# Implement modified_quick_sort to improve performance on sorted/reverse-sorted
# inputs. (e.g., use median-of-three or random pivot selection.)
# input_list -> list of integers
# return -> sorted list (ascending order)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
# < 10 points - autograding >
def modified_partition(A, p, r):
    #choose pivot as the middle, instead of the end, to make runtime into nlogn instead of n^2
    x = A[(p+r)//2]
    #the rest have similar strategy of approaching as the first edition
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i=i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1
def modified_quick(input_list,p,r):
    if p < r:
        q = modified_partition(input_list, p, r)
        modified_quick(input_list, p, q-1)
        modified_quick(input_list, q+1, r)
    return input_list

def modified_quick_sort(input_list):
    return modified_quick(input_list, 0, len(input_list) -1)


# Print the running time of ascending and descending inputs using
# modified_quick_sort.
# < 5 points - manual grading >
def q1_6():
    input_A = np.arange(0, 1000)
    input_B = np.arange(1000, 0, -1)
    ''' write your answers (codes/texts) from here '''
    start = timer()
    modified_quick_sort(input_A)
    end = timer()
    print(f"Sort 1000 integers in asscending order and print the running time: {end-start}")

    start = timer()
    modified_quick_sort(input_B)
    end = timer()
    print(f"Sort 1000 integers in descending order and print the running time: {end-start}")
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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def priority_sort(input):
    for i in range(1,len(input)):
        for j in range(0,len(input)-1):
            #approach priority first, comparing, then swap the to their right place
            if input[i][1] < input[j][1]:
                input[j], input[i] = input[i], input[j]
            # then approach value, comparing, then swap the to their right place
            if input[i][1] == input[j][1] and input[i][0] < input[j][0]:
                input[j], input[i] = input[i], input[j]
    return input


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def checked_subset(nums, a, b, target):
    #base case for recursive
    if nums[a] == target: return True
    #one more base case: loop in range of the subset, check sums of 2 elements
    for i in range(a+1,b+1):
        if nums[a] + nums[i] == target : return True
    #if haven't found the target, let nums[a] be an addend to find the target by summing
    target -= nums[a]
    #recursively check the subset from a+1 to b
    if a+1 <= b and target > 0: return checked_subset(nums, a+1, b, target)
    
    return False
    
def subset_sum(nums, target):
    #loop and check all continuous subsets of nums
    for j in range(0, len(nums)-1):
        return checked_subset(nums,j,len(nums)-1, target)


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_naive(costs, m_minus_one, n_minus_one):
    # base case: can't apply the formulat with the start cell
    if m_minus_one == 0 and n_minus_one ==0:
        return costs[0][0]
    # mamking sure m_minus_one, n_minus_one are both non-negative
    if m_minus_one>=0 and n_minus_one>=0:
        #if m or n is 0, it is at edge, hence the calculation based on the previous edge cell only
        if m_minus_one == 0:
            return min_cost_naive(costs,0,n_minus_one-1)+costs[m_minus_one][n_minus_one]
        if n_minus_one == 0:
            return min_cost_naive(costs,m_minus_one-1,0)+costs[m_minus_one][n_minus_one]
        # apply formula regularly
        return min(min_cost_naive(costs, m_minus_one-1,n_minus_one-1), min_cost_naive(costs, m_minus_one-1,n_minus_one), min_cost_naive(costs, m_minus_one,n_minus_one-1)) + costs[m_minus_one][n_minus_one]
    return []

# function header for Q4.2 (Auto & manual grading)
# Top-down DP (memoization). Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def find_and_store_min(costs, min_costs, m_minus_one, n_minus_one):
    q=None
    #since we can access the stored array, if it exist, return the value instead of calculating again
    if min_costs[m_minus_one][n_minus_one] >= np.min(costs):
        return min_costs[m_minus_one][n_minus_one]
    #cell is at start
    if m_minus_one == 0 and n_minus_one ==0:
        q = costs[0][0]
    #cell is on edge
    if m_minus_one == 0 and n_minus_one>0:
        q = find_and_store_min(costs,min_costs,0,n_minus_one-1)+costs[m_minus_one][n_minus_one]
    if n_minus_one == 0 and m_minus_one>0:
        q = find_and_store_min(costs,min_costs,m_minus_one-1,0)+costs[m_minus_one][n_minus_one]
    #otherwise, apply formula regularly
    elif n_minus_one > 0 and m_minus_one>0:
        q = min(find_and_store_min(costs,min_costs, m_minus_one, n_minus_one-1), find_and_store_min(costs,min_costs, m_minus_one-1, n_minus_one), find_and_store_min(costs,min_costs, m_minus_one-1, n_minus_one-1)) + costs[m_minus_one][n_minus_one]
    #store calculated value in the array
    min_costs[m_minus_one][n_minus_one] = q
    return q
    
def min_cost_top_down(costs, m_minus_one, n_minus_one):
    if m_minus_one>=0 and n_minus_one>=0:
        min_costs = [[-float('inf') for _ in range(m_minus_one+1)] for _ in range(n_minus_one+1)]
        #recursively calculate min costs, while also searching for stored value and access it for calculation
        return find_and_store_min(costs, min_costs, m_minus_one, n_minus_one)
    return []


# function header for Q4.3 (Auto & manual grading)
# Bottom-up DP. Return the minimum cost and print running time.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> integer (minimum cost)
#
# Include comments on key lines of code to demonstrate your comprehension.
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_bottom_up(costs, m_minus_one, n_minus_one):
    if m_minus_one>=0 and n_minus_one>=0:
        min_costs = costs
        #min cost of edge case is sum of previous case from the same edge
        for i in range(1,m_minus_one+1):
            min_costs[i][0] += min_costs[i-1][0]
        for j in range(1,n_minus_one+1):
            min_costs[0][j] += min_costs[0][j-1]
        #after solving special cases, apply formula to the rest
        for i in range(1,m_minus_one+1):
            for j in range(1,n_minus_one+1):
                min_costs[i][j] += min(min_costs[i-1][j], min_costs[i][j-1], min_costs[i-1][j-1])
        return min_costs[m_minus_one][n_minus_one]
    return []


# function header for Q4.4 (Manual grading — printed output evaluated)
# Reconstruct and print the minimum cost path, e.g., (0,0)->(0,1)->...
# Re-use min_cost_bottom_up inside this wrapper.
# costs       -> list of lists (2D cost array)
# m_minus_one -> row index of destination (M-1)
# n_minus_one -> col index of destination (N-1)
# return      -> N/C
#
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def min_cost_path_wrapper(costs, m_minus_one, n_minus_one):
    #we already have the min cost, however the path is unknown
    min_cost = min_cost_bottom_up(costs,m_minus_one,n_minus_one)
    m=m_minus_one
    n=n_minus_one
    min_cost_index = [[m,n]]
    #find the path by continuosly deduct the min of the closest cells(above the destination) from the min cost
    while m > 0 and n > 0:
        temp_min= min(costs[m-1][n], costs[m][n-1],costs[m-1][n-1])
        if temp_min == costs[m-1][n]:
            m = m-1
        if temp_min == costs[m][n-1]:
            n=n-1
        if temp_min == costs[m-1][n-1]:
            n=n-1
            m=m-1
        min_cost -= temp_min
        #insert the indexes at the front, because they are the cells above the destination
        min_cost_index = np.insert(min_cost_index, 0, [m,n], axis=0)
    #eventually insert the start's index at front
    min_cost_index = np.insert(min_cost_index, 0, [0,0], axis=0)
    #print out the list
    for i in range(len(min_cost_index)):
        print(f"({min_cost_index[i][0]},{min_cost_index[i][1]})", end ='')
        if i < len(min_cost_index)-1:
            print(f"->", end ='')
        else: print(".")
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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def top_down_mult(q,m,i,j):
    # base case i=j
    if i == j:
        m[i][j] = 0
        return 0
    #check if memorize array of the index is previously initialized
    if m[i][j] >=0:
        return m[i][j]
    else:
        #recursively check multiplication
        min_mult = top_down_mult(q,m,i+1,j) + q[i-1]*q[i]*q[j]
        p = min_mult
        for k in range(i+1,j):
            p = top_down_mult(q,m,i,k) + top_down_mult(q,m,k+1,j) + q[i-1]*q[k]*q[j]
            if min_mult > p:
                min_mult = p
        #assign found minimum multiplication to memorized array
        m[i][j]=min_mult
    return min_mult

def matrix_chain_top_down(q, i, j):
    m = [[-float("inf") for _ in range(j+1)]for _ in range(j+1)]
    return top_down_mult(q,m,i,j)


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_bottom_up(q):
    m = [[float('inf') for _ in range(len(q))] for _ in range(len(q))]
    s = [[float('inf') for _ in range(len(q))] for _ in range(len(q))]
    #since the multiplication of closer indexes are easier to find, approach them first by looping distance, not index
    for n in range(0, len(q)-1):
        #then initualize first index, and calculate second index based on distance
        for i in range(1, len(q)-n):
            #distance = 0 <=> index i=j
            if n == 0:
                m[i][i]=0
            else:
                #repeatedly calculate and compare to find the min
                min = m[i+1][i+n] + q[i-1]*q[i]*q[i+n]
                s[i][i+n] = i
                for k in range(i+1,i+n):
                    temp = m[i][k] + m[k+1][i+n] + q[i-1]*q[k]*q[i+n]
                    if min > temp:
                        min = temp
                        #if a new min is assigned, update split index
                        s[i][i+n] = k
                #update min
                m[i][i+n] = min

    return tuple([m, s])


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def matrix_chain_parenthesization(q, matrix):
    # found list of min scalar multiplications and split index, access it at the rith index to find k
    if len(matrix) == 1:
        return f"{matrix[0]}"
    k = matrix_chain_bottom_up(q)[1][len(q)-1]
    q_1 = q[:k+1]
    q_2 = q[k:]
    matrix_1 = matrix[:k]
    matrix_2 = matrix[k:]
    #recursively run the function to return the split matrix chain
    if len(matrix_1) == 2:
        return f"(({matrix_1[0]}{matrix_1[1]}){matrix_chain_parenthesization(q_2, matrix_2)})"
    if len(matrix_2) == 2:
        return f"({matrix_chain_parenthesization(q_1, matrix_1)}({matrix_2[0]}{matrix_2[1]}))"
    return f"({matrix_chain_parenthesization(q_1, matrix_1)}{matrix_chain_parenthesization(q_2, matrix_2)})"


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def saved_rod_cut(p,n,r):
    #find saved max revenue
    if r[n] >= 0:
        return r[n]
    #base case length = 0
    if n == 0:
        q = 0
    else:
        #find max of the revenue of cutting, by combining price of different length and saved revenue of remaining
        q = -float('inf')
        for i in range(1,n+1):
            q= max(q,p[i] + saved_rod_cut(p,n-i,r))
    r[n] = q
    return q
def rod_cut_top_down(p, n):
    r = [-float('inf')] * (n+1)
    return saved_rod_cut(p,n,r)


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def rod_cut_bottom_up(p):
    # initialize both list with 0, hence base case is already = 0, continue with index at 1
    r = [0]*len(p)
    s = [0]*len(p)
    for j in range(1,len(p)):
        q = -float('inf')
        # find the max revenue
        for i in range(1,j+1):
            temp= p[i] + r[j-i]
            if q < temp:
                q = temp
                s[j] = i
        r[j] = q
    return tuple([r,s])


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def rod_cut_reconstruct(p, n):
    arr = []
    #let length l = remaining length of the rod after cut
    l = n
    while l > 0:
        #append arr with result from the previous function, accessing its list using indexing 1: list of splits,
        # at index of length l
        arr.append(rod_cut_bottom_up(p)[1][l])
        #decrease l by the known split
        l -= arr[-1]
    # use sorted to return the length of split rod, after all splits
    return sorted(arr)


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def slice_sort_kth(array, commands):
    element = []
    for i in range(len(commands)):
        # use all in one line:
        # firstly find the subset, sort the subset, then find the value of index in that sorted subset
        #finally append the result to llist element
        element.append(sorted(array[commands[i][0] -1 : commands[i][1]])[commands[i][2]-1])
    return element


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
# AI Tool Used: <"None">
# Interaction: <description of how the AI tool was used, e.g., prompts given>
# Verification: <how you verified the correctness of the AI-generated code>
def filter_and_sort(data, ext, val_ext, sort_by):
    new_data = []
    field = ["code","date","maximum","remain"]
    #assign "ext" and "sort_by" as number to access indexes easier
    for f in range(4):
        if ext == field[f]:
            ext = f
        if sort_by == field[f]:
            sort_by = f
    #then find the data with suitable value
    for i in range(len(data)):
        if data[i][ext] < val_ext:
            new_data.append(data[i])
    #return the sorted data, by "sort_by"
    return sorted(new_data, key = lambda data: data[sort_by])


# ============================================================================
# Main - Test Section
# ============================================================================
if __name__ == "__main__":
    # You can test your code here
    # This section will not be evaluated by Gradescope
    """A = [1,3,2,6,4,5]
    print(quick_sort(A))
    q1_2()
    q1_3()
    q1_4()
    q1_6()

    A2 = [[6,0],[212,1],[247,0],[352,1],[388,1],[633,2],[694,0],[779,1],[793,2],[859,0]]
    print(f"List is sorted into: {priority_sort(A2)}")

    A3 = [3,2,10,4,8,9]
    print(subset_sum(A3, 5))
    print(subset_sum(A3, 12))
    print(subset_sum(A3, 15))
    print(subset_sum(A3, 9))
    print(subset_sum(A3, 1))

    #A4 = [[2,2,3],[3,7,1],[4,6,4]]
    #print(min_cost_naive(A4,len(A4)-1,len(A4[0])-1))
    #print(min_cost_top_down(A4,len(A4)-1,len(A4[0])-1))
    #print(min_cost_bottom_up(A4,len(A4)-1,len(A4[0])-1))
    #print(min_cost_path_wrapper(A4,len(A4)-1,len(A4[0])-1))

    A5 = [9,46,4,18,21,40,19,25,14,37,33]
    #print(matrix_chain_bottom_up(A5))
    matrix=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']
    print(matrix_chain_parenthesization(A5,matrix))

    A6 = [0,1,5,8,9,10,17,17,20,24,30]
    print(rod_cut_bottom_up(A6))
    for i in range(len(A6)):
        print(rod_cut_reconstruct(A6,i))

    array=[1,5,2,6,3,7,4]
    commands=[[2,5,3],[4,4,1],[1,7,3]]
    print(slice_sort_kth(array, commands))

    data = [[1, 20300104, 100, 80],
            [2, 20300804, 847, 37],
            [3, 20300401, 10, 8]]
    ext = "date"
    val_ext = 20300501
    sort_by = "remain"
    print(filter_and_sort(data,ext,val_ext,sort_by))"""
    pass
