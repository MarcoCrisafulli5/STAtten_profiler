import pandas as pd

with open('txts_scritps/capCifar100Times_SparsSpuriFix.txt', 'r') as file:
    lines = file.readlines()


SSA_times = [[] for _ in range(8)] # Create 8 lists to store HLF_time for each execution
MLP_times = [[] for _ in range(8)] # Create 8 lists to store HLF_time for each execution
SPS_Times = [[[], []] for _ in range(1)] # Create 8 lists to store SPS_time for each execution
current_execution_index = 0

for line in lines:
    line = line.strip()
    global_execution_index = 0 
    if ':' in line:
        if line.startswith("[Time] - SSA Encoder") or line.startswith("[Time] - MLP") or line.startswith("[Time] - SPS"):
            # If the line indicates a new execution, reset the current index
        
        # Extract metric and value
            metric, value = line.split(':')
            metric = metric.strip()
            value = value.strip()

        # Convert nanoseconds to seconds if necessary
            if 'nanoseconds' in value:
                value = float(value.replace('nanoseconds', '').strip()) / 1e9
            elif 'seconds' in value:
                value = float(value.replace('seconds', '').strip())
            else:
                continue  

        
            if metric == '[Time] - SPS.PSM':
                SPS_Times[global_execution_index][1].append(value)
            if metric == '[Time] - SPS.RPE':  
                SPS_Times[global_execution_index][0].append(value)
                global_execution_index += 1
            if metric == '[Time] - SSA Encoder':
                SSA_times[current_execution_index].append(value)
            if metric == '[Time] - MLP':
                MLP_times[current_execution_index].append(value)
                current_execution_index = (current_execution_index + 1) % 8 


# Calculate the mean for each of the 8 executions
SSA_means = [round(sum(times) / len(times), 9) if times else 0 for times in SSA_times]
MLP_means = [round(sum(times) / len(times), 9) if times else 0 for times in MLP_times]

#means for SPS times 30 executions
SPS_means = [round(sum(times[0]) / len(times[0]), 9) if times[0] else 0 for times in SPS_Times]
SPS_meansRPE = [round(sum(times[1]) / len(times[1]), 9) if times[1] else 0 for times in SPS_Times]


# Save the results to a CSV file
df = pd.DataFrame({'Execution': [f'Execution {i+1}' for i in range(8)], 'SSA_MEAN': SSA_means, 'MLP_MEAN': MLP_means})
df.to_csv('./csv/EncoderMeansExecSpuriFix.csv', index=False)

print("HLF mean times for each execution have been successfully saved to EncoderMeansExec.csv")