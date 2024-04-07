# class MyClass:
#     def __init__(self, value) -> None:
#         self._value = value
        
#     @property
#     def value(self):
#         return self._value
    
#     @value.setter
#     def value(self, new_value):
#         self._value = new_value


class MyClass:
    def __init__(self, value) -> None:
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        self._value = new_value
    
    value = property(get_value, set_value)

if __name__ == "__main__":
    x = MyClass(100)
    print(x.value)
    x.value = 90
    print(x.value)
    x.value = 91
    print(x.value)
        
        
