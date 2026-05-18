package base;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.lang.reflect.Method;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public abstract class BaseSolutionTest<TSolution, TInput, TResult> {
    protected ObjectMapper objectMapper = new ObjectMapper();

    protected abstract TSolution createSolution();

    protected abstract String jsonKey();

    protected abstract Object[] buildArgumentsFromInput(TInput input);

    protected abstract TestCase<TInput, TResult> buildTestCaseFromNode(JsonNode input, JsonNode expected) throws JsonProcessingException;

    protected Stream<TestCase<TInput, TResult>> testCases() {
        var data = TestDataSource.testData();
        var node = (ArrayNode) data.get(jsonKey());
        return StreamSupport.stream(node.spliterator(), false)
            .map(n -> {
                try {
                    return this.buildTestCaseFromNode(n.get("input"), n.get("expected"));
                } catch (JsonProcessingException e) {
                    throw new RuntimeException(e);
                }
            });
    }

    @ParameterizedTest
    @MethodSource("testCases")
    void testAllSolutions(TestCase<TInput, TResult> testCase) throws Exception {
        TSolution solution = createSolution();

        Method[] methods = solution.getClass().getDeclaredMethods();

        for (Method method : methods) {
            if (!method.getName().startsWith("solve")) {
                continue;
            }

            Object actual = method.invoke(
                solution,
                buildArgumentsFromInput(testCase.input())
            );

            if (actual != null && actual.getClass().isArray()) {
                var expectedNode = objectMapper.valueToTree(testCase.expected());
                var actualNode = objectMapper.valueToTree(actual);
                Assertions.assertEquals(
                    expectedNode, actualNode,
                    () -> method.getName() +
                        " failed for input: " +
                        testCase.input()
                );
            } else {
                Assertions.assertEquals(
                    testCase.expected(),
                    actual,
                    () -> method.getName() +
                        " failed for input: " +
                        testCase.input()
                );
            }
        }
    }
}

