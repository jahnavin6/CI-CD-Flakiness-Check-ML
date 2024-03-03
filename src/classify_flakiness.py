# Import necessary libraries
import pandas as pd
import sys

def classify_flakiness(data_path):
    df = pd.read_csv(data_path)
    # Dummy heuristic for example: mark all tests as 'Not Evaluated'
    df['Flakiness'] = 'Not Evaluated'
    return df

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python classify_flakiness.py <path_to_csv_file>")
        sys.exit(1)
    
    data_path = sys.argv[1]
    results = classify_flakiness(data_path)
    print(results)

