"""Reference for a small branch and a reviewable change; terminal steps stay manual."""

# In your own scratch repository from practice/git-starter, with an initial commit:
# git switch -c feature/summary-docs
# Edit README.md: explain that [] returns None and [0] returns 0.0.
# git diff
# git add README.md
# git diff --staged
# git commit -m "Clarify missing data and zero measurements"
# git log --oneline --graph --all
# With a configured remote that you own or are authorized to use:
# For a NEW empty remote, first publish the baseline target:
# git push -u origin main
# git push -u origin feature/summary-docs
# Open a pull request in GitHub with base=main and compare=feature/summary-docs.
# Without remote access, prepare an offline review packet instead; see REVIEW_GUIDE.md.

review_packet = {
    "problem": "Readers can confuse missing data with a measured zero.",
    "behavior": "Empty input gives None; a zero measurement gives 0.0.",
    "check": "Compare the README with summary.mean and evaluate both examples.",
    "question": "Can the recipient distinguish these two cases?",
}
assert "None" in review_packet["behavior"]
print(review_packet)
