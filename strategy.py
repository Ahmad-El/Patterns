from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    (Поведенческие)
    тратегия — это поведенческий паттерн проектирования, 
    который определяет семейство схожих алгоритмов и помещает каждый из них в собственный класс, 
    после чего алгоритмы можно взаимозаменять прямо во время исполнения программы.
    """
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()