package arrays_hashing;

import java.util.HashMap;

public class ValidAnagram {
    public boolean solveHashmap(String input1, String input2) {
        input1 = input1.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        input2 = input2.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        if (input1.length() != input2.length()) return false;
        var hash1 = new HashMap<Character, Integer>();
        var hash2 = new HashMap<Character, Integer>();
        for (int i = 0; i < input1.length(); i++) {
            var char1 = input1.charAt(i);
            var char2 = input2.charAt(i);
            if (!hash1.containsKey(char1))
                hash1.put(char1, 0);
            if (!hash2.containsKey(char2))
                hash2.put(char2, 0);
            hash1.put(char1, hash1.get(char1) + 1);
            hash2.put(char2, hash2.get(char2) + 1);
        }
        return hash1.equals(hash2);
    }

    public boolean solveHashmapOptimized(String input1, String input2) {
        input1 = input1.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        input2 = input2.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        if (input1.length() != input2.length()) return false;
        var hash = new HashMap<Character, Integer>();
        for (int i = 0; i < input1.length(); i++) {
            var char1 = input1.charAt(i);
            var char2 = input2.charAt(i);
            hash.put(char1, hash.getOrDefault(char1, 0) + 1);
            hash.put(char2, hash.getOrDefault(char2, 0) - 1);
        }

        for (char character : hash.keySet()) {
            if (hash.get(character) != 0) return false;
        }
        return true;
    }

//    public boolean solveSorted(String input1, String input2) {
//
//    }
}
