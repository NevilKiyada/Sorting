# List operations 
import random
import os
import time
import pandas as pd

def generate_starting_list(n, min_val, max_val):
    # ... existing code ...
    lst = []

    for _ in range(n):  
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def store_csv_file(lst , sorting_algo_name):
    # ... existing code ...

    relative_path = "sorted_list"
    sorted_list_dir = os.path.join(os.getcwd(), relative_path)
    os.makedirs(sorted_list_dir, exist_ok=True)
 
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"sorted_data_{sorting_algo_name}_{timestamp}.csv"
    file_path = os.path.join(sorted_list_dir, f"sorted_data_{sorting_algo_name}_{timestamp}.csv")

    sorted_list = lst
    df = pd.DataFrame(sorted_list) 
    df.to_csv( file_path , index=False) 
    print(f"Sorted list saved to: {filename}")
    print (sorted_list)