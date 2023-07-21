// beginning of min heap implementation
class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = []

    def parent(self, i):
        return (i) // 2

    def left_child(self, i):
        return 2 * i 

    def right_child(self, i):
        return 2 * i + 1

    def has_parent(self, i):
        return self.parent(i) >= 0

    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while self.has_parent(i) and self.heap[i] < self.heap[self.parent(i)]:
            parent_index = self.parent(i)
            self.swap(i, parent_index)
            i = parent_index

    def heapify_down(self, i):
        while self.has_left_child(i):
            min_child_index = self.left_child(i)
            if self.has_right_child(i) and self.heap[self.right_child(i)] < self.heap[min_child_index]:
                min_child_index = self.right_child(i)

            if self.heap[i] < self.heap[min_child_index]:
                break

            self.swap(i, min_child_index)
            i = min_child_index

    def insert(self, element):
        if self.size >= self.maxsize :
            print("hi")
            return
        self.heap.append(element)
  
        current = self.size
  
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        self.size+= 1

    def get_min(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def remove_min(self):
        if not self.heap:
            raise IndexError("Heap is empty.")

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if self.heap:
            self.heap[0] = last_value
            self.heapify_down(0)

        return min_value

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def heapify(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self.heapify_down(i)

# Example Usage
min_heap = MinHeap(10)
min_heap.insert(5)
min_heap.insert(8)
min_heap.insert(3)
min_heap.insert(10)
min_heap.insert(2)

print(min_heap.get_min())  # Output: 2

min_heap.remove_min()
print(min_heap.get_min())  # Output: 3

print(min_heap.is_empty())  # Output: False

