class Solution:
    from collections import defaultdict, Counter
    from collections import deque

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

    


        indexes = []

        word_count = len(words)
        word_len = len(words[0])
        major_window = word_count * word_len
        q = deque()
        left = 0

        wordCount = Counter(words)


        def splitStr(st, stsize: int) -> List[str]:
            chunks = []

            k = 0

            while k < len(st):
                chunks.append(st[k:k+stsize])
                k+=stsize
            return chunks

        for i in range(len(s)):
            q.append(s[i])

            if i-left +1> major_window:
                q.popleft()
                left+=1

            if i-left+1 == major_window:
                current = "".join(q)
                tempCount = Counter((splitStr(current, word_len)))

                if tempCount == wordCount:
                    indexes.append(left)

        return indexes
