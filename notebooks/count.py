import pandas as pd

# Load the CSV file
csv_path = "/Users/chan/Documents/UOC/ENGO685Wirless/WiFi_Analysis_Project/results/combined_wifi_data.csv"  # Update path if needed
df = pd.read_csv(csv_path)

# Dictionary to store unique MAC counts per location
location_mac_counts = {}

# Loop through each row to count unique MAC addresses per location
for index, row in df.iterrows():
    location = row["Location"]
    mac_address = row["MAC_Address"]
    
    # If location not in dictionary, initialize with an empty set
    if location not in location_mac_counts:
        location_mac_counts[location] = set()
    
    # Add MAC address to the set (sets automatically ensure uniqueness)
    location_mac_counts[location].add(mac_address)

# Convert the result to a DataFrame for display, adding +1 if there's at least one MAC
ap_counts_manual = pd.DataFrame(
    {
        "Location": list(location_mac_counts.keys()), 
        "Number_of_Access_Points": [
            len(mac_set) + 1 if len(mac_set) > 0 else 0  # Adjust count
            for mac_set in location_mac_counts.values()
        ]
    }
)

# Display the manually counted results
from IPython.display import display
display(ap_counts_manual)
