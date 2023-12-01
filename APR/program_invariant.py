
import numpy as np

def calculate_sum(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum


my_arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr_sum = calculate_sum(my_arr)

print("-------------------------------------------------")
print(arr_sum)

print("-------------------------------------------------")

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1



my_sec_arr = np.array([1,2,3,4,5,6,7,8,9,10])
my_target = 5

search_target = binary_search(my_sec_arr, my_target)


print(search_target)


print("-------------------------------------------------")



print("============variant with linked datastructures=================")

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def reverse_linked_list(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev