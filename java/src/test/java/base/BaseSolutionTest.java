package base;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import java.lang.reflect.Method;
import java.util.stream.Stream;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public abstract class BaseSolutionTest<TSolution, TInput, TResult> {
    protected abstract TSolution createSolution();

    protected abstract Stream<TestCase<TInput, TResult>> testCases();

    protected abstract Object[] buildArguments(TInput input);

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
                buildArguments(testCase.input())
            );

            Assertions.assertEquals(
                testCase.expected(),
                actual,
                () -> new StringBuilder()
                    .append(method.getName())
                    .append(" failed for input: ")
                    .append(testCase.input())
                    .toString()
            );
        }
    }
}

