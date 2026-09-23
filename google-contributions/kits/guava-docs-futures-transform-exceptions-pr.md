**Title:** Document that `transform` and `transformAsync` propagate exceptions thrown by the function

The Javadoc for `Futures.transform`, `Futures.transformAsync`, `FluentFuture.transform` and `FluentFuture.transformAsync` says that if the input fails, the returned `Future` fails with the same exception. It does not say what happens when the function itself throws. This adds the following sentence right after the existing one in all four methods:

> If the function throws an exception, the returned {@code Future} fails with that exception.

This is a Javadoc-only change. `catching` and `catchingAsync` (in both `Futures` and `FluentFuture`) already say "If, during the invocation of {@code fallback}, an exception is thrown, this exception is used as the result of the output {@code Future}", so they are not changed.

Fixes #2690

Verification:
- In `AbstractTransformFuture.run()`, any `Throwable` from `doTransform` is passed to `setException(t)`.
- I also ran a small program against the built jar, once with `directExecutor()` and once with a thread pool. In every case the returned future failed, and `ExecutionException.getCause()` was the same instance the function threw:
  - `transform` with a `RuntimeException` or an `Error`, whether the input was already done or completed later
  - `transformAsync` with a `RuntimeException`, a checked exception or an `Error`
  - the same checks through `FluentFuture`
- If an `AsyncFunction` returns `null`, the returned future fails with a `NullPointerException` ("AsyncFunction.apply returned null instead of a Future..."). This PR does not document that case.

Testing:
- `./mvnw -pl guava,guava-testlib,guava-tests test -Dtest.include="**/FuturesTest.java,**/FluentFutureTest.java"`: 169 tests (160 in FuturesTest, 9 in FluentFutureTest), 0 failures, 0 errors.
- `./mvnw -pl guava javadoc:javadoc`: BUILD SUCCESS, and the new sentence appears in the generated `Futures.html` and `FluentFuture.html`.
