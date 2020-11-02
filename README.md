# Python Default Project

## Setup

1. [Install](https://pipenv.pypa.io/en/latest/#install-pipenv-today) ```pipenv```. You might want to set ```export PIPENV_VENV_IN_PROJECT=1``` in your ```.bashrc/.zshrc``` for local virtual environments.

2. Clone repository into preferred directory

    ```
    git clone https://github.com/jomazi/Python-Default
    ``` 

3. Install packages
   
   ```
   cd Python-Default/
   pipenv install --dev
   ```

4. Init ```.env``` file

    ```
    mv .example.env .env
    ```

5. Activate virtual environment

    ```
    pipenv shell
    ```

6. Test setup

    ```
    pipenv run main
    ```

7. Install git hooks

    ```
    pipenv install pre-commit
    ```

Note: To deactivate environment again, simply run `deactivate`.

## Testing

```
pipenv run test
```

## Git Workflow

To coordinate the software development process a set of guidelines are necessary. It is helpful to rely on the [GitHub Flow](https://guides.github.com/introduction/flow/) strategy which defines a branch-based workflow. Essentially, it boils down to the following steps:

1. Create a `main/master` branch. This is done automatically by creating a new project.
2. Create an issue that describes a bug or asks for an additional feature.
3. Add features or solve bug fixes by creating new branches via `git checkout`. Those branches have to be named
`feature-*` or `fix-*` accordingly. Assign the issue that the code changes are meant to solve.
4. Commit to new feature or fix branch. Make sure that you also write `tests` which cover the new features or show that the bug is solved. They should run automatically using the [GitHub CI system](https://docs.github.com/en/free-pro-team@latest/actions/guides/about-continuous-integration).
5. Create pull request once you are done with your work. Use the @mention system to get the maintainer's attention or ask questions to specific people. 
6. Optional discussion about the pull request. If necessary, additional changes can be made.
7. New branch is merged into `main/master` branch.

## Resources

- [Pipenv Cheatsheet](https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55)
- [pre-commit Docs](https://pre-commit.com/)
