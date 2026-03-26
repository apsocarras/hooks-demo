# hooks-demo

Demo repository for the "Git Hooks & Task Runners" presentation.

## Structure

```
hooks-demo/
├── foo/    # Python project with NO justfile
│           # → set_justfile_symlinks.go will create a symlink here
└── bar/    # Python project with its own justfile
            # → set_justfile_symlinks.go will print the diff
```

## Demo

```bash
# From ~/work/bla — installs symlink in foo/, prints diff for bar/
just set-justfile-symlinks

# From either project — installs pre-commit + pre-push hooks
cd foo && just install-hooks
cd bar && just install-hooks
```
