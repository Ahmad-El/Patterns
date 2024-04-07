from typing import Any


class MyClass:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Welcome")
        return 1
    
    
obj = MyClass
