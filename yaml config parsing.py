import confuse # Initialize config with your app
# https://confuse.readthedocs.io/en/latest/
# pip install confuse

config = confuse.Configuration('MyApp', __name__) # Get a value from your YAML file
config['AWS']['Lambda']['Runtime'].get()

# validation of yaml data...
# ...

# init config from cli
config = confuse.Configuration('myapp')# Add arguments to be passed via a CLI
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='a parameter')
args = parser.parse_args()
config.set_args(args)
print(config['foo'].get())


# or
mysql:
    host: localhost
    user: root
    passwd: my secret password
    db: write-math
other:
    preprocessing_queue:
        - preprocessing.scale_and_center
        - preprocessing.dot_reduction
        - preprocessing.connect_lines
    use_anonymous: yes

import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
print(cfg["mysql"])
print(cfg["other"])
