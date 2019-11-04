# About Me

This is the source code for my personal website.

## Environment

* macOS 10.13.6
* Homebrew 2.1.15
* Heroku CLI 7.33.3
* Python 3.7.5, pip 19.2.3
* [requirements.txt](./requirements.txt)

## Setup

1. [Install Python 3 and activate a virtual environment](https://github.com/ginomempin/how-to#python)
1. Install the [project dependencies](./requirements.txt):
    ```bash
    $ pip install -r requirements.txt

    ```

## Run

* Run **run.sh** then access the app at <http://localhost:5000/>

## Deploy (Heroku)

1. Prepare the Heroku remote
    * If the heroku app already exists: ```git remote add heroku <git-URL-of-app>```
    * If creating the app for the first time: ```heroku create <app-name>```
1. Verify that the heroku remote was created:
    * ```git remote -v```
1. Push production code to Heroku: ```git push heroku master```
1. Access the page using its <https://app-name.herokuapp.com> URL

## References

1. <https://devcenter.heroku.com/articles/deploying-python>
1. <https://github.com/datademofun/heroku-basic-flask>
