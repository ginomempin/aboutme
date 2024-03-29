# About Me

This is the source code for my personal website.

## Environment

* Python 3.10
* Flask 2.0.x
* [Heroku + Github Deploys](https://devcenter.heroku.com/articles/github-integration)

## Setup

1. [Install Python 3 and activate a virtual environment](https://github.com/ginomempin/how-to/blob/master/python/README.md)
1. Install the [project dependencies](./Pipfile):
    ```shell
    $ poetry install --dev --no-root
    ```

## Deploy (Local)

```shell
$ ./run.sh
```

Then access the app at <http://localhost:5000/>

## Deploy (Heroku)

1. Setup the [expected files for Python](https://devcenter.heroku.com/articles/deploying-python)
    * Generate `requirements.txt`
        ```
        $ poetry export --format=requirements.txt --without=dev --output=requirements.txt
        ```
1. Setup [Github Integration](https://devcenter.heroku.com/articles/github-integration)
1. Push to the `master` branch
1. Access the page from its Heroku URL

## References

* Heroku
    1. [Deploying Python Apps](https://devcenter.heroku.com/articles/deploying-python)
    1. [Github Integration](https://devcenter.heroku.com/articles/github-integration)
* Examples/Tutorials
    1. [Deploying a simple Flask app to the cloud via Heroku](https://github.com/datademofun/heroku-basic-flask)
