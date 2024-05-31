import heapq

class TSPSolverUCS:
    def __init__(self, distances):
        self.distances = distances
        self.n = len(distances)

    def solve(self, start=0):
        pq = [(0, [start])]
        best_cost = float('inf')
        best_route = None

        while pq:
            current_cost, current_route = heapq.heappop(pq)
            if len(current_route) == self.n:
                total_cost = current_cost + self.distances[current_route[-1]][start]
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_route = current_route + [start]
                continue

            for next_city in range(self.n):
                if next_city not in current_route:
                    new_route = current_route + [next_city]
                    new_cost = current_cost + self.distances[current_route[-1]][next_city]
                    heapq.heappush(pq, (new_cost, new_route))

        return best_route, best_cost

# Example usage
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

solver = TSPSolverUCS(distances)
route, cost = solver.solve()
print(f"Best route: {route}, Cost: {cost}")