import pandas as pd

# Read the text file
with open('txts_scritps/capCifar100Times_SparsSpuriFix.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables
attention_metrics = [
    "[Time] - SPS.PSM", "[Time] - SPS.RPE", "[Time] - Reshape",
    "[Time] - Matmul", "[Time] - Reshape Time-Space", "[Time] - Transpose and LIF",
    "[Time] - Projection and BN", "[Time] - SSA Encoder", "[Time] - MLP", "[Time] - Spikeformer Time time"
]
data = []
current_execution = {metric: [] for metric in attention_metrics}

for line in lines:
    line = line.strip()
    if ':' in line:
        # Extract metric and value
        if line.startswith("Run"):
            # Calculate the mean for the current execution
            if any(current_execution[metric] for metric in attention_metrics):
                mean_execution = {metric: round(sum(current_execution[metric]) / len(current_execution[metric]), 9)
                                  for metric in attention_metrics}
                data.append(mean_execution)
                current_execution = {metric: [] for metric in attention_metrics}
        else:
            metric, value = line.split(':')
            metric = metric.strip()
            value = value.strip()

            # Convert nanoseconds to seconds if necessary
            if 'nanoseconds' in value:
                value = float(value.replace('nanoseconds', '').strip()) / 1e9
            elif 'seconds' in value:
                value = float(value.replace('seconds', '').strip())
            else:
                continue  # Skip lines without valid time format

            # Add the metric value if it belongs to attention
            if metric in attention_metrics:
                current_execution[metric].append(value)

# Append the last execution if it exists
if any(current_execution[metric] for metric in attention_metrics):
    mean_execution = {metric: round(sum(current_execution[metric]) / len(current_execution[metric]), 9)
                      for metric in attention_metrics}
    data.append(mean_execution)

# Convert to a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('./csv/ModelTimesCifarSpuriFix.csv', index=False)

print("Attention module means have been successfully saved to ModelTimesCifar.csv")