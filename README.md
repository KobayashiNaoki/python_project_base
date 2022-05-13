# Python Project Base Repo
This repo is the simple python project base.

References:
- [Tutorials of python packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- Details are in [SETUP TOOLS](https://setuptools.pypa.io/en/latest/setuptools.html)
- About setup.cfg is in [Configuring setuptools using setup.cfg files](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)



## How to packaging
1. Install build command
   ```bash
   pip install build
   ```
2. Run build
   ```bash
   python -m build
   ```


## How to run test
1. Install pytest
   ```bash
   pip install pytest
   ```
2. Run pytest
   ```bash
   pytest tests/
   ```


## Repo structure
```
project_root_dir/
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── sample_package/
│       ├── __init__.py
│       └── sample_code.py
└── tests/
    └── test_sample_code.py
```
