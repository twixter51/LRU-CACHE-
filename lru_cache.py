from collections import OrderedDict
from typing import Any

class LRUCache:


    # previously was O(n) as I was looping through the dict, but now its much more faster with O(1) speed

    __slots__ = ("capacity", "cache")

    def __init__(self, capacity: int):
        if capacity < 0:
            return -1
        self.capacity = capacity
        self.cache: "OrderedDict[Any, Any]" = OrderedDict()

    def get(self, key: Any) -> Any:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  
        return self.cache[key]

    def put(self, key: Any, value: Any) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) >= self.capacity:
            
            self.cache.popitem(last=False)
        self.cache[key] = value
