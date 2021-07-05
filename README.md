# bike_hire

## Description: 
To check out the bike hire analysis, please go into the jupyter notebook folder. It has five parts: 
1. time and seasonal analysis
2. spatial analysis
3. prediction
4. prediction -member 
5. prediction - nonmember

For question 2, prediction between SEPT 4 - SEPT10, please review the notebook prediction. 


For question 3, spliting the model for member/ non-member does seem to improve the model performance, 
which should also be observed in the first **time and seasonal analysis**. Member/Non-member, they do 
use the bike hire service at a different time in the week and different months as well, namely, 
non-member tend to hire bike more on the weekend, and in summer time in July and August

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
