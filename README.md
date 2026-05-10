# collaborative-server
AstraEditor collaborative editing local server

## How to use? 

1. Clone this repo:
```bash
git clone https://github.com/AstraEditor/collaborative-server.git
cd collaborative-server
```

2. Create and activate virtual environment:
``` bash
python -m venv .venv
```
- Linux or MacOS:
``` bash
source .venv/bin/activate
```
- Windows:
- - PowerShell:
``` bash 
.venv\Scripts\Activate.ps1
```
- - CMD:
``` bash
.venv\Scripts\activate.bat
```

3. Install dependencies:
``` bash
pip install -e .
```

### Development

Finish [How to use](#how-to-use) then run

``` bash
collab-server
```