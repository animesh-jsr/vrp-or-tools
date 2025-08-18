from typing import List, Tuple
import matplotlib.pyplot as plt

def plot_routes(points: List[Tuple[float, float]], routes: List[List[int]], outfile: str, title: str):
    plt.figure()
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    # plot customers
    plt.scatter(xs[1:], ys[1:], label='Customers')
    # plot depot
    plt.scatter(xs[0], ys[0], marker='s', s=100, label='Depot')
    # draw routes
    for r in routes:
        rx = [points[i][0] for i in r]
        ry = [points[i][1] for i in r]
        plt.plot(rx, ry, marker='o')
    plt.title(title)
    plt.legend()
    plt.savefig(outfile, bbox_inches='tight')
    plt.close()
