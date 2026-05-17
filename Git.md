# Git & Version Control Interview Questions

This document contains interview questions focused on Git, version control concepts, and repository management.

## Basic (Easy)

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
\n## Additional Depth (Architectural Focus)\n
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
