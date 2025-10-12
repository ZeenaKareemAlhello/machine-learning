1. Select the Python Interpreter from the Command Palette
   /opt/homebrew/bin/python3 (or /usr/local/bin/python3)

2. Create and Activate a Virtual Environment from terminal
   python3 -m venv venv
   source venv/bin/activate
   deactivate

pip install notebook jupyter jupyterlab
pip install numpy pandas scikit-learn seaborn jupyter
pip install black "black[jupyter]"

command to reformat the jupyter notebook:
 black --ipynb  src/test.ipynb