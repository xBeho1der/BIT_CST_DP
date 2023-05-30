# Design Pattern

## 1. Installation: Setup the environment

### Prerequisites

You must have a python environment on your server, or you can install it in its official website.

Python=3.11.2 is requested.

You can run the following scripts to run the configuration in a powershell terminal:
```bash
setup.sh
```

or you can run the following commands to build the environments
```bash
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r .\requirements.txt
```

or if your python environment is named python3

```bash
python3 -m pip install --upgrade pip
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install -r .\requirements.txt
```
