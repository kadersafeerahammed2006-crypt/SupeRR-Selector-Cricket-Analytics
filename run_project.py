"""
Entry point shortcut to main.py
"""
import sys
from pathlib import Path

if __name__ == "__main__":
    from main import parser, run_single_phase, run_all_phases, print_banner
    args = parser.parse_args()
    if args.phase:
        print_banner()
        run_single_phase(args.phase)
    else:
        run_all_phases(start_at=args.start, stop_at=args.stop)

