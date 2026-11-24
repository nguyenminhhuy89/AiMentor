---
id: 20261124-cp5-docker
title: CP5 · Docker
tags: [question-bank, cp5]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp5-ecs, 20261124-cp5-lambda, 20261124-exam-blueprint]
summary: 25 CP5 questions on Docker (8 easy, 12 medium, 5 hard) with answers and explanations.
---

# CP5 · Docker

> Summary: 25 CP5 questions on Docker (8 easy, 12 medium, 5 hard) with answers and explanations.

## Context
Part of the CP5 Runtime, IaC & CI/CD bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP5).

## Questions

### CP5-Q001 · Easy
What is a Docker image?

- A. A Git branch
- B. A read-only template with the app and its dependencies used to start containers
- C. A virtual machine disk only
- D. A running process

**Answer: B** — Containers are running instances of images.

### CP5-Q002 · Easy
Which file defines how an image is built?

- A. docker-compose.yml only
- B. Dockerfile
- C. go.mod
- D. Makefile

**Answer: B** — Build with docker build.

### CP5-Q003 · Easy ★
What does a multi-stage build do?

- A. Runs tests in production
- B. Creates multiple containers
- C. Uses one stage to compile and a smaller final stage that copies only the binary
- D. Builds images for multiple clouds

**Answer: C** — Smaller, safer images.

### CP5-Q004 · Easy
Why should containers run as a non-root user?

- A. AWS requires root
- B. It is faster
- C. Limits damage if the container is compromised
- D. Root cannot run Go

**Answer: C** — DoD: non-root images.

### CP5-Q005 · Easy ★
Which instruction sets the user in a Dockerfile?

- A. USER
- B. RUN user
- C. SETUSER
- D. AS

**Answer: A** — e.g. USER 65532:65532 or USER nonroot.

### CP5-Q006 · Medium
Which base image is a good minimal final stage for a static Go binary?

- A. gcr.io/distroless/static (nonroot) or scratch
- B. node:20
- C. ubuntu:latest
- D. golang:latest

**Answer: A** — Fewer packages = fewer vulnerabilities.

### CP5-Q007 · Medium
How do you build a static Go binary for scratch/distroless?

- A. go build -race
- B. CGO_ENABLED=0 go build -o app ./cmd/api
- C. go run main.go
- D. go test -c

**Answer: B** — No libc dependency.

### CP5-Q008 · Medium ★
Why copy go.mod and go.sum and run go mod download before copying source?

- A. It disables CGO
- B. Docker requires that order
- C. It reduces binary size
- D. Layer caching: dependencies are reused when only source code changes

**Answer: D** — Faster rebuilds.

### CP5-Q009 · Medium
What does .dockerignore do?

- A. Hides containers
- B. Skips image scanning
- C. Excludes files from the build context (e.g. .git, .env, local binaries)
- D. Ignores Docker errors

**Answer: C** — Smaller context and no leaked secrets.

### CP5-Q010 · Medium
Why avoid the :latest tag in deployments?

- A. It is mutable, so you cannot know or roll back exactly what runs
- B. ECS rejects it
- C. It is not free
- D. It is slower

**Answer: A** — Use immutable tags like the Git SHA.

### CP5-Q011 · Medium
What does an image scanner like Trivy report?

- A. Network latency
- B. Unit test failures
- C. Go lint warnings only
- D. Known vulnerabilities (CVEs) in OS packages and dependencies, plus misconfigurations

**Answer: D** — DoD: 0 critical/high.

### CP5-Q012 · Medium
A scan shows high CVEs from the ubuntu base. Fastest fix?

- A. Run as root
- B. Switch the final stage to distroless/scratch and rebuild
- C. Add more packages
- D. Ignore them

**Answer: B** — Most CVEs come from unused OS packages.

### CP5-Q013 · Hard
Why should secrets never be passed via build ARG?

- A. Build args can persist in image history/metadata
- B. ARGs are encrypted
- C. ARG is deprecated
- D. ARGs are slow

**Answer: A** — Use runtime secrets instead.

### CP5-Q014 · Hard
How do you make a container image immutable in ECR?

- A. Use latest tag
- B. Disable scanning
- C. Delete old images
- D. Enable tag immutability on the repository

**Answer: D** — Prevents tag overwrites.

### CP5-Q015 · Easy
Which command lists running containers?

- A. docker images
- B. docker logs
- C. docker ps
- D. docker build

**Answer: C** — docker images lists images.

### CP5-Q016 · Medium
What does EXPOSE 8080 do in a Dockerfile?

- A. Documents the port; it does not publish it by itself
- B. Sets the app port in Go
- C. Creates a security group
- D. Opens the port to the internet

**Answer: A** — Port mapping is done at run/task level.

### CP5-Q017 · Medium ★
Where should the app listen inside the container?

- A. Port 22
- B. A Unix socket only
- C. 0.0.0.0:<port> so traffic from outside the container reaches it
- D. 127.0.0.1 only

**Answer: C** — Localhost binding is unreachable from ECS.

### CP5-Q018 · Hard
What is a HEALTHCHECK or ECS health check for?

- A. Measuring code coverage
- B. Detecting unhealthy containers so the orchestrator replaces them
- C. Scanning images
- D. Rate limiting

**Answer: B** — Use a lightweight /healthz.

### CP5-Q019 · Easy
Which registry does the bootcamp push images to?

- A. GitHub Releases
- B. Amazon ECR
- C. S3
- D. Docker Hub public

**Answer: B** — Private, IAM-controlled.

### CP5-Q020 · Hard ★
Distroless has no shell. How do you debug a running container?

- A. Use logs/traces, ECS Exec with a debug sidecar or a debug image variant — not a shell in prod images
- B. SSH into the container
- C. Run as root
- D. Add bash to the prod image

**Answer: A** — Keep prod images minimal.

### CP5-Q021 · Medium
What does "docker build -t order-service:${GIT_SHA} ." achieve?

- A. Scans the image
- B. Tags the image with the commit SHA for traceability
- C. Pushes the image
- D. Runs tests

**Answer: B** — SHA tags link images to commits.

### CP5-Q022 · Medium
Why keep one process per container?

- A. It improves CPU
- B. It is required by Go
- C. Simpler lifecycle, scaling and logging; the orchestrator manages processes
- D. Docker cannot run two processes

**Answer: C** — Sidecars handle extra concerns.

### CP5-Q023 · Hard
What does the -trimpath and -ldflags "-s -w" build flags help with?

- A. Encryption
- B. Faster tests
- C. Reproducible builds without local paths and smaller binaries without debug symbols
- D. Race detection

**Answer: C** — Optional optimizations.

### CP5-Q024 · Easy
What is a container?

- A. A running, isolated instance of an image
- B. A Dockerfile
- C. A VM image
- D. A registry

**Answer: A** — Lightweight isolation on a shared kernel.

### CP5-Q025 · Medium ★
Which ECR feature scans images on push?

- A. ECR lifecycle policies
- B. ECR pull-through cache
- C. ECR image scanning (basic or enhanced with Inspector)
- D. ECR replication

**Answer: C** — Complements Trivy in CI.

## Related
- [ECS](ecs.md) — see-also: same checkpoint.
- [Lambda](lambda.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
