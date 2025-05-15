from collections import Counter, defaultdict


class Solution:
    @staticmethod
    def minimum_window_brute(s: str, t: str) -> str:
        left = 0
        t_chars = Counter(t)

        result = ""

        for right in range(len(s)):
            s_chars = Counter(s[left : right + 1])
            is_result = all(
                char in s_chars and s_chars[char] >= count
                for char, count in t_chars.items()
            )
            while left <= right and is_result:
                _result = s[left : right + 1]
                if len(result) == 0 or len(_result) < len(result):
                    result = _result
                current = s[left]
                if current not in t_chars or s_chars[current] > t_chars[current]:
                    left += 1
                    s_chars[current] -= 1
                else:
                    is_result = False
        return result

    @staticmethod
    def minimum_window_brute_optimized(s: str, t: str) -> str:
        result = ""
        left = 0
        t_chars = Counter(t)
        s_chars = defaultdict(int)
        result = ""

        for right in range(len(s)):
            current = s[right]
            s_chars[current] += 1
            must_shift_right = False
            for char, count in t_chars.items():
                if s_chars[char] < count:
                    must_shift_right = True
                    print(f"Not enough {char}")
                    break
            if must_shift_right:
                continue
            while s_chars[s[left]] > t_chars[s[left]]:
                s_chars[s[left]] -= 1
                left += 1
            _result = s[left : right + 1]
            if len(result) == 0 or len(_result) < len(result):
                result = _result
        return result
    
    @staticmethod
    def minimum_window_have_need(s: str, t: str) -> str:
        result = ""
        t_chars = Counter(t)
        s_chars = defaultdict(int)
        have, need = 0, t_chars.total()
        left = 0

        for right in range(len(s)):
            current = s[right]
            s_chars[current] += 1
            if current in t_chars and s_chars[current] <= t_chars[current]:
                have += 1
            while have == need:
                _result = s[left:right + 1]
                print(f"Found a result: {_result}")
                if len(result) == 0 or len(_result) < len(result):
                    result = _result
                s_chars[s[left]] -= 1
                if s[left] in t_chars and t_chars[s[left]] > s_chars[s[left]]:
                    have -= 1
                left += 1
            
        return result