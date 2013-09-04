============
Installation
============

Using pip
=========

At the command line::

    $ pip install {{ cookiecutter.repo_name }}

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv {{ cookiecutter.repo_name }} -i {{ cookiecutter.repo_name }}

From Source
===========

In order to install from source simply type::

    $ git clone http//github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    $ cd {{ cookiecutter.repo_name }}
    $ mkvirtualenv {{ cookiecutter.repo_name }}
    $ python setup.py install
