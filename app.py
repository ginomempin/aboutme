"""App Instance."""
# fmt: off

from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
Scss(app)

profiles = [
    {
        "name" : "Instagram",
        "link" : "https://www.instagram.com/ginomempin/",
        "icon" : "fab fa-instagram fa-2x",
    },
    {
        "name" : "Flickr",
        "link" : "https://www.flickr.com/people/ginomempin/",
        "icon" : "fab fa-flickr fa-2x",
    },
    {
        "name" : "GitHub",
        "link" : "https://github.com/ginomempin",
        "icon" : "fab fa-github fa-2x",
    },
    {
        "name" : "StackOverflow",
        "link" : "https://stackoverflow.com/users/2745495/gino-mempin?tab=profile",
        "icon" : "fab fa-stack-overflow fa-2x",
    },
    {
        "name" : "LinkedIn",
        "link" : "https://www.linkedin.com/in/ginomempin/",
        "icon" : "fab fa-linkedin fa-2x",
    },
    {
        "name" : "Goodreads",
        "link" : "https://www.goodreads.com/ginomempin",
        "icon" : "fab fa-goodreads fa-2x",
    },
]

albums = [
    {
        "title" : "Japan (2019)",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157677584052267",
        "img"   : {
            "name"  : "album-japan-2019.jpg",
            "src"   : "images/album-japan-2019.jpg"
        }
    },
    {
        "title" : "Morocco",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157711007699292",
        "img"   : {
            "name"  : "album-morocco.jpg",
            "src"   : "images/album-morocco.jpg"
        }
    },
    {
        "title" : "Japan (2018)",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157665104122898",
        "img"   : {
            "name"  : "album-japan-2018.jpg",
            "src"   : "images/album-japan-2018.jpg"
        }
    },
    {
        "title" : "Japan (2017)",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157681325385125",
        "img"   : {
            "name"  : "album-japan-2017.jpg",
            "src"   : "images/album-japan-2017.jpg"
        }
    },
    {
        "title" : "Hong Kong",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157676416833436/",
        "img"   : {
            "name"  : "album-hongkong.jpg",
            "src"   : "images/album-hongkong.jpg"
        }
    },
    {
        "title" : "Borobodur",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157671800357955/",
        "img"   : {
            "name"  : "album-borobodur.jpg",
            "src"   : "images/album-borobodur.jpg"
        }
    },
    {
        "title" : "Japan (2016)",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157663526941174/",
        "img"   : {
            "name"  : "album-japan-2016.jpg",
            "src"   : "images/album-japan-2016.jpg"
        }
    },
    {
        "title" : "Siem Reap",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157647928260390/",
        "img"   : {
            "name"  : "album-siemreap.jpg",
            "src"   : "images/album-siemreap.jpg"
        }
    },
    {
        "title" : "Seoul",
        "link"  : "https://www.flickr.com/photos/ginomempin/albums/72157638210694503/",
        "img"   : {
            "name"  : "album-seoul.jpg",
            "src"   : "images/album-seoul.jpg"
        }
    }
]

projects = [
    {
        "name" : "how-to",
        "link" : "https://github.com/ginomempin/how-to",
        "desc" : "A list of links to tutorials, templates, tools, and other helpful resources"
    },
    {
        "name" : "perfplotter",
        "link" : "https://github.com/ginomempin/perfplotter",
        "desc" : "A CLI tool for visualizing CSV/spreadsheet-like data"
    },
    {
        "name" : "python-tutorials",
        "link" : "https://github.com/ginomempin/python-tutorials",
        "desc" : "A collection of Python apps from various tutorials "
    },
    {
        "name" : "sample-ci-python",
        "link" : "https://github.com/ginomempin/sample-ci-python",
        "desc" : "Sample Python project that uses Gitlab CI, pytest, and pytest-cov"
    },
    {
        "name" : "sample-ci-cpp",
        "link" : "https://github.com/ginomempin/sample-ci-cpp",
        "desc" : "Sample C++ project that uses Gitlab CI, CMake, googletest, and lcov"
    },
    {
        "name" : "sample-dockerized-ros2-node",
        "link" : "https://github.com/ginomempin/sample-dockerized-ros2-node",
        "desc" : "Sample Dockerized ROS2 node and Python app"
    },
    {
        "name" : "coffeeshopph",
        "link" : "https://github.com/ginomempin/coffeeshopph-web",
        "desc" : "A Ruby on Rails web app for managing the operations of a cafe or a restaurant"
    }
]


@app.route('/')
def home():
    """Render the home page."""
    return render_template(
        'home.html',
        profiles=profiles,
        albums=albums,
        projects=projects)
