==================================================
SYSTEM INFORMATION
==================================================
OS:         Windows 10
Version:    10.0.26200
Machine:    AMD64
Processor:  Intel64 Family 6 Model 158 Stepping 13, GenuineIntel
Python:     3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]

Benchmark 1 — sum(range(5,000,000))
  Result:  12,499,997,500,000
  Time:    0.1547 seconds

Benchmark 2 — list comprehension (n=1,000,000)
  First 5: [0, 1, 4, 9, 16]
  Time:    0.0551 seconds

Benchmark 3 — string join (n=100,000)
  Length:  588,889 characters
  Time:    0.0136 seconds

==================================================
SUMMARY
==================================================
  sum benchmark:    0.1547s
  list benchmark:   0.0551s
  string benchmark: 0.0136s

## RAM

Total RAM: 8 GB