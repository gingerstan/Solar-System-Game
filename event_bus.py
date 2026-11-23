from collections.abc import Callable
from collections import defaultdict
from typing import Any
from itertools import zip_longest

class Bus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event_name: str, fn: Callable[..., Any]) -> None:
        self.subscribers[event_name].append(fn)

    def unsubscribe(self, event_name, fn):
        self.subscribers[event_name].remove(fn)

    def call(self, event_name: str, args: list[list[Any]] = []) -> list[Any]:
        outputs = []
        for fn, params in zip_longest(self.subscribers[event_name], args):
            outputs.append(fn(*params) if params else fn())

        return outputs

    # takes a dict with function keys, containing the arguments to be
    # supplied to their corresponding function.
    def cooler_call(self, event_name: str, args_dict: dict[Callable[..., Any], list[Any]]):
        pass

    def print_call_order(self,event_name):
        print(self.subscribers[event_name])

bus = Bus()



# def sum(first, second):
#     print("yippee")
#     return first + second

# def thisone():
#     print("yay!")

# def anotherone(key=15):
#     print(key)

# b = Bus()
# b.subscribe("shit",thisone)
# b.subscribe("shit",sum)
# b.subscribe("shit",thisone)
# b.subscribe("shit",anotherone)
# b.subscribe("shit",thisone)

# b.call("shit",[None,[2,3],None])