---
id: 20261124-cp4-vpc-subnets-security-groups
title: CP4 · VPC, subnets & security groups
tags: [question-bank, cp4]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp4-iam-least-privilege, 20261124-cp4-secrets-configuration, 20261124-exam-blueprint]
summary: 20 CP4 questions on VPC, subnets & security groups (6 easy, 9 medium, 5 hard) with answers and explanations.
---

# CP4 · VPC, subnets & security groups

> Summary: 20 CP4 questions on VPC, subnets & security groups (6 easy, 9 medium, 5 hard) with answers and explanations.

## Context
Part of the CP4 Gateway, Network & Security bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP4).

## Questions

### CP4-Q041 · Easy ★
What is a VPC?

- A. A virtual machine
- B. A database
- C. A VPN client
- D. A logically isolated virtual network in AWS

**Answer: D** — Contains subnets, routes and gateways.

### CP4-Q042 · Easy
What makes a subnet "public"?

- A. It has more IPs
- B. It is in us-east-1
- C. Its route table has a route to an internet gateway
- D. It has a public name

**Answer: C** — Private subnets have no IGW route.

### CP4-Q043 · Easy
What is a security group?

- A. A stateful virtual firewall attached to resources like ECS tasks and RDS
- B. A Kong plugin
- C. A route table
- D. A group of IAM users

**Answer: A** — Controls inbound and outbound traffic.

### CP4-Q044 · Easy ★
Where should the Order Service tasks run per the DoD?

- A. The default VPC public subnets
- B. On a developer laptop
- C. Private subnets
- D. Public subnets with public IPs

**Answer: C** — Exposure only via gateway/load balancer.

### CP4-Q045 · Medium ★
How do private subnet tasks reach the internet for outbound calls?

- A. Directly via the IGW
- B. Through a NAT gateway in a public subnet (or VPC endpoints for AWS services)
- C. Through Route 53
- D. They cannot ever

**Answer: B** — NAT allows outbound-only.

### CP4-Q046 · Medium
What does CIDR 10.0.0.0/16 represent?

- A. 16 addresses
- B. 256 addresses
- C. 65,536 IP addresses from 10.0.0.0 to 10.0.255.255
- D. One IP

**Answer: C** — /16 leaves 16 host bits.

### CP4-Q047 · Medium
How many IPs are in a /24 subnet?

- A. 256 (AWS reserves 5, leaving 251 usable)
- B. 24
- C. 1024
- D. 65,536

**Answer: A** — AWS reserves the first four and last one.

### CP4-Q048 · Medium
Security groups vs NACLs: which is stateful?

- A. Both
- B. NACLs
- C. Neither
- D. Security groups

**Answer: D** — NACLs are stateless and need return rules.

### CP4-Q049 · Medium
Best way to let only the Order Service reach RDS on 5432?

- A. Use a public RDS endpoint
- B. RDS SG inbound 5432 with source = the Order Service's security group
- C. Inbound 5432 from 0.0.0.0/0
- D. Allow all traffic in the VPC

**Answer: B** — Reference SGs, not IP ranges.

### CP4-Q050 · Medium
Why spread subnets across at least two AZs?

- A. It improves encryption
- B. Required for IAM
- C. High availability if one AZ fails
- D. It is cheaper

**Answer: C** — ECS and RDS Multi-AZ rely on it.

### CP4-Q051 · Hard
What do VPC Flow Logs capture?

- A. CloudTrail events
- B. Metadata about IP traffic accepted/rejected in the VPC
- C. Packet payloads
- D. Application logs

**Answer: B** — Useful for network debugging and security.

### CP4-Q052 · Hard
Security group outbound default allows all. Least-privilege improvement?

- A. Restrict egress to required destinations (endpoints, RDS SG, HTTPS)
- B. Remove the SG
- C. Nothing can be done
- D. Allow inbound all instead

**Answer: A** — Egress control limits data exfiltration.

### CP4-Q053 · Easy
What is an internet gateway?

- A. A VPC component that enables internet access for public subnets
- B. A DNS server
- C. A NAT device
- D. A Kong node

**Answer: A** — One per VPC.

### CP4-Q054 · Medium
Where should an internet-facing load balancer sit?

- A. In public subnets, forwarding to tasks in private subnets
- B. In private subnets only
- C. On the tasks themselves
- D. Outside the VPC

**Answer: A** — Classic tiered layout.

### CP4-Q055 · Hard
Two VPCs have overlapping CIDRs. What problem appears?

- A. Faster routing
- B. Automatic NAT
- C. They cannot be peered/routed cleanly; plan non-overlapping ranges
- D. Nothing

**Answer: C** — Plan IP space early, especially for hybrid links.

### CP4-Q056 · Medium
A route table is associated with…

- A. A DynamoDB table
- B. A security group
- C. One or more subnets
- D. An IAM role

**Answer: C** — Routes decide where traffic goes.

### CP4-Q057 · Hard ★
An ECS task in a private subnet cannot pull its image from ECR and there is no NAT. Fix?

- A. Open SG inbound 0.0.0.0/0
- B. Add VPC interface endpoints for ECR (api, dkr) and the S3 gateway endpoint (plus logs)
- C. Use a bigger task
- D. Make the subnet public without IPs

**Answer: B** — Private image pulls need endpoints.

### CP4-Q058 · Easy
Which component should be the only public entry point to the API?

- A. The API gateway / load balancer in front of the services
- B. Each ECS task
- C. The SQS queue
- D. The RDS database

**Answer: A** — Kong fronts the services.

### CP4-Q059 · Medium ★
What is a NAT gateway charged for?

- A. Hourly plus per-GB processed, so VPC endpoints can reduce cost for AWS traffic
- B. Per Lambda invocation
- C. Per IAM user
- D. Nothing

**Answer: A** — Cost-aware networking.

### CP4-Q060 · Hard
Freshers' depth for VPC in this bootcamp is "guided". What does that mean for the lab?

- A. Skip networking
- B. Only read a blog post
- C. Build a multi-region VPC from scratch
- D. Use a provided template, explain each part, and draw the network diagram

**Answer: D** — G = template + help.

## Related
- [IAM least privilege](iam-least-privilege.md) — see-also: same checkpoint.
- [Secrets & configuration](secrets-configuration.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
