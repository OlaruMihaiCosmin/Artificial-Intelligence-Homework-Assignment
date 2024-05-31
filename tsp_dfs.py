class TSPSolverDFS:
    def __init__(self, distances):
        self.distances = distances
        self.n = len(distances)
        self.best_cost = float('inf')
        self.best_route = None

    def dfs(self, start, current_route, current_cost):
        if len(current_route) == self.n:
            total_cost = current_cost + self.distances[current_route[-1]][start]
            if total_cost < self.best_cost:
                self.best_cost = total_cost
                self.best_route = current_route + [start]
            return

        for next_city in range(self.n):
            if next_city not in current_route:
                self.dfs(start, current_route + [next_city], current_cost + self.distances[current_route[-1]][next_city])

    def solve(self, start=0):
        self.dfs(start, [start], 0)
        return self.best_route, self.best_cost

# Example usage
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

solver = TSPSolverDFS(distances)
route, cost = solver.solve()
print(f"Best route: {route}, Cost: {cost}")
