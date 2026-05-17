package base;

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
    protected abstract TestCase<TInput, TResult> buildTestCaseFromNode(JsonNode node);

    protected Stream<TestCase<TInput, TResult>> testCases() {
        var data = TestDataSource.testData();
        var node = (ArrayNode) data.get(jsonKey());
        return StreamSupport.stream(node.spliterator(), false)
            .map(this::buildTestCaseFromNode);
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

