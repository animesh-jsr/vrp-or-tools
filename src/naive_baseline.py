from typing import List, Dict

def naive_sequential_routes(num_nodes: int, num_vehicles: int) -> List[List[int]]:
    """A simple baseline that splits customers sequentially among vehicles.
    Nodes are numbered 0..(n-1) with 0 as depot. Customers are 1..(n-1).
    Each route starts and ends at depot (0).
    """
    assert num_nodes >= 2
    customers = list(range(1, num_nodes))
    chunk_size = max(1, (len(customers) + num_vehicles - 1) // num_vehicles)
    routes = []
    for i in range(0, len(customers), chunk_size):
        chunk = customers[i:i+chunk_size]
        route = [0] + chunk + [0]
        routes.append(route)
    # If fewer chunks than vehicles, add empty depot-only routes
    while len(routes) < num_vehicles:
        routes.append([0, 0])
    return routes

def route_distance(route: List[int], distance_matrix: List[List[int]]) -> int:
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i+1]]
    return total

def total_distance(routes: List[List[int]], distance_matrix: List[List[int]]) -> int:
    return sum(route_distance(r, distance_matrix) for r in routes)
