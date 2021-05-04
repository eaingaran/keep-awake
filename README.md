# keep-awake

## An Utility for efficient multitaskers to prevent computer from going to sleep or any application like skype/teams to conclude you are "Away".

### Supported Platorms
- Windows
- Mac OS
- Linux

### Instructions

- Setup python (Preferably 3.x)
- Clone this repository
- **Optional** Setup virtual environment (I strongly recommend it) *If you are using virtual environment, make sure you activate it before installing the requirement.*
- Install requirements - `pip install -r requirements.txt` *If you are in a computer that uses proxy, you can add optional parameter `--proxy=username:"password"@proxy_url:proxy_port` to pip*
- **Optional** Change default values for Awake Duration and/or Operation Interval in main.py *Default values are to duration=3600 (seconds) and interval=60 (seconds)*
- run `main.py -d=5200 -i=30` or `main.py --duration=5200 --interval=30` *This runs the program for about 2 hours with an ALT-TAB operation every 30 seconds.*
- **Additional Info** If duration and/or interval is not passed during invoking, it uses the default value set in main.py
- For help, you can use `main.py -h` or `main.py --help`
