import json
import os
import matplotlib.pyplot as plt

results_dir = "benchmarks/results"

latencies = []
labels = []

for file in os.listdir(results_dir):
    if file.endswith(".json"):
        path = os.path.join(results_dir, file)
        with open(path) as f:
            data = json.load(f)
            latencies.append(data["average_latency"])
            labels.append(file.replace(".json", ""))

plt.figure()
plt.bar(labels, latencies)
plt.xticks(rotation=45)
plt.ylabel("Average Latency (sec)")
plt.title("Benchmark Latency Comparison")
plt.tight_layout()

plt.savefig("analysis/visualizations/latency_chart.png")
plt.show()
