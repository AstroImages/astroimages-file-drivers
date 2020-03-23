AstroImages Generic File Handling routines (astroimages-file-drivers)
=================================
![Version](https://img.shields.io/badge/version-0.1.1-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)
![Build Test](https://github.com/AstroImages/astroimages-file-drivers/workflows/Build%20Test%20(astroimages-file-drivers)/badge.svg)

Generic file handling routines and wrappers


Usage
-----

Clone the repo:

```console
$ git clone https://github.com/AstroImages/astroimages-file-drivers/
$ cd astroimages-file-drivers
```

Create virtualenv:

```console
$ virtualenv -p python3 env
$ source env/bin/activate
(env) $ pip3 install -r requirements.txt
```

## Testing

To run unit tests:

```console
(env) $ python -m unittest discover test/unit -v
```

## Packaging

To package
    
```console
(env) $ python setup.py sdist
```

To upload

```console
(env) $ pip3 install twine
(env) $ twine upload dist/*
```

## References


License
-------

MIT, see LICENSE file


