---
id: 20261124-cp2-kms-pii-encryption
title: CP2 · KMS & PII encryption
tags: [question-bank, cp2]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp2-aws-fundamentals-iam-basics, 20261124-cp2-aws-sdk-for-go-v2, 20261124-exam-blueprint]
summary: 20 CP2 questions on KMS & PII encryption (5 easy, 10 medium, 5 hard) with answers and explanations.
---

# CP2 · KMS & PII encryption

> Summary: 20 CP2 questions on KMS & PII encryption (5 easy, 10 medium, 5 hard) with answers and explanations.

## Context
Part of the CP2 Data & Encryption bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP2).

## Questions

### CP2-Q101 · Easy ★
What is AWS KMS?

- A. A Kong plugin
- B. A managed service to create and control cryptographic keys
- C. A VPN
- D. A password manager for users

**Answer: B** — Keys never leave KMS unencrypted.

### CP2-Q102 · Easy ★
What is PII?

- A. Public infrastructure inventory
- B. Personally identifiable information such as email and phone
- C. An IAM policy
- D. A Go package

**Answer: B** — Customer email and phone are PII in the capstone.

### CP2-Q103 · Easy
What is envelope encryption?

- A. Encrypting data with a data key, and encrypting that data key with a KMS key
- B. Encrypting the database file only
- C. Encrypting the envelope of an email
- D. Double hashing a password

**Answer: A** — Store the encrypted data key alongside the ciphertext.

### CP2-Q104 · Medium
Which KMS API returns a plaintext data key and its encrypted copy?

- A. GenerateDataKey
- B. Encrypt
- C. CreateKey
- D. ListAliases

**Answer: A** — Use the plaintext key locally, then discard it.

### CP2-Q105 · Medium ★
What should happen to the plaintext data key after encrypting a field?

- A. Zero it/discard it from memory; store only the encrypted data key
- B. Cache it forever on disk
- C. Store it in DynamoDB next to the data
- D. Log it for debugging

**Answer: A** — Only the KMS-encrypted key is persisted.

### CP2-Q106 · Medium
What is the encryption context?

- A. A Go context.Context
- B. A password
- C. Non-secret key-value pairs bound to the ciphertext and required to decrypt
- D. The region name

**Answer: C** — e.g. {orderId, field: "email"}; also logged in CloudTrail.

### CP2-Q107 · Medium
Direct KMS Encrypt is limited to small payloads. What is the size limit?

- A. 400 KB
- B. 4 MB
- C. 4 KB of plaintext
- D. Unlimited

**Answer: C** — Use envelope encryption for larger data.

### CP2-Q108 · Medium
Why use a KMS key alias like alias/order-pii?

- A. Aliases are more secure keys
- B. Aliases avoid IAM
- C. Code references a stable name while the underlying key can rotate or change
- D. Aliases are free keys

**Answer: C** — Decouples code from key IDs.

### CP2-Q109 · Medium
Which permission does the service need to read encrypted PII?

- A. kms:*
- B. s3:GetObject
- C. kms:CreateKey
- D. kms:Decrypt on the specific key

**Answer: D** — Least privilege for crypto too.

### CP2-Q110 · Medium
Which mode of AES does the AWS Encryption SDK use with data keys by default?

- A. AES-GCM (authenticated encryption)
- B. DES
- C. ROT13
- D. AES-ECB

**Answer: A** — Authenticated encryption detects tampering.

### CP2-Q111 · Hard ★
Why not encrypt every field individually with kms:Encrypt on every request?

- A. It is less secure
- B. It is not allowed in Go
- C. KMS cannot encrypt strings
- D. It adds latency, cost and throttling risk; data-key caching/envelope encryption scales better

**Answer: D** — Balance security with performance.

### CP2-Q112 · Hard
How do you prove "no plaintext PII in logs"?

- A. Delete logs daily
- B. Mask PII in logging middleware and test that logs never contain email/phone patterns
- C. Trust developers
- D. Use DEBUG level

**Answer: B** — Make it a test, not a hope.

### CP2-Q113 · Hard
Decrypt fails with InvalidCiphertextException after a code change. Likely cause?

- A. The encryption context used on decrypt differs from the one used on encrypt
- B. The key was too strong
- C. Go version changed
- D. DynamoDB corrupted the data

**Answer: A** — Context must match exactly.

### CP2-Q114 · Medium
What does automatic key rotation for a customer managed key do?

- A. Deletes old keys
- B. Re-encrypts all data
- C. Generates new key material yearly while old material remains for decrypting old data
- D. Changes the alias

**Answer: C** — Transparent to callers.

### CP2-Q115 · Easy
Where are KMS key usage events visible?

- A. Kong logs
- B. AWS CloudTrail
- C. S3 access logs only
- D. Jira

**Answer: B** — Auditable crypto operations.

### CP2-Q116 · Medium ★
How should a unit test cover encryption code without AWS?

- A. Call real KMS
- B. Mock the KMS client interface and assert encrypt/decrypt round-trip and that plaintext is not persisted
- C. Disable encryption in prod
- D. Skip encryption in tests

**Answer: B** — Round-trip tests catch bugs.

### CP2-Q117 · Hard
Hashing vs encryption for customer phone numbers you must display later?

- A. Encryption, because hashing is one-way and cannot be reversed for display
- B. Neither
- C. Base64, because it is encryption
- D. Hashing, because it is reversible

**Answer: A** — Hash for lookup/compare; encrypt to read back.

### CP2-Q118 · Hard
What is a key policy?

- A. An IAM user password rule
- B. A rotation schedule
- C. A Kong rate limit
- D. The resource policy on a KMS key that controls who can use and manage it

**Answer: D** — Key policy + IAM together grant access.

### CP2-Q119 · Easy
Is base64 encoding a form of encryption?

- A. Only for PII
- B. Yes, strong encryption
- C. No, it is reversible encoding with no key
- D. Yes, with AWS only

**Answer: C** — Never treat base64 as protection.

### CP2-Q120 · Medium
Searching orders by customer email when email is encrypted: common approach?

- A. Store a keyed hash (HMAC) of the normalized email as a lookup attribute
- B. Store email in plaintext too
- C. Disallow search
- D. Decrypt every item in a scan

**Answer: A** — Blind index pattern; awareness for freshers.

## Related
- [AWS fundamentals & IAM basics](aws-fundamentals-iam-basics.md) — see-also: same checkpoint.
- [AWS SDK for Go v2](aws-sdk-for-go-v2.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
