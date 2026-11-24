---
id: 20261124-cp0-git-github-flow
title: CP0 · Git & GitHub flow
tags: [question-bank, cp0]
created: 2026-11-24
updated: 2026-11-24
related: [20261124-cp0-github-copilot, 20261124-cp0-jira-confluence, 20261124-exam-blueprint]
summary: 20 CP0 questions on Git & GitHub flow (8 easy, 9 medium, 3 hard) with answers and explanations.
---

# CP0 · Git & GitHub flow

> Summary: 20 CP0 questions on Git & GitHub flow (8 easy, 9 medium, 3 hard) with answers and explanations.

## Context
Part of the CP0 Onboarding & Go essentials bank. Exam questions marked ★ are in the current exam (seed exam-v1-CP0).

## Questions

### CP0-Q001 · Easy
Which command creates a new branch and switches to it in one step?

- A. git checkout feature/x --new
- B. git merge feature/x
- C. git branch -m feature/x
- D. git switch -c feature/x

**Answer: D** — git switch -c (or git checkout -b) creates the branch and checks it out.

### CP0-Q002 · Easy
What does `git status` show?

- A. The list of remote repositories
- B. The diff between two remote branches
- C. Changed, staged and untracked files in the working tree
- D. The commit history of the branch

**Answer: C** — git status reports the state of the working tree and the staging area.

### CP0-Q003 · Easy
Which command stages a single file for the next commit?

- A. git push path/to/file.go
- B. git stage --all
- C. git add path/to/file.go
- D. git commit path/to/file.go

**Answer: C** — git add moves changes into the staging area (index).

### CP0-Q004 · Easy
What is a pull request on GitHub?

- A. A request to clone a repository
- B. A command that downloads the latest commits
- C. A GitHub Actions job that pulls Docker images
- D. A request to review and merge changes from one branch into another

**Answer: D** — A PR proposes merging a branch and is where review happens.

### CP0-Q005 · Easy ★
Which command downloads commits from the remote AND merges them into the current branch?

- A. git pull
- B. git fetch
- C. git clone
- D. git push

**Answer: A** — git pull = git fetch + merge (or rebase if configured).

### CP0-Q006 · Easy
What does `git fetch` do?

- A. Resets the working tree to HEAD
- B. Deletes local branches already merged
- C. Uploads local commits to the remote
- D. Downloads remote commits without changing your working branch

**Answer: D** — fetch only updates remote-tracking refs such as origin/main.

### CP0-Q007 · Easy
A good commit message for the bootcamp should start with…

- A. The date and time
- B. A random emoji
- C. The Jira key and a short imperative summary, e.g. "ORD-12 Add create order handler"
- D. The trainee's name

**Answer: C** — Jira key + imperative summary links work to tickets and reads well in history.

### CP0-Q008 · Medium
You committed to main by mistake but have not pushed. What is the safest way to move the commit to a new branch?

- A. Create the branch at HEAD, then reset main back one commit
- B. Run git revert on the remote
- C. Delete the repository and clone again
- D. Force-push main to the remote

**Answer: A** — git branch fix; git reset --hard HEAD~1 on main keeps the commit on the new branch.

### CP0-Q009 · Medium
What does a merge conflict mean?

- A. Both branches changed the same lines and Git cannot decide which to keep
- B. The remote repository is offline
- C. Two people pushed at the same second
- D. The branch name already exists

**Answer: A** — Conflicts must be resolved manually, then staged and committed.

### CP0-Q010 · Medium ★
What is the purpose of `.gitignore`?

- A. To encrypt secret files in the repo
- B. To ignore failing tests in CI
- C. To stop Git from tracking files such as build output, binaries and local env files
- D. To hide files from code reviewers

**Answer: C** — Ignored files are not added; it does not protect files already committed.

### CP0-Q011 · Medium ★
What is the difference between `git revert` and `git reset --hard`?

- A. revert only works on merge commits
- B. revert deletes the remote branch; reset deletes the local one
- C. They are identical
- D. revert creates a new commit that undoes changes; reset moves the branch pointer and can discard commits

**Answer: D** — revert is safe for shared history; reset rewrites history.

### CP0-Q012 · Medium
Branch protection on main typically requires…

- A. That main is deleted after each release
- B. That only the repo owner can read main
- C. A passing CI check and at least one approved review before merge
- D. That every commit is signed by GitHub Copilot

**Answer: C** — Protection rules enforce reviews and status checks.

### CP0-Q013 · Medium
What does "squash and merge" do on a PR?

- A. Combines all PR commits into one commit on the target branch
- B. Merges without running CI
- C. Deletes all commits in the PR
- D. Rebases main onto the PR branch

**Answer: A** — Squash keeps main history to one commit per PR.

### CP0-Q014 · Medium
You need the latest main in your feature branch with linear history. Which command fits?

- A. git rebase origin/main (after git fetch)
- B. git push --force origin main
- C. git stash drop
- D. git clone origin/main

**Answer: A** — Rebasing replays your commits on top of the updated main.

### CP0-Q015 · Medium
What does `git stash` do?

- A. Deletes all untracked files
- B. Squashes the last commits
- C. Pushes changes to a hidden remote branch
- D. Temporarily shelves uncommitted changes so you can switch context

**Answer: D** — git stash pop restores the shelved changes.

### CP0-Q016 · Hard
You accidentally committed an AWS access key and pushed it. What must happen FIRST?

- A. Revoke/rotate the key immediately, then clean the history
- B. Delete the line and push a new commit
- C. Make the repository private
- D. Rename the file

**Answer: A** — Once pushed the key is compromised; rotation comes before history cleanup.

### CP0-Q017 · Hard ★
Why should you avoid `git push --force` on a shared branch?

- A. It overwrites remote history and can delete teammates' commits
- B. It is slower than a normal push
- C. It only works on tags
- D. It disables branch protection permanently

**Answer: A** — Use --force-with-lease on your own branches; never force-push shared branches.

### CP0-Q018 · Hard
What does `git push --force-with-lease` add over `--force`?

- A. It refuses to overwrite if the remote has commits you have not seen
- B. It pushes to all remotes at once
- C. It signs the commits automatically
- D. It squashes before pushing

**Answer: A** — The lease check protects against overwriting others' work.

### CP0-Q019 · Easy ★
What is a "remote" in Git?

- A. A commit that was reverted
- B. A file stored outside the repository
- C. A named reference to another copy of the repository, e.g. origin on GitHub
- D. A branch that has been deleted

**Answer: C** — origin is the default remote created by git clone.

### CP0-Q020 · Medium
What should a pull request description include in this bootcamp?

- A. A list of every file in the repository
- B. What changed, why, how it was tested, and the Jira key
- C. Only the trainee's name
- D. The full source code pasted again

**Answer: B** — A clear description speeds up review and traceability.

## Related
- [GitHub Copilot](github-copilot.md) — see-also: same checkpoint.
- [Jira & Confluence](jira-confluence.md) — see-also: same checkpoint.
- [Exam blueprint](../program/exam-blueprint.md) — supports: how these questions are drawn into the exam.
