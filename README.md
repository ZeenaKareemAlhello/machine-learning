1. python -m ipykernel install --user --name=ml_env --display-name "Python (ml_env)"
1. Select the Python Interpreter from the Command Palette
   
2. Create and Activate a Virtual Environment from terminal
   pipenv install
   # runs the commands in the env (option 1)
   pipenv shell 
   # create .env folder in the project dir
   PIPENV_VENV_IN_PROJECT=1 pipenv install
   # to run comands with the env (option2)
   pipenv run 

pipenv install notebook jupyter jupyterlab
pipenv install numpy pandas scikit-learn seaborn jupyter
pipenv install black "black[jupyter]"

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
 