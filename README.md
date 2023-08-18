# Audio-visualiser
Ford Jones, Aug 18 2023

## Getting started
Make sure you have a python3 release installed with:
```
python3 --version
```

If you don't, please find a guide in the resources section at the bottom of this file.

## Setup your python virtual environment

1. From your working directory, make a new folder and navigate into it:
```
mkdir pyEnv && cd pyEnv
```

2. From here you can install the venv package to manage the projects virtual environment, with python installed you should be able to run this from your CLI:
```
python3 -m venv env
```
Now when listing the current directory you will notice a new folder has been created called env.

3. The environment needs to be activated. Do this by setting the source of the env like so:
```
source env/bin/activate
```

4. To check if that worked, you can list the python files using pip:
```
pip list
```

5. Note that the environment can be deactivated again easily by running this from the root:
```
deactivate
```
## Install dependencies:
install the dependencies using pip:
```
pip install -r requirements.txt
```

## Run the project:
```
python3 main.py
```

## Gotchas:
This project uses `Tkinter` to launch a native window which, from what I've read should be installed by default when setting up python at this location `../env/lib/python3.10/site-packages`.

For me it wasn't, find the download link in the resources section below.

## Resources: 
1. https://docs.python.org/3.11/using/index.html
2. Tkinter documentation: https://tkdocs.com/
3. Tkinter installation: https://tkdocs.com/tutorial/install.html 
4. pyAudio documentation: https://people.csail.mit.edu/hubert/pyaudio/docs/
