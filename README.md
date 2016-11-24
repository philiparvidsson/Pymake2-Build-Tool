[![Travis](https://img.shields.io/travis/philiparvidsson/pymake.svg)]() [![LICENSE.md](https://img.shields.io/github/license/philiparvidsson/pymake.svg)]()


# What is pymake? <img align="right" src="assets/images/pymake-logo.png">

**Pymake** is a tool for automating build tasks. It comes with ready-made templates for several different kinds of projects, allowing you to quickly set up portable build tasks. **With pymake, it becomes trivial to set up complex build tasks, doing everything from library and executable compilation to asset building and even deployment.**

* [Download](https://github.com/philiparvidsson/pymake/releases/)
* [Manual](docs/manual.md)

## Getting Started

1. Download and install [Python 2.7](https://www.python.org/downloads/).
2. Start with one of the [example](examples) or [template](src/templates) scripts, picking one relevant to your type of project.
3. Modify the script as needed for your project. See [the manual](docs/manual.md) for instructions on how to do so.
3. Build your project by running your make script. You can either type `python your_make_file.py` or `./your_make_file.py` (only on Linux).

### Prerequisities

* [Python 2.7](https://wiki.python.org/moin/BeginnersGuide/Download)

### Installation

#### Begin by downloading and installing [Python 2.7](https://www.python.org/downloads/).
On Linux, depending on your distribution, Python comes pre-installed. This means that you do not need to install anything for pymake to work. If you don't have Python (you can check by typing python in a terminal), you might be able to install it by typing `sudo apt-get install python`.

On Windows, you need to install Python manually. See [this link](https://wiki.python.org/moin/BeginnersGuide/Download) for more information.

#### Download the latest pymake release.
The latest pymake scripts are always available [here](https://github.com/philiparvidsson/pymake/releases/). Download and save `pymake.py` along with any make script you need for your project.

### Usage

#### Begin by creating a simple make script.
To familiarize yourself with pymake, you can begin by writing a simple make script. You could also use one of the [example programs](examples), or the one below if you just want to try out pymake quickly. In case you use the script below, make sure to put `pymake.py` in the same directory.

```python
#!/usr/bin/env python
from pymake import *

@target
@depends_on('build', 'compile')
def all(conf):
    print 'done.'

@target
def build(conf):
    print 'building', conf.name + '...'

@target
def compile(conf):
    print 'compiling...'

pymake({ 'name': 'some_program.bin' })
```

Since pymake scripts are written in Python, there is really no limit to what can be done. This allows you to easily create very complex and secure build and deployment scripts for your projects.

#### Build your project.
Save your script in a file named `make.py` in your project directory. Make sure you have installed pymake into the `build/pymake` directory (this is the standard directory, but can always be changed if needed). Invoke your make script by running it with the following command: `python make.py`

Make sure you are in your project directory, where your `make.py` file is.

## Running the Tests

n/a

## Deployment

### Deploying make scripts

Along with your `make.py` file, you need to store the `pymake.py` file in your project. You also need to store any template files that your make script depends on (for example, `csc.py`) in your project.

## Built With

* **Emacs** - Emacs is, along with vi, one of the two main contenders in the traditional editor wars of Unix culture. Both are among the oldest application programs still in use.
* **Python** - A widely used high-level, general-purpose, interpreted, dynamic programming language.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/philiparvidsson/pymake/tags).

## Authors

* **Philip Arvidsson** - *Initial work* - [philiparvidsson](https://github.com/philiparvidsson)

See also the list of [contributors](https://github.com/philiparvidsson/pymake/contributors) who participated in this project.

## License

This project is licensed under the MIT License—see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

n/a
