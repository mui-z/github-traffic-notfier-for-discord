# Github Traffic Notifier for Discord

Github traffic views and clones count notifier for discord.

## About

Github Traffic Notifier used by discord webhook.  
This software notifies views and clones in your public repositories.

```
repo: foo
views: 290
clones: 109

repo: bar
views: 200
clones: 187


total views: 490
total clones: 296
```

## Usage

### 1. Create `.env`

create `.env` at project root dir.
```.env
GITHUB_TOKEN="YOUR GITHUB TOKEN"
DISCORD_WEBHOOK_URL="YOUR DISCORD WEBHOOK URL"
USER_NAME="YOUR GITHUB USERNAME"
```

`GITHUB_TOKEN` requires only `repo: public_repo` scope.

### 2. Setup Project

```bash
# create venv
python3 -m venv env

# activate venv
source env/bin/activate

# install requirements library
pip3 install -r requirements.txt
```

### 3. Run Script

```bash
python3 main.py
```

## LICENSE
This Application is licensed under the Apache-2.0  [License](LICENSE)
