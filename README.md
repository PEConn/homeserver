To set up:

```bash
git clone https://github.com/PEConn/homeserver.git
cd homeserver
sudo apt install python3-venv python3-pip
python3 -v venv python/env
source python/env/bin/activate
pip3 install python/requirements.txt
```

To run:

```bash
source python/env/bin/activate
python python/main.py
```