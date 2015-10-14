
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = '' if numerator * denominator >= 0 else '-'
        n, d = abs(numerator), abs(denominator)
        head, remainder = divmod(n, d)
        tail, seen = '', {}
        while remainder != 0:
            if remainder in seen:
                x = seen[remainder]
                tail = "{}({})".format(tail[:x], tail[x:])
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder*10, d)
            tail += str(digit)
        return sign + str(head) + (tail and '.' + tail)


def main():
    test = [
        (1, 2, "0.5"),
        (2, 1, "2"),
        (2, 3, "0.(6)"),
        (1, 7, "0.(142857)")
    ]
    s = Solution()
    for (n, d, a) in test:
        b = s.fractionToDecimal(n, d)
        print(a == b, a, b)


if __name__ == "__main__":
    main()
