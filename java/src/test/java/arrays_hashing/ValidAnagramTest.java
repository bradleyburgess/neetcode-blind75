package arrays_hashing;

import base.BaseSolutionTest;
import base.TestCase;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

public class ValidAnagramTest extends BaseSolutionTest<ValidAnagram, String[], Boolean> {
    @Override
    protected ValidAnagram createSolution() {
        return new ValidAnagram();
    }

    @Override
    protected String jsonKey() {
        return "02_valid_anagram";
    }

    @Override
    protected Object[] buildArgumentsFromInput(String[] testData) {
        return testData;
    }

    @Override
    protected TestCase<String[], Boolean> buildTestCaseFromNode(JsonNode node) {
        try {
            return new TestCase<>(
                objectMapper.treeToValue(node.get("input"), String[].class),
                node.get("expected").asBoolean()
            );
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }

    }
}
