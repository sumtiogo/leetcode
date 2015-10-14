
class Solution(object):

    def minDistance(self, word1, word2):
        """
        O(mn), O(n)
        """
        m, n = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in xrange(n)]
        for j in xrange(n):
            pre[j] = j
        for i in xrange(1, m):
            cur = [i]*n
            for j in xrange(1, n):
                if word1[i-1] == word2[j-1]:
                    cur[j] = pre[j-1]
                else:
                    cur[j] = min(pre[j]+1,
                                 cur[j-1]+1,
                                 pre[j-1]+1)
            pre = cur[:]
        return pre[n-1]

    def minDistance2(self, word1, word2):
        """
        O(mn), O(mn)
        """
        m = len(word1) + 1
        n = len(word2) + 1
        d = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            d[i][0] = i
        for j in xrange(n):
            d[0][j] = j
        for i in xrange(1, m):
            for j in xrange(1, n):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j] + 1,  # deltetion
                                  d[i][j-1] + 1,  # insertion
                                  d[i-1][j-1] + 1) # substitution
        return d[m-1][n-1]

    def minDistance1(self, word1, word2):
        """
        T(i, j) = T(i-1, j) + T(i, j-1) + T(i-1, j-1) + 1
        O(3^{i+j-1})
        """
        def lev(i, j):
            if i == 0 or j == 0:
                return i + j
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            return min(
                lev(i - 1, j) + 1,
                lev(i, j - 1) + 1,
                lev(i - 1, j - 1) + cost)
        return lev(len(word1), len(word2))


def main():
    test = [
        ("cat", "at", 1),
        ("kitten", "sitting", 3)
    ]
    s = Solution()
    for w1, w2, ans in test:
        t = s.minDistance(w1, w2)
        print(w1, w2, ans, t, t == ans)


if __name__ == "__main__":
    main()
