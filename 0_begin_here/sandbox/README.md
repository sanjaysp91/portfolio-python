# sandbox/README.md

Purpose
- A lightweight sandbox to evaluate scalable, long-term strategies for creating and managing Python environments.
- Use this repo to run reproducible experiments, compare approaches, and collect results.

Goals
- Compare isolation, reproducibility, portability, and developer ergonomics.
- Test tools for multi-Python support, dependency resolution, CI/CD integration, and deployment.
- Produce clear, repeatable experiment artifacts and recommendations.

Scope
- Local and CI workflows (macOS / Linux; Windows optional).
- Tools to test: venv, virtualenv, pyenv, pyenv-virtualenv, pipx, pip-tools (pip-compile), poetry, pipenv, hatch, conda/mamba, nix, Docker, direnv, tox/nox.

Repository structure (suggested)
- /experiments/
    - /001-venv/        → experiment folder with step-by-step README and scripts
    - /002-poetry/
    - /003-pyenv/
    - ...
- /results/           → structured results (results.md or CSV)
- /scripts/           → helper scripts used across experiments
- README.md (this file)

Experiment template (create inside each experiment)
- README.md:
    - Purpose and hypothesis
    - Commands to reproduce the environment (copy/paste)
    - Test steps (install, run unit tests, package, CI run)
    - Expected artifacts (lock files, wheel, Docker image)
    - Cleanup steps
- examples:
    - Create venv:
        - python3 -m venv .venv
        - source .venv/bin/activate
        - python -m pip install --upgrade pip
        - pip install -r requirements.txt
    - Use pyenv:
        - pyenv install 3.x.x
        - pyenv local 3.x.x
        - python -m pip install -r requirements.txt
    - Poetry minimal:
        - poetry init --no-interaction
        - poetry add <package>
        - poetry lock

Metrics to record
- Reproducibility: can an environment be rebuilt verbatim from the repo?
- Isolation: does the environment avoid host contamination?
- Ease of use: developer UX and onboarding time
- CI friendliness: setup time and reliability in CI runners
- Storage/size: disk footprint and image sizes (if Docker)
- Speed: env creation and install times
- Multi-Python support: ease of testing multiple interpreters

Automation & CI
- Use GitHub Actions or equivalent to run baseline scenarios:
    - matrix: python: [3.10, 3.11, 3.12]
    - jobs: create env, install deps from lockfile, run tests
- Example succinct job steps:
    - uses: actions/checkout@v4
    - run: python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && pytest

Recording results
- Add a results.md or results.csv in /results/ with:
    - experiment id, tool, python versions, reproducible (yes/no), notes, time, size
- Keep one-line summary at top of each experiment README.

Best practices to test
- Always pin dependencies and generate lock files.
- Test both host-based envs and containerized (Docker) builds.
- Compare deterministic builds (hash/lock) vs unconstrained installs.
- Validate prod packaging: wheel, sdist, Docker image.

Cleanup
- Provide `./cleanup.sh` per experiment to remove envs, caches, and artifacts.

Notes
- Keep experiments small and focused; iterate by codifying best practices found.

GitHub Copilot
- Use this sandbox to capture concrete recommendations; iterate experiments into a final reproducible workflow.
