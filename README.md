# swasthya-setu
AI-driven Multilingual Health Chatbot

## Contribution Rules
1. Please raise a PR before merging a new feature — it helps contributors track your progress.
2. PRs should be merged in the presence of at least 2 developers.
3. Provide a short and clear commit message that briefly overviews the changes made.
4. Every PR must be linked to an issue (create one if it doesn’t exist).
5. Avoid committing directly to the main branch — always use feature branches.
6. If you’re working on a large feature, please update progress in the project board channel regularly.
7. Keep sensitive information (API keys, tokens, credentials) out of commits — use .env files and .gitignore.
8. Before merging, run all tests and linters locally and ensure the build passes.

Respect inclusive communication and maintain a collaborative, open-source friendly environment.

## Helpful commands
### Clone repo 
git clone https://github.com/Rishabh9306/swasthya-setu.git

### Check remotes
git remote -v

### Create new branch for a feature/bugfix
git checkout -b feature/branch-name

### Switch branches
git checkout main

### Delete branch locally
git branch -d feature/branch-name

### Delete branch on GitHub
git push origin --delete feature/branch-name

### Stage changes
git add <file>
git add .        # stage all

### Commit with message
git commit -m "short, clear message"

### Amend last commit (if not pushed yet)
git commit --amend -m "new message"

### Push branch to GitHub
git push origin feature/branch-name

### Pull latest changes from main
git pull origin main

### Fetch all branches
git fetch origin

### Checkout someone’s PR branch
git checkout -b review/xyz origin/feature/xyz

### Reference issue in commit/PR
git commit -m "fix: corrected bug in NLP pipeline (#23)"

### Auto-close issue when PR merges
git commit -m "feat: added Hindi language support, closes #45"

### Rebase with main (clean history)
git checkout feature/xyz
git fetch origin
git rebase origin/main

### Abort rebase if things break
git rebase --abort

## PR Workflow
(1) Create feature branch & push
git checkout -b feature/xyz
git push origin feature/xyz

(2) Go to GitHub → Open Pull Request from feature/xyz → main

(3) After PR review & approval:
Merge via GitHub UI (squash/rebase/merge commit)

(4) Clean up local branches
git checkout main
git pull origin main
git branch -d feature/xyz
