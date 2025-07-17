import pandas as pd
import numpy as np


def extract_chunks(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    chunks = []
    current_chunk = []
    chunk_count = 1
    
    for line in lines:
        if 'sparsity Attention postReshape chunk' in line:
            current_chunk.append(float(line.split(':')[1].strip()))
            if len(current_chunk) == 8:  # 4 output + 4 x lines
                # Create dictionary for each chunk
                chunk_dict = {
                    'Execution': chunk_count,
                    'output_0': current_chunk[0],
                    'output_1': current_chunk[1],
                    'output_2': current_chunk[2],
                    'output_3': current_chunk[3],
                    'x_0': current_chunk[4],
                    'x_1': current_chunk[5],
                    'x_2': current_chunk[6],
                    'x_3': current_chunk[7]
                }
                chunks.append(chunk_dict)
                current_chunk = []
                chunk_count += 1
    
    # Create DataFrame from chunks
    df = pd.DataFrame(chunks)
    
    # Round all numeric columns to 4 decimal places
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].round(4)
    
    # Save to CSV
    df.to_csv('csv/chunksRANDN.csv', index=False)
    return df

def calculate_average_sparsities_per_encoder(filename):
    # Initialize lists for each encoder execution (8 executions)
    x_for_qkv = [[] for _ in range(8)]
    q_vals = [[] for _ in range(8)]
    k_vals = [[] for _ in range(8)]
    v_vals = [[] for _ in range(8)]
    attention_out = [[] for _ in range(8)]
    attention_LIFout = [[] for _ in range(8)]
    mlp_postlif = [[] for _ in range(8)]
    mlp_postfc2 = [[] for _ in range(8)]
    
    lines_per_block = 20  # Approximate number of lines per encoder block
    current_encoder = 0
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        total_blocks = len(lines) // lines_per_block
        blocks_per_encoder = total_blocks // 8  # Should be 10
        
        for i, line in enumerate(lines):
            # Calculate current encoder based on block number
            current_encoder = (i // (lines_per_block * blocks_per_encoder)) % 8
            
            if 'sparsity x_for_qkv:' in line:
                value = float(line.split(':')[1].strip())
                x_for_qkv[current_encoder].append(value)
            elif 'sparsity q:' in line and 'chunks' not in line:
                value = float(line.split(':')[1].strip())
                q_vals[current_encoder].append(value)
            elif 'sparsity k:' in line and 'chunks' not in line:
                value = float(line.split(':')[1].strip())
                k_vals[current_encoder].append(value)
            elif 'sparsity v:' in line and 'chunks' not in line:
                value = float(line.split(':')[1].strip())
                v_vals[current_encoder].append(value)
            elif 'sparsity Attention out:' in line:
                value = float(line.split(':')[1].strip())
                attention_out[current_encoder].append(value)
            elif 'sparsity Attention postReshape x:' in line:
                value = float(line.split(':')[1].strip())
                attention_LIFout[current_encoder].append(value)
            elif 'MLP sparsity postLIF x after lif:' in line:
                value = float(line.split(':')[1].strip())
                mlp_postlif[current_encoder].append(value)
            elif 'MLP sparsity postLIF x after fc2:' in line:
                value = float(line.split(':')[1].strip())
                mlp_postfc2[current_encoder].append(value)

    # Calculate averages for each encoder execution
    data = {
        'Encoder Execution': range(1, 9),
        'x_for_qkv': [np.mean(x) for x in x_for_qkv],
        'q': [np.mean(q) for q in q_vals],
        'k': [np.mean(k) for k in k_vals],
        'v': [np.mean(v) for v in v_vals],
        'Attention out': [np.mean(a) for a in attention_out],
        'Attention postLIF x': [np.mean(a) for a in attention_LIFout],  # Fixed this line
        'MLP postLIF': [np.mean(m) for m in mlp_postlif],
        'MLP postfc2': [np.mean(m) for m in mlp_postfc2]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Round all numeric columns to 4 decimal places
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].round(4)
    
    return df

# Call the function and display the DataFrame
# Call the function
df_chunks = extract_chunks('txts_scritps/capcifarTensRandn.txt')
