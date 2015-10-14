#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
    public:
        string fractionToDecimal(int numerator, int denominator) {
            if (!numerator) return "0";
            string sign = (numerator < 0 ^ denominator < 0) ? "-" : "";
            long numer = numerator < 0 ? (long)numerator * (-1) : (long)numerator;
            long denom = denominator < 0 ? (long)denominator * (-1) : (long)denominator;
            long head = numer / denom;
            long remainder = numer % denom;
            string tail = "";
            unordered_map<long, long> seen;
            while (remainder != 0) {
                if(seen.find(remainder) != seen.end()) {
                    tail.insert(seen[remainder], 1, '(');
                    tail += ')';
                    break;
                }
                seen[remainder] = tail.size();
                long digit = remainder*10 / denom;
                remainder = remainder*10 % denom;
                tail += to_string(digit);
            }
            string res = sign + to_string(head);
            return tail.empty() ? res : res + "." + tail;
        }
};

int main()
{
    int input[6][2] = {{1, 2}, {2, 1}, {2, 3}, {1, 7}, {-2147483648, 1},
        {-1, -2147483648}};
    string output[6] = {"0.5", "2", "0.(6)", "0.(142857)", "-2147483648",
        "0.0000000004656612873077392578125"};
    int n, d;
    string a;
    Solution s;
    for (int i = 0; i < 6; ++i) {
        n = input[i][0];
        d = input[i][1];
        a = output[i];
        cout << n << '\t' << d << '\t' << '\t' << a << '\t';
        cout << s.fractionToDecimal(n, d) << endl;
    }
}
