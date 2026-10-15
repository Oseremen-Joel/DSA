# Git Workflow — DSA Repository

A quick reference for the Git commands and workflow used for your DSA project.

## 1. Open your repository

Your repository is located at:

```bash
~/gitstuff/DSA
```

Open a terminal and run:

```bash
cd ~/gitstuff/DSA
```

## 2. The usual workflow

### Step 1 — Get the latest changes

```bash
git pull
```

Fetches changes from the remote repository and integrates them into your current branch. This is especially useful before working on a different computer.

### Step 2 — Check the repository status

```bash
git status
```

Shows your current branch and whether files are modified, staged, or untracked.

### Step 3 — Make and review changes

Edit your code and notes in VS Code. Then inspect changes that have not been staged:

```bash
git diff
```

Use the down and up arrow to move through the list

### Step 4 — Stage changes

Stage all changes beneath the current directory:

```bash
git add .
```

Or stage one specific file:

```bash
git add path/to/file.py
```

Staging chooses which changes will be included in the next commit.

### Step 5 — Review staged changes

```bash
git diff --cached
```

Check that the staged changes are the ones you intend to commit.

### Step 6 — Commit

```bash
git commit -m "Describe the changes"
```

A commit records the staged changes in your **local** Git history. Use a short, specific message, for example:

```bash
git commit -m "Add binary tree traversals"
```

### Step 7 — Push to the remote

```bash
git push
```

Uploads your local commits to the remote repository, making them available on GitHub and other computers.

### Quick version

```bash
git pull
git status
# Make and review changes
git diff
git add .
git diff --cached
git commit -m "Describe the changes"
git push
```

You do not need to commit every tiny edit. Commit when you have a meaningful set of changes you want to save.

## 3. Useful commands

| Command | What it does |
|---|---|
| `git status` | Shows the current branch and working-tree changes |
| `git diff` | Shows unstaged changes |
| `git diff --cached` | Shows staged changes |
| `git add .` | Stages changes under the current directory |
| `git add filename` | Stages a specific file |
| `git commit -m "message"` | Records staged changes locally |
| `git push` | Uploads local commits to the remote |
| `git pull` | Fetches and integrates remote changes |
| `git log --oneline` | Shows a compact commit history |
| `git branch` | Lists local branches and marks the current branch |
| `git remote -v` | Shows configured remote URLs |
| `git show --stat` | Summarises the latest commit and the files it changed |

## 4. Your repository so far

- **Repository:** `~/gitstuff/DSA`
- **Branch:** `main`
- **Remote:** Connected to `origin` (check its URL with `git remote -v`)
- **Previously noted commits:**
  - `aa083d5`
  - `f085afa`

Check the current state with:

```bash
git status
git log --oneline
git remote -v
```

Commit messages and the current state can change, so use these commands to confirm them rather than relying on this note alone.

## 5. Working across two computers

GitHub acts as the bridge between the local copies of your repository.

**On the computer where you start working:**

```bash
git pull
```

Make changes, then save and share them:

```bash
git add .
git commit -m "Describe the changes"
git push
```

**On the other computer:**

```bash
git pull
```

This brings down the changes you pushed.

Push work you want to keep available before switching computers. Avoid editing the same files independently on both computers before syncing, as that can cause merge conflicts.

## 6. If something goes wrong

### I don't know what changed

```bash
git status
git diff
```

Start here before running commands that change files or history.

### I staged the wrong changes

Unstage everything while keeping your edits in the working files:

```bash
git restore --staged .
```

Or unstage one file:

```bash
git restore --staged path/to/file
```

These commands do **not** delete your file edits.

### I want to inspect previous commits

```bash
git log --oneline
git show
```

`git show` displays details of the latest commit by default. To inspect a particular commit:

```bash
git show COMMIT_ID
```

### Git reports a merge conflict

1. Run `git status` to find the conflicted files.
2. Open each file and resolve the conflict markers, keeping the correct content.
3. Stage the resolved files with `git add path/to/file`.
4. Follow Git's instructions to finish the merge or other operation.

Don't blindly overwrite a conflicted file if you need changes from both versions.

## 7. Know the difference

- **Working changes:** Edits in your files that have not been staged.
- **Staged changes:** Edits selected for the next commit.
- **Commit:** A snapshot saved in your local Git history.
- **Push:** Sends local commits to the remote repository.
- **Pull:** Brings remote changes into your local repository.

A commit is not the same as a push: committing saves work locally; pushing shares it with the remote.

## 8. Safety habits

- Run `git status` whenever you are unsure.
- Review `git diff` before staging and `git diff --cached` before committing.
- Use clear commit messages.
- Pull before starting work on another computer.
- Avoid `git reset --hard`, force-pushing, or deleting branches unless you understand the consequences; these can discard work or rewrite history.
