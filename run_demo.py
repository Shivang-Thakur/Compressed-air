"""Bina HiveMQ ke 30-second demo: data banao -> CSV me save karo -> print karo.

Run: python run_demo.py
Iske baad: streamlit run layer1/dashboard.py  (charts dikhenge)
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "layer1"))
from save_csv import save_reading  # noqa: E402
from synthetic_data import generate_reading  # noqa: E402

prev = None
for i in range(15):
    reading = generate_reading(leak=(i % 5 == 4), prev_pressure=prev)
    prev = reading["pressure"]
    save_reading(reading)
    print(reading)
    time.sleep(0.2)
print("\nDone. Ab chalao: streamlit run layer1/dashboard.py")
