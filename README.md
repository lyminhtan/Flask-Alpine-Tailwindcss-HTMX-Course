# Template
https://www.youtube.com/watch?v=jYhAxyDYFLI

## Install
```bash
touch environment.yml
conda env create
conda export -f environment.yml
conda env update

npm install -g browser-sync
```

## Run
```bash
flask run  # prefer for dev
python manage.py runserver  # for deployment
browser-sync 'http://localhost:8000' --watch --files .  # BUG

```