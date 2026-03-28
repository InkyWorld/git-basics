# git-basics

Learning project for Lab 3: CI/CD pipeline architecture.

## Pipeline stages

This repository uses a multi-stage GitHub Actions workflow:

`test -> build -> deploy_staging -> verify_staging -> deploy_production`

- `test`: runs unit tests from `tests/test_core.py`
- `build`: creates build artifact `artifact/build.txt`
- `deploy_staging`: simulates staging deployment using the artifact
- `verify_staging`: runs post-deploy smoke verification
- `deploy_production`: simulates production deployment after manual approval

## Manual approval for production

The `deploy_production` job uses GitHub Environment `production`.
To enable manual approval:

1. Open repository settings.
2. Go to Environments.
3. Create environment `production`.
4. Add `Required reviewers`.

After that, production deployment will wait for approval.

## How to demonstrate failures required by the lab

1. Break unit test in `tests/test_core.py` and push commit.
2. Confirm pipeline fails on stage `test`.
3. Fix the test and push again.
4. Run workflow manually with input `force_verify_fail=true`.
5. Confirm pipeline fails on `verify_staging` and production is not executed.
6. Run again with `force_verify_fail=false`.

