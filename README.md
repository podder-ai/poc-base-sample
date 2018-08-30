# poc-base-sample

Sample task implementation for Podder.ai pipeline framework.
How to implement a task using poc-base repository.

## How to run sample code

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
