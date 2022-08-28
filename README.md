# About Me

This is the source code for my personal website.

## Environment

* Python 3.9
* Flask 2.0.2
* [Heroku + Github Deploys](https://devcenter.heroku.com/articles/github-integration)

## Setup

1. [Install Python 3 and activate a virtual environment](https://github.com/ginomempin/how-to/blob/master/python/README.md)
1. Install the [project dependencies](./Pipfile):
    ```shell
    $ pipenv install --dev --python=$(which python3.9)

    ```

## Deploy (Local)

```shell
$ pipenv run local
```

Then access the app at <http://localhost:5000/>

## Deploy (Heroku)

1. Setup the [expected files for Python](https://devcenter.heroku.com/articles/deploying-python)
1. Setup [Github Integration](https://devcenter.heroku.com/articles/github-integration)
1. Push to the `master` branch
1. Access the page from its Heroku URL

## References

* Heroku
    1. [Deploying Python Apps](https://devcenter.heroku.com/articles/deploying-python)
    1. [Github Integration](https://devcenter.heroku.com/articles/github-integration)
* Examples/Tutorials
    1. [Deploying a simple Flask app to the cloud via Heroku](https://github.com/datademofun/heroku-basic-flask)
