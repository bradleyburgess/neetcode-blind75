from collections import defaultdict


class Solution:
    @staticmethod
    def group_anagrams_sorted(words: list[str]) -> list[list[str]]:
        hash = defaultdict(list)
        for word in words:
            sorted_word = "".join(sorted(word))
            hash[sorted_word].append(word)
        return list(hash.values())

    @staticmethod
    def group_anagrams_char_count(words: list[str]) -> list[list[str]]:
        hash = defaultdict(list)
        for word in words:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord("a")] += 1
            key = tuple(key)
            hash[key].append(word)
        return list(hash.values())
