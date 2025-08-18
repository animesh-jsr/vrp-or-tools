import argparse
import json
from pathlib import Path
import pandas as pd

from data import generate_locations, build_distance_matrix
from naive_baseline import naive_sequential_routes, total_distance
from vrp_solver import solve_vrp
from visualize import plot_routes

def routes_to_csv(routes, out_prefix, points):
    for vid, route in enumerate(routes):
        rows = []
        for i, node in enumerate(route):
            rows.append({
                "vehicle_id": vid,
                "step": i,
                "node": node,
                "x": points[node][0],
                "y": points[node][1],
            })
        df = pd.DataFrame(rows)
        df.to_csv(f"{out_prefix}_vehicle{vid}.csv", index=False)

def main():
    parser = argparse.ArgumentParser(description="Vehicle Routing & Scheduling with OR-Tools")
    parser.add_argument("--num_locations", type=int, default=20, help="Total locations including depot (>=2)")
    parser.add_argument("--num_vehicles", type=int, default=3, help="Number of vehicles")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--outputs_dir", type=str, default=str(Path(__file__).resolve().parents[1] / "outputs"))
    args = parser.parse_args()

    outputs_dir = Path(args.outputs_dir)
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # 1) Generate data & matrix
    locs = generate_locations(num_locations=args.num_locations, seed=args.seed)
    dist_matrix, points = build_distance_matrix(locs)

    # 2) Naive baseline
    naive_routes = naive_sequential_routes(len(points), args.num_vehicles)
    naive_total = total_distance(naive_routes, dist_matrix)

    # 3) OR-Tools optimization
    opt_routes, opt_total = solve_vrp(dist_matrix, args.num_vehicles, depot=0)

    # 4) Save CSVs
    routes_to_csv(naive_routes, str(outputs_dir / "routes_naive"), points)
    routes_to_csv(opt_routes, str(outputs_dir / "routes_optimized"), points)

    # 5) Plots
    plot_routes(points, naive_routes, str(outputs_dir / "naive_routes.png"), "Naive Routes (Sequential Split)")
    plot_routes(points, opt_routes, str(outputs_dir / "optimized_routes.png"), "Optimized Routes (OR-Tools)")

    # 6) Summary JSON
    improvement = None
    if naive_total > 0 and opt_total >= 0:
        improvement = round(100.0 * (naive_total - opt_total) / naive_total, 2)
    summary = {
        "num_locations": args.num_locations,
        "num_vehicles": args.num_vehicles,
        "seed": args.seed,
        "naive_total_distance": naive_total,
        "optimized_total_distance": opt_total,
        "percent_improvement_vs_naive": improvement,
        "notes": "Distances are in scaled units (Euclidean * 100)."
    }
    with open(outputs_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))
    print(f"Saved plots and routes CSVs to: {outputs_dir}")

if __name__ == "__main__":
    main()
