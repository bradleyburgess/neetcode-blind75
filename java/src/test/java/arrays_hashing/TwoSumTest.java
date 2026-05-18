package arrays_hashing;

import base.BaseSolutionTest;
import base.TestCase;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

public class TwoSumTest extends BaseSolutionTest<TwoSum, TestInput, int[]> {
    @Override
    protected TwoSum createSolution() {
        return new TwoSum();
    }

    @Override
    protected String jsonKey() {
        return "03_two_sum";
    }

    @Override
    protected Object[] buildArgumentsFromInput(TestInput testInput) {
        return new Object[]{testInput.nums(), testInput.target()};
    }

    @Override
    protected TestCase<TestInput, int[]> buildTestCaseFromNode(JsonNode input, JsonNode expected) throws JsonProcessingException {
        var nums = objectMapper.treeToValue(input.get(0), int[].class);
        var target = input.get(1).asInt();
        return new TestCase<>(
            new TestInput(nums, target),
            objectMapper.treeToValue(expected, int[].class)
        );
    }
}

record TestInput(
    int[] nums,
    int target
) {
}
