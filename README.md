# Beijing Housing Predict System
The predict model is based on [Decision trees](https://en.wikipedia.org/wiki/Decision_tree) of Machine Learning Framework [scikit-learn](http://scikit-learn.org/) and the system backend is powered by [Django](https://www.djangoproject.com/). 

It adopts [grid search algorithm](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search) to optimization learning model and uses [coefficient of determination](http://stattrek.com/statistics/dictionary.aspx?definition=coefficient_of_determination) as training metrics.

## Install

Clone Repo

```
git clone https://github.com/pwfee/Housing.git
cd Housing
```

Install Python Requirements

```pip install -r requirements.txt```

## Run

```
python manage.py runserver
```
Then Visit http://127.0.0.1:8000/

## Screenshots

![](http://cdn.pwfee.com/ext/housing.png)





