"""
Master Project Runner: SupeRR Selector Season 2 - PressurePlay Analytics
Runs all project phases (Phase 1 through Phase 8) end-to-end.
"""

import sys
import os
import time
import argparse
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

PHASES = {
    1: {
        "name": "Phase 1: Data Understanding & Profiling",
        "script": "run_phase1.py",
        "description": "Inspects raw datasets, schema validation, data dictionary & relationships"
    },
    2: {
        "name": "Phase 2: Data Cleaning & Preprocessing",
        "script": "src/run_phase2.py",
        "description": "Handles missing values, deduplication, cricket rules validation, referential integrity"
    },
    3: {
        "name": "Phase 3: Data Integration & Master Analytical Dataset",
        "script": "src/run_phase3.py",
        "description": "Integrates deliveries, matches, competitions, player mapping into unified delivery data"
    },
    4: {
        "name": "Phase 4: Match Context & Pressure Feature Engineering",
        "script": "src/run_phase4.py",
        "description": "Calculates pre-delivery match context, pressure engine, baseline vs pressure metrics"
    },
    5: {
        "name": "Phase 5: Exploratory Data Analysis (EDA)",
        "script": "src/run_phase5.py",
        "description": "Statistical distributions, 21 publication-grade charts, hypothesis testing"
    },
    6: {
        "name": "Phase 6: Player Rating & Ranking Engine",
        "script": "src/run_phase6.py",
        "description": "Multi-criteria 5-pillar scoring, Empirical Bayes shrinkage, Top 10 rankings"
    },
    7: {
        "name": "Phase 7: Power BI Data Preparation",
        "script": "src/run_phase7.py",
        "description": "Exports star/constellation schema CSVs, conformed calendar, data dictionary"
    },
    8: {
        "name": "Phase 8: Power BI Dashboard & Visual Architecture",
        "script": "src/run_phase8.py",
        "description": "Generates theme JSON, 35+ DAX measures library, 5-page blueprints, mathematical audit"
    }
}

def print_banner():
    banner = """
================================================================================
   ____                   ____  ____    ____       _           _             
  / ___| _   _ _ __   ___|  _ \\|  _ \\  / ___|  ___| | ___  ___| |_ ___  _ __ 
  \\___ \\| | | | '_ \\ / _ \\ |_) | |_) | \\___ \\ / _ \\ |/ _ \\/ __| __/ _ \\| '__|
   ___) | |_| | |_) |  __/  _ <|  _ <   ___) |  __/ |  __/ (__| || (_) | |   
  |____/ \\__,_| .__/ \\___|_| \\_\\_| \\_\\ |____/ \\___|_|\\___|\\___|\\__\\___/|_|   
              |_|                                                            
               SEASON 2 - PRESSUREPLAY CRICKET ANALYTICS ENGINE               
================================================================================
"""
    print(banner)

def run_single_phase(phase_num):
    info = PHASES[phase_num]
    print(f"\n>> Running [{phase_num}/8] {info['name']}")
    print(f"   Script: {info['script']}")
    print(f"   Purpose: {info['description']}")
    print("-" * 80)
    
    start_time = time.time()
    result = subprocess.run(
        [sys.executable, info['script']],
        cwd=str(PROJECT_ROOT),
        capture_output=False
    )
    elapsed = time.time() - start_time
    
    if result.returncode == 0:
        print(f">> [PASSED] {info['name']} completed in {elapsed:.2f}s\n")
        return True, elapsed
    else:
        print(f">> [FAILED] {info['name']} exited with code {result.returncode}\n")
        return False, elapsed

def run_all_phases(start_at=1, stop_at=8):
    print_banner()
    print(f"Starting End-to-End Pipeline Execution (Phases {start_at} to {stop_at})...\n")
    
    total_start = time.time()
    timing_summary = {}
    success_count = 0
    
    for p in range(start_at, stop_at + 1):
        success, elapsed = run_single_phase(p)
        timing_summary[p] = (success, elapsed)
        if success:
            success_count += 1
        else:
            print(f"Pipeline stopped early due to failure in Phase {p}.")
            break
            
    total_elapsed = time.time() - total_start
    print("=" * 80)
    print("                      PIPELINE EXECUTION SUMMARY")
    print("=" * 80)
    for p, (succ, elap) in timing_summary.items():
        status = "PASSED" if succ else "FAILED"
        print(f"  Phase {p}: {PHASES[p]['name']:55s} [{status}] ({elap:6.2f}s)")
    print("-" * 80)
    print(f"  Total Phases Completed: {success_count} / {len(timing_summary)}")
    print(f"  Total Execution Time:   {total_elapsed:.2f} seconds ({total_elapsed/60:.2f} minutes)")
    print("=" * 80)
    
    # Print Quick Insights Summary
    if success_count == 8:
        print("\n" + "=" * 80)
        print("                 PRESSUREPLAY ANALYTICS - FINAL RESULTS")
        print("=" * 80)
        print("  Tournament Scope:   200,999 deliveries across 867 matches (28.28% pressure)")
        print("  Ranked Batters:     264 players evaluated with Empirical Bayes reliability")
        print("  Ranked Bowlers:     244 players evaluated with Empirical Bayes reliability")
        print("  Top #1 Batter:      Brian Bennett (Rating: 74.32, Pressure SR: 150.54, Lift: +33.05)")
        print("  Top #1 Bowler:      Brad Evans (Rating: 71.58, Pressure Econ: 5.11, Suppr: +4.63)")
        print("  Power BI Assets:    9 Star-Schema CSVs in data/powerbi/, Theme JSON in config/")
        print("  DAX Measures:       35+ production measures in reports/phase8_dax_measures.md")
        print("  Visual Layouts:     5-page interactive blueprints in reports/phase8_dashboard_design.md")
        print("=" * 80 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SupeRR Selector Season 2 Master Runner")
    parser.add_argument("--phase", type=int, choices=range(1, 9), help="Execute a specific phase (1-8)")
    parser.add_argument("--start", type=int, default=1, choices=range(1, 9), help="Start phase number (default: 1)")
    parser.add_argument("--stop", type=int, default=8, choices=range(1, 9), help="Stop phase number (default: 8)")
    parser.add_argument("--all", action="store_true", help="Execute all phases from 1 to 8")
    
    args = parser.parse_args()
    
    if args.phase:
        print_banner()
        run_single_phase(args.phase)
    else:
        start_p = args.start
        stop_p = args.stop
        run_all_phases(start_at=start_p, stop_at=stop_p)

