# Git & Version Control Interview Questions

This document contains interview questions focused on Git, version control concepts, and repository management.

## Basic Questions

### 1. What is Git?
**Answer:** 
**The Core Concept:**
Git is a free and open-source distributed version control system.

**Key Details:**
- It is designed to handle everything from small to very large projects with speed and efficiency.
- Unlike centralized systems (like SVN), every Git working directory is a full-fledged repository with complete history and full version-tracking capabilities.

**Example:** `git init` initializes a new repository.

**Reference:** [Git About](https://git-scm.com/about)

---

---

---

### 2. What is the difference between `git pull` and `git fetch`?
**Answer:** 
**The Core Concept:**
`git fetch` downloads new data from a remote repository, but it doesn't integrate any of this new data into your working files.

**Key Details:**
- `git pull` is essentially a `git fetch` followed immediately by a `git merge`.
- Fetching is safer because it lets you review changes before applying them.

**Example:** `git fetch origin` followed by `git merge origin/main`.

**Reference:** [Git Fetch vs Pull](https://git-scm.com/docs/git-pull)

---

---

## Intermediate Questions

---

## Intermediate Questions

### 3. What is a Git stash?
**Answer:** 
**The Core Concept:**
`git stash` temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later.

**Key Details:**
- It is useful when you need to quickly switch branches but aren't ready to commit your half-finished work.
- It operates on a stack, meaning you can stash multiple times.

**Example:** `git stash` to save, `git stash pop` to apply and remove from the stack.

**Reference:** [Git Stashing](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)

---

## Additional Depth (Architectural Focus)


---

---

### 4. What is a Git rebase and how does it differ from merge?
**Answer:** 
**The Core Concept:**
Git rebase integrates changes from one branch into another by moving or combining a sequence of commits to a new base commit. Unlike `git merge`, which creates a new merge commit and preserves the exact history of both branches, rebasing rewrites the project history to create a perfectly linear timeline.

**Key Details:**
- Rebasing results in a cleaner, more readable commit history, but it alters commit hashes. Therefore, you should never rebase commits that have already been pushed to a public, shared repository.
- Interactive rebasing (`-i`) is a powerful tool to squash, edit, or reorder commits before merging a feature branch.

**Example:** 
`git rebase main`

**Reference:** [Documentation](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

---

---

## Expert Questions

## Technical Questions

---

## Expert Questions

### 1. Write the Git commands to resolve a merge conflict in a file step-by-step.

**Example Solution:**
```bash
# 1. Start the merge that creates a conflict
git merge feature-branch

# 2. Check which files are in conflict
git status

# 3. Open the conflicted file and resolve markers manually
# <<<<<<< HEAD
# const url = "production-url";
# =======
# const url = "staging-url";
# >>>>>>> feature-branch

# 4. Add the resolved file
git add resolved_file.js

# 5. Complete the merge commit
git commit -m "merge: resolve conflict on API endpoints"
```

---

### 2. Write Git commands to squash the last 3 local commits before pushing.

**Example Solution:**
```bash
# Start an interactive rebase for the last 3 commits
git rebase -i HEAD~3

# In the interactive editor, keep the first commit as "pick" and change the next two to "squash" or "s":
# pick a1b2c3d Commit number 1
# squash e5f6g7h Commit number 2
# squash i9j0k1l Commit number 3

# Save and exit. An editor will open to edit the combined commit message.
# Save the new squashed message and verify using:
git log --oneline
```

---

## Technical Questions

### 1. Write the Git commands to resolve a merge conflict in a file step-by-step.

**Example Solution:**
```bash
# 1. Start the merge that creates a conflict
git merge feature-branch

# 2. Check which files are in conflict
git status

# 3. Open the conflicted file and resolve markers manually
# <<<<<<< HEAD
# const url = "production-url";
# =======
# const url = "staging-url";
# >>>>>>> feature-branch

# 4. Add the resolved file
git add resolved_file.js

# 5. Complete the merge commit
git commit -m "merge: resolve conflict on API endpoints"
```

### 2. Write Git commands to squash the last 3 local commits before pushing.

**Example Solution:**
```bash
# Start an interactive rebase for the last 3 commits
git rebase -i HEAD~3

# In the interactive editor, keep the first commit as "pick" and change the next two to "squash" or "s":
# pick a1b2c3d Commit number 1
# squash e5f6g7h Commit number 2
# squash i9j0k1l Commit number 3

# Save the new squashed message and verify using:
git log --oneline
```

### 3. Write Git commands to rollback a pushed commit without rewriting Git history.

**Example Solution:**
```bash
# Revert the specific commit using git revert (creates a new commit reverting changes)
git revert a1b2c3d4

# Push the revert commit to remote safely
git push origin main
```

### 4. [Self-Practice] Design a high-throughput, fault-tolerant system leveraging key principles of Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 5. [Self-Practice] Write a custom utility to validate input schemas and sanitize payloads in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 6. [Self-Practice] Implement a comprehensive error-boundary and logging module for a Git & Version Control application.

*(Challenge question for self-study and practical project implementation.)*

### 7. [Self-Practice] Optimize memory consumption and execution hot-paths under high load in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 8. [Self-Practice] Write an automated unit testing suite targeting complex race-conditions in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 9. [Self-Practice] Create a localized internationalization (i18n) helper integrated with Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 10. [Self-Practice] Build a secure token-based authentication handshake flow within Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 11. [Self-Practice] Design a distributed caching and invalidation strategy for heavy Git & Version Control operations.

*(Challenge question for self-study and practical project implementation.)*

### 12. [Self-Practice] Create a CLI tool to automate scaffolding and deployment of Git & Version Control configurations.

*(Challenge question for self-study and practical project implementation.)*

### 13. [Self-Practice] Implement a real-time event-driven pub/sub handler using Git & Version Control event structures.

*(Challenge question for self-study and practical project implementation.)*

### 14. [Self-Practice] Draft an architectural decision record (ADR) comparing Git & Version Control with its primary competitors.

*(Challenge question for self-study and practical project implementation.)*

### 15. [Self-Practice] Create a mock framework to isolate and test external integrations in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 16. [Self-Practice] Write a custom telemetry wrapper to output Git & Version Control performance metrics to Prometheus/Grafana.

*(Challenge question for self-study and practical project implementation.)*

### 17. [Self-Practice] Design a zero-downtime blue-green roll-out plan for a database or service utilizing Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 18. [Self-Practice] Implement a circuit-breaker pattern to gracefully degrade service during Git & Version Control failures.

*(Challenge question for self-study and practical project implementation.)*

### 19. [Self-Practice] Write an automated script to detect memory leaks and unhandled promise rejections in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 20. [Self-Practice] Build a user-friendly audit log tracking all state mutations and access events in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 21. [Self-Practice] Design an API gateway integration mapping REST inputs to Git & Version Control data layers.

*(Challenge question for self-study and practical project implementation.)*

### 22. [Self-Practice] Implement a rate-limiter with custom sliding-window configurations in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 23. [Self-Practice] Create a backup and recovery automated script for preserving Git & Version Control state repositories.

*(Challenge question for self-study and practical project implementation.)*

### 24. [Self-Practice] Design a microservice boundary that encapsulates Git & Version Control logic without tight coupling.

*(Challenge question for self-study and practical project implementation.)*

### 25. [Self-Practice] Build a role-based access control (RBAC) middleware verifying permissions on Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 26. [Self-Practice] Write an optimized compiler or parser configuration to bundle Git & Version Control files for web browsers.

*(Challenge question for self-study and practical project implementation.)*

### 27. [Self-Practice] Implement a dead-letter queue (DLQ) pattern for handling corrupted messages in Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 28. [Self-Practice] Create an automated health-check endpoint monitor checking Git & Version Control connection integrity.

*(Challenge question for self-study and practical project implementation.)*

### 29. [Self-Practice] Implement a secure CORS and CSP policy wrapper for endpoints exposing Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

### 30. [Self-Practice] Refactor a legacy monolithic module into modern, modular ES modules using Git & Version Control.

*(Challenge question for self-study and practical project implementation.)*

