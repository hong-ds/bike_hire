# bike_hire

## Description: 
To check out the bike hire analysis, please go into the jupyter notebook folder. It has three parts: 
1. time and seasonal analysis
2. spatial analysis
3. prediction

If you would like to run the notebook or change settings, please set up your enviroment as follow. 

## Set up enviroment: 
There are three ways to set up your enviroment:
1. Run the jupyter notebook inside a docker container. 
```
  $ docker build -t bike-hire:1.0 .
  $ docker compose up
  # click the 8888 link to open jupyter notebook server
```
2. Use poetry to install the virtual env and all the dependencies
```
  # install poetry (https://python-poetry.org/docs/)
  $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  
  $ poetry install
  $ poetry shell
  $ jupyter notebook
```
3. use your own virtual env and install the requirement.txt 
