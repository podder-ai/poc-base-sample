from framework import Context

from typing import Any

DATA_PATH = "data/"


class BaseTask(object):
    """
    Abstract task class.
    Please add your concrete code to concrete task class: `app/task.py`.
    """

    def __init__(self, context: Context) -> None:
        self.context = context
        self.set_arguments()

    def execute(self) -> Any:
        pass

    def set_arguments(self) -> None:
        pass
