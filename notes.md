https://pypi.org/project/markdown-strings/
https://pypi.org/project/Markdown/

https://github.com/ReactTraining/react-router

https://www.codespeedy.com/convert-json-to-csv-in-python/

https://dev.mysql.com/doc/connector-python/en/

memarch create event "MoR 2020"
memarch create memory [-t TAGS] [[--date] or [--sdate --edate]] "standalone MEMORY" 
memarch add memory [eventName] [-t TAGS] [[--date] or [--sdate --edate]] "MEMORY associated with event" 



-----
sudo apt install mysql-server

-----
python requirements.txt vs setup.py
- PyPl libraries, that have metadata

requirements.txt:
- non-redistributable things
- may or not exist in pypl
- app needs
- deployment requirements

# This is an implicit value, here for clarity
--index-url https://pypi.python.org/simple/
This line turns abstract dependency of name-version into very specific name-version.
Says: Request something-1.2.0 from <url>/simple/.

- deps with exact version
- we want our app deploy with exact deps-versions with which our app has been tested
- can get by running "pip freeze > requirements.txt"


setup.py:
- redistributable things
- metadata: Name, Version, Deps, etc
- here specify these metadata
- abstract dependencies - just name and optional [version]
- just type deps, dont care about dep's deps.

- one can specify dependency links
setup(
    # ...
    dependency_links = [
        "http://packages.example.com/snapshots/",
        "http://example2.com/p/bar-1.0.tar.gz",
    ],
)
  

## Virtual envs
python3 -m venv fastapi-venv
source fastapi-env/bin/activate

pip install fastapi uvicorn aiofiles torch torch_snippets
pip freeze > requirements.txt


####### ini
Writing configuration ¶

import os

configfile_name = "config.ini"

# Check if there is already a configurtion file
if not os.path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    cfgfile = open(configfile_name, "w")

    # Add content to the file
    Config = ConfigParser.ConfigParser()
    Config.add_section("mysql")
    Config.set("mysql", "host", "localhost")
    Config.set("mysql", "user", "root")
    Config.set("mysql", "passwd", "my secret password")
    Config.set("mysql", "db", "write-math")
    Config.add_section("other")
    Config.set(
        "other",
        "preprocessing_queue",
        [
            "preprocessing.scale_and_center",
            "preprocessing.dot_reduction",
            "preprocessing.connect_lines",
        ],
    )
    Config.set("other", "use_anonymous", True)
    Config.write(cfgfile)
    cfgfile.close()
