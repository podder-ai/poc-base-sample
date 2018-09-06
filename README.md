# poc-base

This is base repository for PoC (Proof of Concept) code.
Boilerplate project for creating python task using the [Pipeline-framework](https://github.com/podder-ai/pipeline-framework).

## How to implement your code

### Source code directory

```
$ tree . -L 2
.
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   └── task.py  # main task implementation
├── data
│   └── tmp      # where to put your data 
├── framework    # framework code base
│   ├── __init__.py
│   ├── __pycache__
│   ├── config.py
│   ├── context.py
│   ├── file.py
│   ├── logger.py
│   └── tasks
├── main.py
├── requirements.txt # add required packages here
├── .env.sample # sample of environment variables 
├── .env # where to add your environment variables 
```

### How to implement a task class

Add your code to `app/task.py`. 

#### Implementation sample

Please check task sample here [Sample](https://github.com/podder-ai/poc-base-sample)

#### __init__: Initialize task instance 

```python
def __init__(self, context: Context) -> None:
    self.context.logger.debug("Initiate task...")
    super().__init__(context)
```

#### execute: Main process

```python
def execute(self) -> None:

    self.context.logger.debug("START processing...")
    
    self.yourProcess(self.args.input_path)
    
    self.context.logger.debug("Completed.")
        
```

#### set_arguments: Arguments

```python
def set_arguments(self, parser) -> None:
    
    parser.add_argument('--input_path', dest="input_path", help='set input path', default='.')

```

### Framework API

Some framework APIs you can use for your implementation.

#### Logging

You can output logs with `self.context.logger`. `logger` is just a wrapper of logging. For further logging usage, please check [here](https://docs.python.org/3.6/library/logging.html)

```python
self.context.logger.debug("debug")
self.context.logger.info("info")
```

#### Environment variables

Please config  your environment variables in `.env` file.
You can access to environment variables with `self.context.config.get([YOUR_ENV_KEY])`.

```dotenv
ENV=local
```
```python
self.context.config.get("ENV") # local
```

#### Command Line Arguments

You can access to arguments through `self.args` after set your arguments through `set_arguments` method.

Adding command line arguments implementation
```python
parser.add_argument('--model', dest="model_path", help='set model path')
```

Framework uses ArgumentParser in background. You can check usage of ArgumentParser usage [here](https://docs.python.org/3.6/library/argparse.html#argparse.ArgumentParser)

Get command line arguments
```python
model_path = self.args.model_path
```

#### Data files

You can get absolute path under `data` directory by `self.context.file.get_path`. Please put your files (data set or any necessary files) under `data` directory.

```python
self.context.file.get_path('sample.csv')
```

### Run

Run your task with argument
```bash
$ python main.py --model your_model_path
```

## How to run your code

### For Mac os, Linux user

```bash
# clone poc-base
$ git clone git@github.com:podder-ai/poc-base.git
$ cd poc-base
# configure environment variables if require
$ cp .env.sample .env
# enable python3
$ python3 -m venv env
$ source env/bin/activate
# install required libraries
$ pip install -r requirements.txt
# run sample code
$ python main.py
```

### For Windows user with PowerShell

If using Powershell, the activate script is subject to the execution policies on the system. By default on Windows 7, the system's excution policy is set to `Restricted`, meaning no scripts as virtualenv activation script are allowed to be executed. 

In order to use the script, you can relax your system's execution policy to `Unrestricted`, meaning all scripts on the system can be executed. As an administrator run:

```
C:\>Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force -Verbose
```

```bash
# clone poc-base
C:\> git clone git@github.com:podder-ai/poc-base.git
C:\> cd poc-base
# configure environment variables if require
C:\> cp .env.sample .env
# enable python3
C:\>python3 -m venv C:\path\to\myenv
# Windows cmd.exe
C:\> C:\path\to\myenv\Scripts\activate.bat
# PowerShell PS
C:\> C:\path\to\myenv\Scripts\Activate.ps1
# install required libraries
C:\> pip install -r requirements.txt
# run sample code
C:\> python main.py
```

### Via Docker

To skip python environment setting, we are using Docker to run task. 
For detail Dockerfile check [here](./Dockerfile)


```bash
# build docker image with python enviroment
$ docker build -t poc-sample .

# run code
$ docker run -ti poc-sample python main.py
```

## Implementation note

Finally, your task implementation will be integrated to Pipeline-framework and deploy using Docker/Kubernetes.
To make it easier, please follow this implementation rules below.

- Only add your code to `app/task.py`
- Put your data set or model files to `data`
- Your task implementation will be compiled by Cython in integrating. Please don't use `__file__` in your code.
- Create virtual environment for your code. Please check [Creation of virtual environments](https://docs.python.org/3/library/venv.html)

Please add issue & pull request if you have any request!


