# About Me

This is the source code for my personal website.

## Environment

* macOS 10.13.6
* Homebrew 2.1.15
* Python 3.7.5, pip 19.2.3
* [requirements.txt](./requirements.txt)

## Setup

1. [Install Python 3 and activate a virtual environment](https://github.com/ginomempin/how-to#python)
1. Install the [project dependencies](./requirements.txt):
    ```shell
    $ pip install -r requirements.txt

    ```

## Run

* Run **run.sh** then access the app at <http://localhost:5000/>

## Deploy (Heroku)

1. Setup [Github Integration](https://devcenter.heroku.com/articles/github-integration)
1. Push to the `master` branch
1. Access the page using its <https://app-name.herokuapp.com> URL

## References

1. <https://devcenter.heroku.com/articles/deploying-python>
1. <https://devcenter.heroku.com/articles/github-integration>
1. <https://github.com/datademofun/heroku-basic-flask>
