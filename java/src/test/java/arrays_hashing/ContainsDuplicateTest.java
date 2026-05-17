package arrays_hashing;

import base.BaseSolutionTest;
import base.TestCase;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

public class ContainsDuplicateTest
    extends BaseSolutionTest<ContainsDuplicate, int[], Boolean> {

    @Override
    protected ContainsDuplicate createSolution() {
        return new ContainsDuplicate();
    }

    @Override
    protected String jsonKey() {
        return "01_contains_duplicate";
    }

    @Override
    protected Object[] buildArgumentsFromInput(int[] ints) {
        return new Object[]{ints};
    }

    @Override
    protected TestCase<int[], Boolean> buildTestCaseFromNode(JsonNode node) {
        try {
            return new TestCase<>(
                objectMapper.treeToValue(node.get("input"), int[].class),
                node.get("expected").asBoolean()
            );
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }
}
