import json
import yaml

# read json data from the file
with open('sample.json', 'r') as fd:
    json_data = fd.read()

# Parse JSON
parsed_data = json.loads(json_data)

# Convert to YAML
yaml_data = yaml.dump(parsed_data, default_flow_style=False)

# Write yaml data to the file
with open('output.yaml', 'w') as fd:
  fd.write(yaml_data)