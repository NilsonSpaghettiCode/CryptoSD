.. CryptoSD documentation master file, created by
   sphinx-quickstart on Thu Oct 14 22:38:45 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CryptoSD documentation!
======================================
Hey welcome, do you want a cookie? :)

What is CryptoSD?
==================
CryptoSD is a software made with Python and the framework Flask, to simulate,
the function of Blockchain, using distributed systems for each one of the
components

Getting Started
==================

For start you should clone the next repository that contains all the code of CryptoSD project.
``Repository: https://github.com/NilsonVargas/CryptoSD``
 
.. Note:: For that you getting started you should have ``Python in version 3.6.0 or later``, 
   and then you could run the following commands that allows you to use the program.

Virtual environment
===================
It is important to use the virtual environment because it allows you to maintain the same 
version of dependencies for all members of the group of developers

Linux
-----
>>> (bash) python3 -m venv name_env

Activate the virtual environment

>>> (bash) cd name_env && source bin/activate

Windows
-------

>>> python -m venv name_env

Now, enter to the environment and activate it

>>> cd name_env/Scripts && activate
   
Install the depedencies of the project inside the virtual environment using the follow command

>>> (env) cd CryptoSD && pip install -r requirements.txt

and if you download new dependencies use the command for update the requirements.txt

>>> (env) pip freeze > requirements.txt

.. Note:: Update the requirements.txt always in the root folder.

Deploy the services as components
=================================
The next step, consist in running the components in different containers using your workspace (env).

>>> (env) python main_coordinator.py
Shape example running a service: python name_component.py

Contents for each components
================================
.. toctree::
   :maxdepth: 1
   :caption: Contents:

   blockchain
   opencloser
   register
   coordinator


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
