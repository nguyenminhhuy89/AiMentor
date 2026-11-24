---
id: 20261124-cp0-go-syntax-types
title: CP0 · Go syntax & types
tags: [question-bank, cp0]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp0-git-github-flow, 20261124-cp0-github-copilot, 20261124-exam-blueprint]
summary: 20 CP0 questions on Go syntax & types (8 easy, 9 medium, 3 hard) with answers and explanations.
---

# CP0 · Go syntax & types

> Summary: 20 CP0 questions on Go syntax & types (8 easy, 9 medium, 3 hard) with answers and explanations.

## Context
Part of the CP0 Onboarding & Go essentials bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP0).

## Questions

### CP0-Q066 · Easy
What is the entry point of a Go program?

- A. func main() in package main
- B. func init() in any package
- C. The first function in the file
- D. func start()

**Answer: A** — Executables need package main with func main.

### CP0-Q067 · Easy
Which declares and initializes a variable with type inference?

- A. count := 10
- B. var count = int
- C. let count = 10
- D. count == 10

**Answer: A** — := is the short variable declaration inside functions.

### CP0-Q068 · Easy ★
What is the zero value of a string in Go?

- A. undefined
- B. "null"
- C. nil
- D. "" (empty string)

**Answer: D** — Every type has a zero value; string's is "".

### CP0-Q069 · Easy
What is the zero value of a pointer, slice or map?

- A. nil
- B. An empty struct
- C. false
- D. 0

**Answer: A** — nil maps panic on write; initialize with make.

### CP0-Q070 · Easy
How do you define a struct type for an order?

- A. type Order = map
- B. struct Order { ID string }
- C. type Order struct { ID string; Amount int64 }
- D. class Order { ID string }

**Answer: C** — Go uses struct types, not classes.

### CP0-Q071 · Easy
Which identifier is exported from a Go package?

- A. _createOrder
- B. create_order
- C. createOrder
- D. CreateOrder

**Answer: D** — Names starting with an uppercase letter are exported.

### CP0-Q072 · Medium ★
What does `make([]int, 0, 10)` create?

- A. A map with 10 keys
- B. A channel of size 10
- C. An array of 10 zeros
- D. A slice with length 0 and capacity 10

**Answer: D** — make sets length and optional capacity for slices.

### CP0-Q073 · Medium ★
What happens when you write to a nil map?

- A. Nothing happens
- B. A compile error
- C. The map is created automatically
- D. A runtime panic

**Answer: D** — Use make(map[string]int) or a literal first.

### CP0-Q074 · Medium
How do you check if a key exists in a map?

- A. m.has("k")
- B. v, ok := m["k"]
- C. exists(m, "k")
- D. m["k"] != nil always works

**Answer: B** — The comma-ok idiom returns presence.

### CP0-Q075 · Medium
What does `defer` do?

- A. Delays the call by one second
- B. Runs the call in a new goroutine
- C. Schedules a call to run when the surrounding function returns
- D. Skips the call on error

**Answer: C** — Defers run in LIFO order, useful for Close().

### CP0-Q076 · Medium
Which loop form iterates over a slice with index and value?

- A. for i, v := range items {}
- B. while i < len(items) {}
- C. for v of items {}
- D. foreach (v in items) {}

**Answer: A** — Go has only for, with range for collections.

### CP0-Q077 · Medium
Struct method with pointer receiver: why use `func (s *Service) Create()`?

- A. Value receivers cannot have methods
- B. It makes the method private
- C. Pointer receivers are faster to type
- D. To modify the struct and avoid copying it on each call

**Answer: D** — Pointer receivers share state and avoid copies.

### CP0-Q078 · Medium
What is a Go module?

- A. A collection of packages versioned together, defined by go.mod
- B. A single .go file
- C. A Gin middleware
- D. A Docker image

**Answer: A** — go mod init creates go.mod.

### CP0-Q079 · Hard
Two goroutines append to the same slice without synchronization. What is the risk?

- A. The program becomes faster
- B. A data race causing lost or corrupted data
- C. Nothing, slices are thread-safe
- D. A compile error

**Answer: B** — Use a mutex or channels; go test -race detects it.

### CP0-Q080 · Hard
What does `go test -race` do?

- A. Retries failing tests
- B. Runs tests with the race detector to find unsynchronized concurrent access
- C. Measures coverage
- D. Runs tests faster in parallel

**Answer: B** — Race detection is part of quality checks.

### CP0-Q081 · Easy ★
What does `go mod tidy` do?

- A. Runs the linter
- B. Deletes the vendor folder
- C. Adds missing and removes unused module dependencies
- D. Formats the code

**Answer: C** — Keep go.mod and go.sum clean.

### CP0-Q082 · Medium
What is the difference between an array and a slice?

- A. Slices are fixed, arrays are dynamic
- B. Arrays have fixed length as part of the type; slices are dynamic views over arrays
- C. They are the same
- D. Arrays can only hold strings

**Answer: B** — [3]int vs []int.

### CP0-Q083 · Hard ★
What is printed? `s := []int{1,2,3}; t := s[:2]; t[0] = 9; fmt.Println(s[0])`

- A. 0
- B. Compile error
- C. 1
- D. 9

**Answer: D** — t shares the backing array with s.

### CP0-Q084 · Easy
Which tool formats Go code to the standard style?

- A. go build
- B. gofmt (or go fmt)
- C. golint only
- D. go vet

**Answer: B** — Formatting is not optional in Go teams.

### CP0-Q085 · Medium
What is a goroutine?

- A. A test helper
- B. An OS process
- C. A lightweight concurrent function started with the go keyword
- D. A Go module

**Answer: C** — go doWork() starts it.

## Related
- [Git & GitHub flow](git-github-flow.md) — see-also: same checkpoint.
- [GitHub Copilot](github-copilot.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
