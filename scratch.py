import unittest
import random
import time

# Merge sort implementation I took from online
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    if any(isinstance(item, str) for item in arr):
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


class test_sort(unittest.TestCase):
    def test_positive(self):
        arr = [38, 27, 43, 3, 9, 82, 10]
        self.assertEqual(merge_sort(arr), [3, 9, 10, 27, 38, 43, 82])

    def test_negative(self):
        arr = ["Hello,", "World"];
        self.assertEqual(merge_sort(arr), arr)

    def test_speed(self):
        arr = [random.randint(0, 1000) for _ in range(100)]
        start_time = time.time()
        sorted_arr = merge_sort(arr)
        end_time = time.time()
        time_taken = end_time - start_time

        self.assertLess(time_taken, 0.01)

    def test_edge(self):
        arr = []
        self.assertEqual(merge_sort(arr), [])
    
    def test_repeatability(self):
        arr = [1, 2, 3]
        self.assertEqual(merge_sort(arr), arr)

        arr = [10, 5, 7, 3, 1]
        self.assertEqual(merge_sort(arr), [1, 3, 5, 7, 10])

        arr = [10, 5, 7, 3, 1]
        self.assertEqual(merge_sort(arr), [1, 3, 5, 7, 10])

        arr = [10, 5, 7, 3, 1]
        self.assertEqual(merge_sort(arr), [1, 3, 5, 7, 10])


if __name__ == '__main__':
    unittest.main()

#sorted_arr = merge_sort(arr)
#print("Sorted array:", sorted_arr)
