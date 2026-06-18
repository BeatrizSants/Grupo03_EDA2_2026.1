class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, score, recipe_id, recipe_data=None):
        self.heap.append((score, recipe_id, recipe_data))
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        max_item = self.heap.pop()
        
        if self.heap:
            self._sift_down(0)
            
        return max_item

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx][0] > self.heap[parent][0]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != idx:
            self._swap(idx, largest)
            self._sift_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __len__(self):
        return len(self.heap)