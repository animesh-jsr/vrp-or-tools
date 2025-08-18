import math
import random
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class LocationSet:
    depot: Tuple[float, float]
    customers: List[Tuple[float, float]]

def generate_locations(num_locations: int = 20, seed: int = 42) -> LocationSet:
    """Generate a depot at (0,0) and num_locations-1 customers in a square grid [-10, 10]."""
    assert num_locations >= 2, "Need at least 2 locations (1 depot + customers)."
    random.seed(seed)
    depot = (0.0, 0.0)
    customers = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(num_locations - 1)]
    return LocationSet(depot=depot, customers=customers)

def euclidean_distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def build_distance_matrix(locset: LocationSet) -> Tuple[list, list]:
    """Return integer distance matrix (scaled by 100) and list of points (depot first)."""
    points = [locset.depot] + locset.customers
    n = len(points)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                d = 0.0
            else:
                d = euclidean_distance(points[i], points[j])
            dist[i][j] = int(round(d * 100))  # scale to int for OR-Tools
    return dist, points
