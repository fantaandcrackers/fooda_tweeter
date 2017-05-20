# fooda_tweeter
# Arthur Shir

Description:
This app uses a virtualenv virtual environment for storing pip packages as well as the Click python package for creating the command line interface. Install by creating and activating a virtual environment, installing dependancies, and running python setup.py script. Alternatively, just run the install.sh. Please note, to run the commandline tool you must be in the virtualenvironment.

Installation Dependancies:
- pip
- virtualenv

Manual Installation:
1. Install virtual environment: 'virtualenv venv'
2. Activate virtual environemnt: 'source venv/bin/activate'
3. Install pip requirements: 'pip install -r requirements.txt'
4. Install fooda_tweeter by using setup.py: 'python setup.py install'

Automated Installation (install.sh):
1. Allow execution permissions for installation script: 'sudo chmod +x install.sh'
2. Run installation script: './install.sh'

Usage:
1. Load Virtual Environment by running 'source venv/bin/activate'
2. Run with: 'fooda_tweeter <@ + twitter handle> <number of tweets>''