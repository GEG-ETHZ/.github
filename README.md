# .github

Organisation-wide defaults for `GEG-ETHZ`.

- **`profile/README.md`** is the text on the
  [organisation page](https://github.com/GEG-ETHZ).
- **`.github/ISSUE_TEMPLATE/`** holds the default issue forms: Task, Bug, Feature and
  Topic. Every repository without its own `.github/ISSUE_TEMPLATE/` folder uses them.
  Each form sets the issue type and adds the issue to the
  [GEG-AI board](https://github.com/orgs/GEG-ETHZ/projects/7). Blank issues are off.
- **`.github/workflows/gitleaks.yml`** scans a repository's full history for secrets.
  An organisation ruleset requires it on pull requests in every repository it targets,
  so no repository pins gitleaks in its own CI. Why, and how to set it up:
  `computing/code/secrets.md` in the `geg-ops` repository.

How the board, issue types and forms are meant to be used is documented in
`operations/project-management/` in the `geg-ops` repository (team members only).

To change a form, change it here. `scripts/check_issue_forms.py` runs on every pull
request and checks that each form sets an issue type, that Task is the first form, and
that blank issues stay off. A repository that adds its own
`.github/ISSUE_TEMPLATE/` folder stops getting these forms, so do not add one unless
that repository really needs different forms.
