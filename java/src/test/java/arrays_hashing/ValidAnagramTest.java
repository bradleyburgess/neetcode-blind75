package arrays_hashing;

import base.BaseSolutionTest;
import base.TestCase;

import java.util.stream.Stream;

public class ValidAnagramTest
    extends BaseSolutionTest<ValidAnagram, TestData, Boolean> {

    @Override
    protected ValidAnagram createSolution() {
        return new ValidAnagram();
    }

    @Override
    protected Stream<TestCase<TestData, Boolean>> testCases() {
        return Stream.of(
            new TestCase<>(new TestData("hello", "elloh"), true),
            new TestCase<>(new TestData("hellz", "elloh"), false)
        );
    }

    @Override
    protected Object[] buildArguments(TestData input) {
        return new Object[]{input.string1(), input.string2()};
    }
}

record TestData(
    String string1,
    String string2
) { }
