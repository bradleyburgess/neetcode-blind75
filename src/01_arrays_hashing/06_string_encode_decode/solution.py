from typing import List
import json


class Solution:
    class Json:
        @staticmethod
        def encode(strs: List[str]) -> str:
            return json.dumps(strs)

        @staticmethod
        def decode(s: str) -> List[str]:
            return json.loads(s)

    class LengthDelimited:
        @staticmethod
        def encode(strs: List[str]) -> str:
            return "".join(map(lambda s: f"{len(s)}#{s}", strs))

        @staticmethod
        def decode(s: str) -> List[str]:
            result = []
            i = 0
            while i < len(s):
                j = i
                while s[j] != "#":
                    j += 1
                length = int(s[i:j])
                result.append(s[j + 1 : j + 1 + length])
                i = j + length + 1
            return result
