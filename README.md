# Vehicle Routing & Scheduling (Google OR-Tools)

A ready-to-run Python project that demonstrates the **Vehicle Routing Problem (VRP)** using **Google OR-Tools**, with a simple **naive baseline** for comparison and clean **matplotlib visualizations**.

## ✨ What this project shows
- Generate a reproducible synthetic delivery scenario (depot + customer locations).
- Solve VRP with **multiple vehicles** using OR-Tools.
- Compare to a **naive baseline** (sequential split) and report **% improvement**.
- Save route **plots** and **CSV results** to the `outputs/` folder.

## 📦 Setup (VS Code friendly)

1. **Clone/Extract** this folder.
2. (Optional) Create a virtual environment
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run**
   ```bash
   python src/main.py --num_locations 20 --num_vehicles 3 --seed 42
   ```

> Results (routes, distances, plots) are saved in `outputs/`.

## 🧠 Key Files
- `src/main.py` — entry point; orchestrates data, baseline, solver, and plotting.
- `src/data.py` — generates synthetic coordinates and builds a distance matrix.
- `src/naive_baseline.py` — simple baseline routes (sequential split).
- `src/vrp_solver.py` — OR-Tools VRP solver (multiple vehicles).
- `src/visualize.py` — matplotlib plots for naive vs optimized routes.

## 📈 Example Output
- `outputs/optimized_routes.png` — plot of OR-Tools routes
- `outputs/naive_routes.png` — plot of baseline routes
- `outputs/summary.json` — distances & % improvement
- `outputs/routes_*.csv` — CSV of routes per vehicle

## 🔍 Notes
- Distances are computed as **Euclidean** between points and scaled to integers for OR-Tools.
- You can change number of locations/vehicles and the random seed via CLI flags.

## 🧩 Next Steps (to impress professors)
- Add **capacity constraints** (demands + vehicle capacity via OR-Tools dimensions).
- Add **time windows** (deliveries within given time ranges).
- Load **real coordinates** (lat/long) and map distances via OSRM/Google Maps API.
- Try **Pyomo/PuLP** to formulate VRP variants as MILP for comparison.
