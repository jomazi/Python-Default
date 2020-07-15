# Python Default Project

## Setup

1. [Install](https://pipenv.pypa.io/en/latest/#install-pipenv-today) ```pipenv```. You might want to set ```export PIPENV_VENV_IN_PROJECT=1``` in your ```.bashrc/.zshrc``` for local virtual environments.

2. Clone repository into preferred directory

    ```
    git clone https://github.com/jomazi/Python-Default
    ``` 

3. Activate virtual environment

    ```
    cd Python-Default/
    pipenv shell
    ```

4. Test Setup

    ```
    python -m main
    ```

5. Install Git Hooks

    ```
    pipenv pre-commit install
    ```

## Testing

```
pipenv run tests
```

## Resources

- [Pipenv Cheatsheet](https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55)
- [pre-commit Docs](https://pre-commit.com/)
