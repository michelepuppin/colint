import subprocess
import sys


def run_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(1)


def code_format(args="."):
    """Run black code formatter."""
    run_command(f"python3 -m black {args}")
    print(args)


def flake_lint(args="."):
    """Run flake8 linter."""
    run_command(f"python3 -m flake8 {args}")


def isort(args="."):
    """Run isort for import sorting."""
    run_command(f"python3 -m isort {args}")


def lint(args="."):
    """Run all linting tools: isort, black, flake8."""
    isort(args)
    code_format(args)
    flake_lint(args)


def clean():
    """Clean up Python bytecode and cache files."""
    run_command('find . -type f -name "*.py[co]" -delete')
    run_command('find . -type d -name "__pycache__" -delete')


def main():
    tasks = {
        "code-format": code_format,
        "flake-lint": flake_lint,
        "isort": isort,
        "lint": lint,
        "clean": clean,
    }

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <task> [args]")
        sys.exit(1)

    task = sys.argv[1]
    args = sys.argv[2:] if len(sys.argv) > 2 else ["."]
    if task in tasks:
        tasks[task](*args)
    else:
        print(f"Unknown task: {task}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    print("Done!")
