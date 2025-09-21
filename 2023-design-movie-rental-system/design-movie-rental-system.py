from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self._unrented = {}
        self._rented = SortedList()
        self._prices = {}
        
        for shop, movie, price in entries:
            if movie not in self._unrented:
                self._unrented[movie] = SortedList()
            self._unrented[movie].add((price, shop))
            self._prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self._unrented:
            return []
        
        shops = []
        for i in range(min(5, len(self._unrented[movie]))):
            shops.append(self._unrented[movie][i][1])
        return shops

    def rent(self, shop: int, movie: int) -> None:
        price = self._prices[(shop, movie)]
        
        # Remove from unrented
        self._unrented[movie].remove((price, shop))
        
        # Add to rented
        self._rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self._prices[(shop, movie)]
        
        # Remove from rented
        self._rented.remove((price, shop, movie))
        
        # Add back to unrented
        if movie not in self._unrented:
             self._unrented[movie] = SortedList()
        self._unrented[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        report_list = []
        for i in range(min(5, len(self._rented))):
            price, shop, movie = self._rented[i]
            report_list.append([shop, movie])
        return report_list