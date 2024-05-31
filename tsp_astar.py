import heapq

class TSPSolverAStar:
    def __init__(self, distances):
        self.distances = distances
        self.n = len(distances)

    def heuristic(self, route):
        unvisited = set(range(self.n)) - set(route)
        h = 0
        if unvisited:
            current_node = route[-1]
            h = min(self.distances[current_node][u] for u in unvisited)
        return h

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
                    new_cost = current_cost + self.distances[current_route[-1]][next_city] + self.heuristic(new_route)
                    heapq.heappush(pq, (new_cost, new_route))

        return best_route, best_cost

# Example usage
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

solver = TSPSolverAStar(distances)
route, cost = solver.solve()
print(f"Best route: {route}, Cost: {cost}")