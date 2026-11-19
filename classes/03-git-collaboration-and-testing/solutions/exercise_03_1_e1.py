"""Reference plan: run these commands manually in a separate scratch repository."""

# First COPY practice/git-starter to a NEW folder outside the course checkout.
# In a terminal in that copy:
# git init -b main
# git config user.name "Your Name"
# git config user.email "your-chosen-address@example.org"
# git status
# git add README.md summary.py .gitignore
# git diff --staged
# git commit -m "Add quantity summary starter"
# Edit README.md to document the empty-input contract.
# git diff
# git add README.md
# git diff --staged
# git commit -m "Document empty-input behavior"
# git status --short
# git log --oneline -2

reference_plan = [
    "inspect",
    "stage named files",
    "review staged diff",
    "commit",
    "inspect",
]
assert reference_plan.index("review staged diff") < reference_plan.index("commit")
print(reference_plan)
