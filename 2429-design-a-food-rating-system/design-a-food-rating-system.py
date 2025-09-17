from typing import List
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food -> (cuisine, rating)
        self.food_info = {}
        # cuisine -> SortedList of (-rating, food)
        self.cuisine_map = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = (c, r)
            if c not in self.cuisine_map:
                self.cuisine_map[c] = SortedList()
            self.cuisine_map[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.food_info[food]
        # Remove old record
        self.cuisine_map[cuisine].remove((-oldRating, food))
        # Add new record
        self.cuisine_map[cuisine].add((-newRating, food))
        # Update food info
        self.food_info[food] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        # The smallest tuple in SortedList has the highest rating 
        # because we stored as (-rating, food)
        return self.cuisine_map[cuisine][0][1]

