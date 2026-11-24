---
id: 20261124-cp4-cognito-jwt
title: CP4 · Cognito & JWT
tags: [question-bank, cp4]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp4-iam-least-privilege, 20261124-cp4-secrets-configuration, 20261124-exam-blueprint]
summary: 20 CP4 questions on Cognito & JWT (5 easy, 10 medium, 5 hard) with answers and explanations.
---

# CP4 · Cognito & JWT

> Summary: 20 CP4 questions on Cognito & JWT (5 easy, 10 medium, 5 hard) with answers and explanations.

## Context
Part of the CP4 Gateway, Network & Security bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP4).

## Questions

### CP4-Q101 · Easy
What is Amazon Cognito user pool?

- A. A DynamoDB table
- B. An IAM role
- C. A managed user directory that authenticates users and issues JWTs
- D. A Kong plugin

**Answer: C** — Issues ID, access and refresh tokens.

### CP4-Q102 · Easy ★
What are the three parts of a JWT?

- A. Key, value, TTL
- B. Header, payload, signature
- C. User, password, role
- D. Issuer, audience, scope

**Answer: B** — Base64URL-encoded, dot-separated.

### CP4-Q103 · Easy
Is a JWT payload encrypted?

- A. Only with HTTPS
- B. No, it is only encoded and signed; anyone can read it
- C. Only in Cognito
- D. Yes, always

**Answer: B** — Never put secrets in JWT claims.

### CP4-Q104 · Medium
Which claim states when the token expires?

- A. sub
- B. aud
- C. exp
- D. iat

**Answer: C** — Reject expired tokens.

### CP4-Q105 · Medium ★
How does Kong verify a Cognito token signature?

- A. It cannot
- B. By calling Cognito for every request with the client secret
- C. Using Cognito's public keys from the JWKS endpoint
- D. Using the user's password

**Answer: C** — RS256 signatures verified with public keys.

### CP4-Q106 · Medium
Which token should be sent to APIs as the bearer token?

- A. The client secret
- B. The access token
- C. The refresh token
- D. The ID token always

**Answer: B** — Access tokens carry scopes for APIs.

### CP4-Q107 · Medium
What is the refresh token for?

- A. Rate limiting
- B. Encrypting data
- C. Calling APIs directly
- D. Obtaining new access/ID tokens without re-login

**Answer: D** — Keep it secure on the client.

### CP4-Q108 · Medium
What is an app client in Cognito?

- A. Configuration for an application that can authenticate against the user pool
- B. A Lambda layer
- C. A Kong consumer
- D. An ECS task

**Answer: A** — Defines flows, scopes, callback URLs.

### CP4-Q109 · Medium ★
Which OAuth2 flow fits server-to-server calls with Cognito?

- A. Password grant from browser
- B. Authorization code with PKCE only
- C. Implicit flow
- D. Client credentials grant with resource server scopes

**Answer: D** — Machine-to-machine.

### CP4-Q110 · Medium
Which flow fits a web/mobile user login?

- A. Implicit flow (recommended)
- B. Sending passwords to the API
- C. Client credentials
- D. Authorization code with PKCE

**Answer: D** — PKCE is the modern standard.

### CP4-Q111 · Hard
Which claims must be validated besides signature and exp?

- A. iss (issuer = the user pool) and audience/client_id, plus token_use
- B. None
- C. Only the username
- D. Only iat

**Answer: A** — Prevents tokens from other pools/clients.

### CP4-Q112 · Hard
How do you implement "only admins can cancel any order"?

- A. Use different URLs
- B. Hide the button in UI only
- C. Trust a role field sent in the JSON body
- D. Use Cognito groups/scopes in the token and enforce in Kong/service authorization logic

**Answer: D** — Never trust client-supplied roles.

### CP4-Q113 · Easy ★
Which header carries the bearer token?

- A. Cookie only
- B. Authorization: Bearer <token>
- C. X-Token
- D. Accept

**Answer: B** — Standard header.

### CP4-Q114 · Medium
Where should a SPA store tokens to reduce XSS risk?

- A. In the URL
- B. In Git
- C. In localStorage forever
- D. In memory or secure, httpOnly cookies handled by a backend — not long-lived in localStorage

**Answer: D** — Awareness for front-end integration.

### CP4-Q115 · Hard
An attacker changes "alg" to "none" in a JWT. What must the validator do?

- A. Re-sign them
- B. Accept them
- C. Accept if exp is valid
- D. Reject tokens not signed with the expected algorithm (RS256)

**Answer: D** — Pin the algorithm.

### CP4-Q116 · Medium
What does the sub claim contain in Cognito tokens?

- A. The client secret
- B. The email address
- C. The group name
- D. The user's unique, immutable identifier

**Answer: D** — Use sub as the user key, not email.

### CP4-Q117 · Hard ★
Access token lifetime is 60 minutes. A user is disabled now. What still works until expiry?

- A. Already-issued access tokens unless revoked/short-lived; plan short lifetimes and revocation
- B. Nothing works immediately
- C. Refresh tokens forever
- D. Only the ID token

**Answer: A** — Trade-off of stateless tokens.

### CP4-Q118 · Easy
What does Cognito's hosted UI provide?

- A. A CI pipeline
- B. An API gateway
- C. Ready-made sign-in/sign-up pages
- D. A database

**Answer: C** — Optional for the capstone.

### CP4-Q119 · Medium
Why must all token traffic use HTTPS?

- A. Bearer tokens can be replayed by anyone who intercepts them
- B. Cognito blocks HTTP for speed
- C. It reduces token size
- D. JWTs require it to parse

**Answer: A** — Bearer = whoever holds it.

### CP4-Q120 · Hard
Cognito rotates signing keys. How should Kong/service handle it?

- A. Disable validation during rotation
- B. Hardcode one key forever
- C. Fetch JWKS by kid and refresh the cache when an unknown kid appears
- D. Ask users to re-register

**Answer: C** — Key rotation must not break auth.

## Related
- [IAM least privilege](iam-least-privilege.md) — see-also: same checkpoint.
- [Secrets & configuration](secrets-configuration.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
