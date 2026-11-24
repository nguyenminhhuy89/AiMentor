---
id: 20261124-cp1-json-schema
title: CP1 · JSON Schema
tags: [question-bank, cp1]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp1-http-rest, 20261124-cp1-openapi-3-0, 20261124-exam-blueprint]
summary: 20 CP1 questions on JSON Schema (6 easy, 10 medium, 4 hard) with answers and explanations.
---

# CP1 · JSON Schema

> Summary: 20 CP1 questions on JSON Schema (6 easy, 10 medium, 4 hard) with answers and explanations.

## Context
Part of the CP1 Contract & Core API bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP1).

## Questions

### CP1-Q046 · Easy
Which JSON Schema keyword sets the data type?

- A. type
- B. format
- C. class
- D. kind

**Answer: A** — e.g. type: string.

### CP1-Q047 · Easy
Which keyword limits string length?

- A. maxLength
- B. maxItems
- C. maximum
- D. length

**Answer: A** — maxLength/minLength for strings.

### CP1-Q048 · Easy
Which keyword sets the smallest allowed number?

- A. minItems
- B. minLength
- C. minimum
- D. lowest

**Answer: C** — minimum/maximum for numbers.

### CP1-Q049 · Easy ★
Which keyword restricts a value to a fixed set?

- A. enum
- B. choice
- C. oneOf only
- D. const only

**Answer: A** — e.g. status: enum [PENDING, PAID, CANCELLED].

### CP1-Q050 · Easy
What does format: email do?

- A. Encrypts the email
- B. Annotates/validates that a string is an email address
- C. Converts to lowercase
- D. Hides the field

**Answer: B** — Format validation depends on the validator.

### CP1-Q051 · Medium ★
Which keyword validates a string against a regular expression?

- A. pattern
- B. format: regex
- C. match
- D. regex

**Answer: A** — e.g. pattern: '^ORD-[0-9]+$'.

### CP1-Q052 · Medium
What does `exclusiveMinimum` mean in OpenAPI 3.0?

- A. The minimum is ignored
- B. It sets a default
- C. The minimum applies to strings
- D. A boolean making minimum exclusive (value must be greater than minimum)

**Answer: D** — In 3.0 it is boolean; in 3.1 it is a number.

### CP1-Q053 · Medium ★
How do you model money safely in the schema?

- A. Integer minor units (e.g. amountMinor: integer) plus a currency code
- B. A free-text string
- C. A float in dollars
- D. A boolean

**Answer: A** — Floats cause rounding errors with money.

### CP1-Q054 · Medium
What does `oneOf` require?

- A. None of the schemas
- B. The value matches exactly one of the listed schemas
- C. All schemas
- D. At least one schema

**Answer: B** — anyOf = at least one; allOf = all.

### CP1-Q055 · Medium
What is `allOf` often used for?

- A. Arrays only
- B. Marking fields optional
- C. Choosing one of many types
- D. Composing a schema from a base schema plus extra properties

**Answer: D** — e.g. OrderResponse = allOf [Order, Audit].

### CP1-Q056 · Medium
What does `uniqueItems: true` enforce?

- A. IDs are UUIDs
- B. All array elements are distinct
- C. Strings are unique in the DB
- D. The array has one item

**Answer: B** — Array-level constraint.

### CP1-Q057 · Medium
Which is a correct schema for an ISO-8601 timestamp?

- A. type: date
- B. type: integer, format: iso
- C. type: timestamp
- D. type: string, format: date-time

**Answer: D** — date-time maps to time.Time in oapi-codegen.

### CP1-Q058 · Hard
Using oneOf for payment methods, what helps code generators and validators pick the type?

- A. A discriminator with propertyName (e.g. type)
- B. Using anyOf instead
- C. Adding more required fields
- D. Making all fields nullable

**Answer: A** — Discriminators make polymorphism explicit.

### CP1-Q059 · Hard
Why validate requests against the schema at runtime as well as generating types?

- A. Validation makes responses faster
- B. Kong requires it
- C. Go cannot parse JSON otherwise
- D. Generated types do not enforce constraints like pattern, min/max or enum on input

**Answer: D** — Use request validation middleware (e.g. kin-openapi based).

### CP1-Q060 · Hard
A phone number field is PII. What should the schema NOT do?

- A. Include real example phone numbers of real people
- B. Use pattern validation
- C. Mark it required
- D. Set maxLength

**Answer: A** — Examples must be synthetic.

### CP1-Q061 · Easy ★
Which keyword gives an illustrative value in docs?

- A. sample
- B. const
- C. example
- D. default

**Answer: C** — Examples help consumers; they do not validate.

### CP1-Q062 · Medium
What is the difference between `default` and `example`?

- A. They are identical
- B. example is enforced; default is not
- C. default is the value assumed when absent; example is only illustrative
- D. default only works for arrays

**Answer: C** — Do not confuse documentation with behavior.

### CP1-Q063 · Medium
What does `minProperties: 1` mean for a PATCH body?

- A. Only one field allowed
- B. At least one field must be provided
- C. The body must be empty
- D. All fields are required

**Answer: B** — Prevents empty updates.

### CP1-Q064 · Hard ★
How should an error response schema follow RFC 7807?

- A. stack and line
- B. error: true
- C. code and message only
- D. Fields type, title, status, detail, instance (plus extensions like traceId)

**Answer: D** — Media type application/problem+json.

### CP1-Q065 · Medium
Which type should an order quantity be?

- A. integer with minimum: 1
- B. number with minimum: 0
- C. string
- D. boolean

**Answer: A** — Quantities are whole and positive.

## Related
- [HTTP & REST](http-rest.md) — see-also: same checkpoint.
- [OpenAPI 3.0](openapi-3-0.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
