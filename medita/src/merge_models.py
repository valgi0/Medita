import os

cli = "mergekit-yaml config.yaml merge --copy-tokenizer --allow-crimes --out-shard-size 1B"
# Now I run the command
os.system(cli)