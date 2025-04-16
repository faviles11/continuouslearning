# 🧠 Git & GitHub Tips for SRE / DevOps

## Basic Commands

- `git init` – Initialize a Git repository.
- `git clone <repo-url>` – Clone a remote repository.
- `git status` – Check current changes.
- `git add <file>` – Stage a file.
- `git commit -m "message"` – Commit staged changes.
- `git push` – Push commits to remote.
- `git pull` – Fetch and merge remote changes.
- `git fetch` – Only fetch remote changes (no merge).
- `git checkout -b <branch>` – Create and switch to a new branch.

## Reverting and Resetting

- `git revert <commit>` – Safely undo a commit by creating a new one.
- `git reset --hard <commit>` – Dangerous! Resets history (avoid on shared branches).
- `git clean -fd` – Remove untracked files and directories.

## Branching and Merging

- Use branches to isolate features, fixes, or environments.
- `git merge <branch>` – Merge another branch into your current one.
- Resolve merge conflicts manually, then:
  ```bash
  git add <file>
  git commit
  ```

## Tags & Releases

- Use tags to mark versioned releases:
  ```bash
  git tag v1.0.0
  git push origin --tags
  ```

##GitHub Best Practices

### Repositories

- Use meaningful names, README, and `.gitignore` files.
- Enable **branch protection rules** (e.g. require PR reviews).

### Security Tips

- Enable **2FA** on your GitHub account.
- Use **GitHub Secrets** in workflows (`${{ secrets.MY_SECRET }}`).
- Regularly review authorized GitHub Apps and OAuth tokens.

### GitHub Actions CI/CD

- Place workflow files in `.github/workflows/`.
- Example structure:

  ```yaml
  name: CI Pipeline

  on: [push, pull_request]

  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Run tests
          run: npm test
  ```

- Keep secrets safe (e.g., `ARM_CLIENT_ID`, `ARM_SUBSCRIPTION_ID` for Terraform).

### Git + Terraform Tips (for IaC workflows)

- Never commit `.tfstate` files – use remote backends (e.g., Azure Storage).
- Use `terraform plan -out=tfplan` in PRs and only `apply` on merge.
- Validate with `terraform validate` and lint with `tflint` or `checkov`.

### Useful Commands for Inspection

- `git log --oneline --graph --decorate` – Visualize commit history.
- `git diff` – See changes between commits or branches.
- `git blame <file>` – Identify who modified which line.

### Pull Request Guidelines

- One feature/fix per PR.
- Write clear, concise commit messages.
- Use draft PRs for work in progress.
- Always link to related issues if applicable.

```

```
