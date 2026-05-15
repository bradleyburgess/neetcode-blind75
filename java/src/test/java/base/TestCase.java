package base;

public record TestCase<TInput, TExpected>(
    TInput input,
    TExpected expected
) {
}
