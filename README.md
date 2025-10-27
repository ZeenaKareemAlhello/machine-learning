1. python -m ipykernel install --user --name=ml_env --display-name "Python(ml_env)"
1. Select the Python Interpreter from the Command Palette

python3 -m pip install --upgrade pip setuptools wheel --user
python3 -m pip install --user uv
2. Create and Activate a Virtual Environment from terminal
  
   uv venv .venv
   uv init
   uv
   to install the packages from uv.lock
   uv sync  

uv add notebook jupyter jupyterlab
uv add numpy pandas scikit-learn seaborn jupyter
uv add black "black[jupyter]"

command to reformat the jupyter notebook:
 black --ipynb  src/test.ipynb

pip install tqdm

# web service
pip install flask

# use flask in production (WSGI server)
pip install gunicorn
% gunicorn --bind 0.0.0.0:9696 src.service.churn:app

# Docker
docker build -t churn-test .
docker run -it --rm -p 9696:9696 churn-test

open bash in the image container:
docker run -it churn-test bash
 
# install nbstripout to let .git ignore the metadata of notebooks
uv add nbstripout
uv run nbstripout --install --attributes .gitattributes

# use Fastapi to build service app
uv add uvicorn
uv run uvicorn src.service.churn:app --host 0.0.0.0 --port 9696 --reload