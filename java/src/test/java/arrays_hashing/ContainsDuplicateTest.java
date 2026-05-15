package arrays_hashing;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.stream.Stream;
import static org.junit.jupiter.api.Assertions.assertEquals;

class ContainsDuplicateTest {
    ContainsDuplicate cd = new ContainsDuplicate();

    static Stream<Function<int[], Boolean>> methodProvider() {
        ContainsDuplicate sol = new ContainsDuplicate();
        return Stream.of(sol::solveBrute, sol::solveHashMap);
    }

    static Stream<Arguments> testData() {
        return Stream.of(
            Arguments.of(new int[]{1, 2, 3, 1}, true),
            Arguments.of(new int[]{1, 2, 3}, false),
            Arguments.of(new int[]{ }, false),
            Arguments.of(new int[]{ 1 }, false),
            Arguments.of(new int[]{ 1, 1 }, true)
        );
    }

    @ParameterizedTest
    @MethodSource("methodProvider")
    void testAll(Function<int[], Boolean> solve) {
        testData().forEach(arg -> {
            Object[] params = arg.get();
            boolean result = solve.apply((int[]) params[0]);
            assertEquals((boolean) params[1], result);
        });
    }
}
