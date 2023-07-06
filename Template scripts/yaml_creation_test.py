import pandas as pd
import yaml

# Load the CSV data into a DataFrame
df = pd.read_csv('./docs/csv/bdv-example.csv')

# Convert the DataFrame to a dictionary
data_dict = df.to_dict()

# Convert the dictionary to a YAML string
yaml_data = yaml.dump(data_dict)

# Write the YAML string to a file
with open('output.yaml', 'w') as f:
    f.write(yaml_data)