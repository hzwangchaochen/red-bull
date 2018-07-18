import heapq


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topk_frequent_words(self, words, k):
        # write your code here
        heap = []
        fre_map = {}
        for word in words:
            if word in fre_map:
                fre_map[word] += 1
            else:
                fre_map[word] = 1
        for word, freq in fre_map.items():
            heapq.heappush(heap, (-freq, word))
        res = []
        for i in range(0, k):
            res.append(heapq.heappop(heap)[1])
        return res


if __name__ == '__main__':
    solution = Solution()
    words = ["yes", "lint", "code", "yes", "code", "baby", "you", \
             "baby", "chrome", "safari", "lint", "code", "body", "lint", "code"]
    print(solution.topk_frequent_words(words, 3))
