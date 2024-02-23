import os
import sys

dir = 'medita-model'
config_file = 'medita_merge.yaml'
if not os.path.exists(dir):
    os.makedirs(dir)
cli = f"mergekit-yaml {config_file} {dir} --copy-tokenizer --allow-crimes --out-shard-size 1B"
# Now I run the command
os.system(cli)