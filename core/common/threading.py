from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from typing import Any

class Threading(Thread):
    
    def __init__(self, func):
        self.func = func

    def run(self):
        self.func()