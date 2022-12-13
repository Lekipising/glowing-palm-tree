
def main():
    n, m, s = map(int, input().split())
    if m <= (n - 1) * (n - 2) // 2 + 1:
        print(m + s - n + 1)
    else:
        s -= n - 1
        e = m - (n - 1) * (n - 2) // 2
        mnc = (s + n - 2) // (n - 1)
        ans = 1e42
        s -= mnc
        # first loop: loop through all possible values of A
        for A in [0, s // (n - 2), s // (n - 2) - 1]:
            # second loop: loop through all possible values of B
            for B in [0, n - 3, (s - A * (n - 2)) % (n - 2)]:
                x = A * (n - 2) + B
                if 0 <= x <= s:
                    ans = min(ans, (s - x + mnc) * e + (n - 1) * (n - 2) //
                              2 * A + B * (B - 1) // 2 + B * (n - B - 1))

        print(ans + m)


# pseduo code:
# 1. Read in the values for n, m, and s from the input
# 2. If m is less than or equal to the maximum number of edges that can be added without creating a cycle, print m + s - n + 1 and return
# 3. Otherwise, subtract n - 1 from s, and calculate e as the difference between m and the maximum number of edges without creating a cycle
# 4. Calculate mnc as the minimum number of edges needed to create a cycle, using the formula (s + n - 2) // (n - 1)
# 5. Set ans to a very large value
# 6. Subtract mnc from s
# 7. For each possible value of A in the set {0, s // (n - 2), s // (n - 2) - 1}:
#     8. For each possible value of B in the set {0, n - 3, (s - A * (n - 2)) % (n - 2)}:
#         9. Calculate x as the product of A and (n - 2) plus B
#         10. If x is between 0 and s (inclusive), update ans to the minimum of its current value and the product of (s - x + mnc) and e plus the product of (n - 1) and (n - 2) divided by 2 and A plus the product of B and (B - 1) divided by 2 plus the product of B and (n - B - 1)
# 11. Print the sum of ans and m

# overall equation for running time:
# T = O(n^2)


if __name__ == '__main__':
    main()
