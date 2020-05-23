from abc import ABC, abstractmethod

from logic.model import Recipe

class Store(ABC):
    @abstractmethod
    def add_recipe(self, recipe: Recipe) -> None:
        pass

    @abstractmethod
    def get_recipes(self) -> Recipe:
        pass

class InMemoryStore(Store):
    def __init__(self):
        self.store = []

    def add_recipe(self, recipe: Recipe) -> None:
        self.store += [recipe]
    
    def get_recipes(self) -> Recipe:
        return self.store
