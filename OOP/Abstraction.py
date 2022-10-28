# Program to understand Abstraction

from abc import ABC, abstractmethod


class cook(ABC):
    @abstractmethod
    def recipe(self):
        pass


class prepare(cook):
    def recipe(self):
        print("We will prepare food.")


meal = prepare()

meal.recipe()
