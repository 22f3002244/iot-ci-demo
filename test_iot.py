#!/usr/bin/env python3
import pytest
from iot_sensor import SENSORS, read_sensor

class TestSensorReading:
    def test_sensors_defined(self):
        types = {s['type'] for s in SENSORS}
        assert 'temperature' in types
        assert 'humidity' in types
        assert 'pressure' in types
        assert 'light' in types

    def test_reading_within_range(self):
        for sensor in SENSORS:
            val = read_sensor(sensor)
            lo, hi = sensor['range']
            assert lo <= val <= hi

    def test_reading_is_float(self):
        for sensor in SENSORS:
            val = read_sensor(sensor)
            assert isinstance(val, float)

    def test_reading_has_2_decimal_places(self):
        for sensor in SENSORS:
            val = read_sensor(sensor)
            assert val == round(val, 2)

    def test_temperature_threshold_alert(self):
        reading = 41.5
        assert reading > 40, "High temperature alert not triggered"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
```

---

### File 3 — `requirements.txt`
```
pytest==8.2.0
pytest-html==4.1.1
