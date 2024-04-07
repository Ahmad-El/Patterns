class SingletonMeta(type):
    """
    (Порождающие)
    Одиночка — это порождающий паттерн проектирования, 
    который гарантирует, что у класса есть только один экземпляр, 
    и предоставляет к нему глобальную точку доступа.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Any logic")



s1 = Singleton()
s2 = Singleton()

if id(s1) == id(s2):
    print(f"Singleton works, both variables contain the same instance:\n{id(s1)}\n{id(s2)}")
else:
    print(f"Singleton failed, variables contain different instances:\n{id(s1)}\n{id(s2)}")