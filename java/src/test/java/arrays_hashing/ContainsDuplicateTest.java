package arrays_hashing;

import base.BaseSolutionTest;
import base.TestCase;

import java.util.stream.Stream;

public class ContainsDuplicateTest
    extends BaseSolutionTest<ContainsDuplicate, int[], Boolean> {

    @Override
    protected ContainsDuplicate createSolution() {
        return new ContainsDuplicate();
    }

    @Override
    protected Stream<TestCase<int[], Boolean>> testCases() {
        return Stream.of(
            new TestCase<>(new int[]{1, 2, 3, 1}, true),
            new TestCase<>(new int[]{1, 2, 3, 4}, false),
            new TestCase<>(new int[]{1,1,1,1}, true)
        );
    }

    @Override
    protected Object[] buildArguments(int[] input) {
        return new Object[]{input};
    }
}
