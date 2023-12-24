"""
문자열의 모든 부분집합 찾기

시간복잡도 O(2^(n-1))
"""

def find_combinations(s, substring=[]):
    if not s:
        combs.update(substring)
        return

    for i in range(len(s)):
        substring.append(s[:i+1])
        find_combinations(s[i+1:], substring)
        substring.pop()

if __name__ == "__main__":
    s = "abcd"

    combs = set()
    find_combinations(s)
    print()
    subs = sorted(combs, key=lambda x: (len(x), x))
    print(subs)
