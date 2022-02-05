import yaml
import json

with open('.\yaml-json\input.yaml') as yaml_in:
    with open ('.\yaml-json\output.json', 'w') as json_out:
        json.dump(yaml.load(yaml_in, Loader=yaml.FullLoader),json_out,indent=2)