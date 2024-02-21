read -p "enter access token: " token
echo "DISCORD_ACCESS_TOKEN='$token'" >> .env

python -m venv .venv || python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
deactivate

read -p "start bot? [y/n]: " start

if [[ $start == 'y' ]]; then
    source .venv/bin/activate
    python run.py || python3 run.py
else
    exit 0
fi
