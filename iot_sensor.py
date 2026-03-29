#!/usr/bin/env python3
import random, time, json
from datetime import datetime

SENSORS = [
    {'id': 'TEMP_01', 'type': 'temperature', 'range': (18.0, 45.0), 'unit': 'C'},
    {'id': 'HUM_01',  'type': 'humidity',    'range': (30.0, 90.0), 'unit': '%'},
    {'id': 'PRES_01', 'type': 'pressure',    'range': (980.0, 1025.0), 'unit': 'hPa'},
    {'id': 'LUX_01',  'type': 'light',       'range': (0.0, 1200.0), 'unit': 'lux'},
]

def read_sensor(sensor):
    lo, hi = sensor['range']
    return round(random.uniform(lo, hi), 2)

def collect_data(n_cycles=5):
    all_readings = []
    for _ in range(n_cycles):
        batch = []
        for s in SENSORS:
            val = read_sensor(s)
            batch.append({**s, 'value': val,
                          'timestamp': datetime.now().isoformat()})
            print(f"  [{s['id']}] {s['type']}: {val} {s['unit']}")
        all_readings.extend(batch)
        time.sleep(1)
    return all_readings

if __name__ == '__main__':
    print("=== IoT Data Collector Started ===")
    data = collect_data()
    with open('sensor_output.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Collected {len(data)} readings. Saved to sensor_output.json")
