import heapq
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(char_freq):
    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]
def assign_codes(node, code='', huffman_code={}):
    if node:
        if node.char:
            huffman_code[node.char] = code
        assign_codes(node.left, code + '0', huffman_code)
        assign_codes(node.right, code + '1', huffman_code)
    return huffman_code
def huffman_encoding(char_freq):
    root = build_huffman_tree(char_freq)
    return assign_codes(root)
char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13}
huffman_codes = huffman_encoding(char_freq)
print(f"Huffman Codes = {huffman_codes}")