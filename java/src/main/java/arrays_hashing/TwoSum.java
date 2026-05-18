package arrays_hashing;

import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {
    public int[] solveBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) return new int[]{i, j};
            }
        }
        return new int[0];
    }

    public int[] solveHashmap(int[] nums, int target) {
        var hash = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hash.containsKey(complement)) {
                var result = new int[]{i, hash.get(complement)};
                Arrays.sort(result);
                return result;
            }
            hash.put(nums[i], i);
        }
        return new int[0];
    }
}
