class ArrayDeque:
    def __init__(self):
        self._data = []

    def add_first(self, item):
        self._data.insert(0, item)

    def add_last(self, item):
        self._data.append(item)

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._data.pop(0)

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

def lvp(s):
    stack = []
    max_len = 0
    last_invalid = -1
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    max_len = max(max_len, i - last_invalid)
            else:
                last_invalid = i
    return max_len
