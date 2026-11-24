---
id: 20261124-cp0-go-errors-interfaces-context
title: CP0 · Go errors, interfaces & context
tags: [question-bank, cp0]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp0-git-github-flow, 20261124-cp0-github-copilot, 20261124-exam-blueprint]
summary: 20 CP0 questions on Go errors, interfaces & context (6 easy, 9 medium, 5 hard) with answers and explanations.
---

# CP0 · Go errors, interfaces & context

> Summary: 20 CP0 questions on Go errors, interfaces & context (6 easy, 9 medium, 5 hard) with answers and explanations.

## Context
Part of the CP0 Onboarding & Go essentials bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP0).

## Questions

### CP0-Q086 · Easy
How does a Go function usually report failure?

- A. By throwing an exception
- B. By returning an error as the last return value
- C. By returning -1
- D. By calling os.Exit

**Answer: B** — Go uses explicit error values.

### CP0-Q087 · Easy
What is the idiomatic error check?

- A. assert err
- B. if err { }
- C. if err != nil { return err }
- D. try { } catch { }

**Answer: C** — Check every returned error.

### CP0-Q088 · Easy
What is an interface in Go?

- A. A set of method signatures; any type with those methods satisfies it implicitly
- B. A generated file
- C. A struct with no fields
- D. A class that must be extended

**Answer: A** — Implicit satisfaction keeps packages decoupled.

### CP0-Q089 · Medium
How do you wrap an error with context while keeping the original?

- A. fmt.Errorf("create order: %w", err)
- B. panic(err)
- C. fmt.Println(err)
- D. errors.New(err)

**Answer: A** — %w enables errors.Is / errors.As.

### CP0-Q090 · Medium ★
What does errors.Is(err, ErrNotFound) check?

- A. Whether err is a pointer
- B. Whether err or any error it wraps matches ErrNotFound
- C. Whether err is nil
- D. Whether err has the same text

**Answer: B** — Use sentinel errors with errors.Is.

### CP0-Q091 · Medium
When is panic appropriate in service code?

- A. For not-found records
- B. For every database error
- C. For validation failures
- D. Almost never; only for truly unrecoverable programmer errors

**Answer: D** — Return errors; recovery middleware catches stray panics.

### CP0-Q092 · Medium
Why define `type OrderRepository interface { Save(ctx, o) error }` in the service package?

- A. So the service depends on an abstraction that can be mocked in tests and swapped (DynamoDB, memory)
- B. Go requires an interface for every struct
- C. To export the DynamoDB client
- D. Interfaces make code run faster

**Answer: A** — Small consumer-side interfaces enable testing.

### CP0-Q093 · Medium
What is context.Context used for?

- A. Carrying deadlines, cancellation and request-scoped values across calls
- B. Replacing function parameters entirely
- C. Logging only
- D. Storing global configuration

**Answer: A** — Pass ctx as the first parameter.

### CP0-Q094 · Medium
What should a handler do with the request context when calling AWS SDK?

- A. Use context.Background() always
- B. Ignore context
- C. Create a new context with no deadline
- D. Pass c.Request.Context() so cancellations and timeouts propagate

**Answer: D** — Propagating ctx stops wasted work.

### CP0-Q095 · Hard
What is a common mistake with context values?

- A. Cancelling contexts
- B. Passing ctx first
- C. Storing optional business parameters in context instead of function arguments
- D. Using context.WithTimeout

**Answer: C** — Context values are for request-scoped metadata like trace IDs.

### CP0-Q096 · Hard
Why is `var _ OrderRepository = (*DynamoRepo)(nil)` useful?

- A. It disables the interface
- B. It is a compile-time check that DynamoRepo implements the interface
- C. It allocates memory at startup
- D. It creates a global repository

**Answer: B** — Fails the build if a method is missing.

### CP0-Q097 · Easy ★
What does errors.New("not found") return?

- A. A panic
- B. A string
- C. A new error value with that message
- D. nil

**Answer: C** — Often used for sentinel errors.

### CP0-Q098 · Medium ★
How should you compare an error to a custom error type to access its fields?

- A. reflect.DeepEqual
- B. errors.As(err, &target)
- C. err.(string)
- D. err == target

**Answer: B** — errors.As unwraps to find a matching type.

### CP0-Q099 · Hard
What happens if you forget to call cancel() from context.WithTimeout?

- A. Resources tied to the context leak until the timeout fires
- B. The program panics immediately
- C. Nothing ever
- D. The timeout is ignored

**Answer: A** — go vet warns; always defer cancel().

### CP0-Q100 · Easy ★
Which empty interface type can hold any value?

- A. any (alias of interface{})
- B. void
- C. dynamic
- D. object

**Answer: A** — Prefer concrete types where possible.

### CP0-Q101 · Medium
What does a type switch do?

- A. Changes a variable's type
- B. Switches between goroutines
- C. Converts JSON to structs
- D. Branches on the dynamic type of an interface value

**Answer: D** — switch v := x.(type) { case string: ... }.

### CP0-Q102 · Hard
A function returns `(*Order, error)`. Which return is a bug?

- A. return nil, ErrNotFound
- B. return nil, fmt.Errorf("get: %w", err)
- C. return o, nil
- D. return nil, nil when the order was not found

**Answer: D** — Callers will dereference a nil order; signal not-found with an error.

### CP0-Q103 · Medium
Where should errors be logged?

- A. At every function that sees them
- B. Only in tests
- C. Once, at the boundary that handles them (e.g. the handler), not at every layer
- D. Never

**Answer: C** — Log-and-return everywhere creates duplicate noise.

### CP0-Q104 · Easy
What does `context.WithCancel` return?

- A. A new goroutine
- B. A derived context and a cancel function
- C. Only a cancel function
- D. An error

**Answer: B** — Calling cancel stops work using that context.

### CP0-Q105 · Hard ★
What is the safest way to hide internal error details from API clients?

- A. Map internal errors to a public problem type and log the internal error with the trace ID
- B. Panic and let Gin print it
- C. Return err.Error() to the client
- D. Return HTTP 200 with the stack trace

**Answer: A** — Never leak stack traces or SQL errors.

## Related
- [Git & GitHub flow](git-github-flow.md) — see-also: same checkpoint.
- [GitHub Copilot](github-copilot.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
