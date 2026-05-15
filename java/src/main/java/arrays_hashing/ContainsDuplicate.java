package arrays_hashing;

import java.util.HashMap;

public class ContainsDuplicate {
    public boolean solveBrute(int[] nums) {
        for (var startIndex = 0; startIndex < nums.length - 1; startIndex++) {
            for (var i = startIndex + 1; i < nums.length; i++) {
                if (nums[i] == nums[startIndex]) return true;
            }
        }
        return false;
    }

    public boolean solveHashMap(int[] nums) {
        var hashMap = new HashMap<Integer, Boolean>();
        for (int num : nums) {
            if (hashMap.containsKey(num)) return true;
            hashMap.put(num, true);
        }
        return false;
    }
}
