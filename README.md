# poc-base-sample

Sample task implementation for Podder.ai pipeline framework.
How to implement a task using poc-base repository.

## How to run sample code

### Create virtual environment

Create Python virtual environment. Please check [Creation of virtual environments](https://docs.python.org/3/library/venv.html)

### For Mac os, Linux user

```bash
# clone poc-base
$ git clone git@github.com:podder-ai/poc-base-sample.git
$ cd poc-base-sample
>>>>>>> :+1: update Readme file
# configure environment variables
$ cp .env.sample .env
# enable python3
$ python3 -m venv env
$ source env/bin/activate
# install required libraries
$ pip install -r requirements.txt
# run sample code
$ python main.py
```

### For Windows user

```bash
C:\>python -m venv C:\path\to\myenv
# Windows cmd.exe
C:\> C:\path\to\myenv\Scripts\activate.bat
# PowerShell PS
C:\> C:\path\to\myenv\Scripts\Activate.ps1
```

### Via Docker

For detail Dockerfile check [here](./Dockerfile)

```bash
# build docker image with python enviroment
$ docker build -t poc-sample .

# run code
$ docker run -ti poc-sample python main.py
```

## Source code directory

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
│   ├── base_task.py
│   ├── config.py
│   ├── context.py
│   ├── file.py
│   └── logger.py
├── main.py
├── requirements.txt # add required packages here
├── .env.sample # sample of environment variables 
├── .env # where to add your environment variables 
```

## How to implement the new task

Please check the implementation guideline here. [PoC base guideline](https://github.com/podder-ai/poc-base)
