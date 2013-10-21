Olle & Maija Portfolio
======================

## About
myFlaskProject is a template-based webserver created by Olle Kvarnström and Maija Vilkinia.
Our goal is to provide a simple-to-use webserver for users who may not have much experience with HTML.

Here follows technical instructions on installation, etc. If you are looking for the user manual, please see the doc folder.

Installation
------------
There are two dependencies for myFlaskProject: Python (version 3.3.2 or higher) and Flask.
Since we recommend running Flask inside virtualenv, we've included it in our instructions.
### Windows
**NOTE: Support for the Windows operating systems is experimental at best! Please use Mac OS X or Linux instead!**
**Step1: Installing Python and VirtualEnv**
> Download and install Python from this [link](http://python.org/download/). Please install it to C:\Python33 as is the default.
> Download and extract VirtualEnv, which can be found here: [link](https://pypi.python.org/pypi/virtualenv)
> Open up Command Prompt and navigate to the folder where you extracted VirtualEnv
> Type the following and press enter: `C:\Python33\python.exe setup.py install`
> Now you have installed both Python And VirtualEnv. If you like you can remove the extracted folder.

**Step 2: Fetch the newest myFlaskProject build**
> Download the latest version of myFlaskProject through this [link](http://gitlab.ida.liu.se/ip-arbeten-2013/tdp003/repository/archive) (requires a valid LiU-ID).
> Extract the contents to a suitable location (choose a location wisely, as moving it later might cause issues).
> Open up Command Prompt and navigate to the newly extracted folder, then open tdp003. Here we will initialise a virtual environment, so please run the following command:
> `C:\Python33\python.exe -m virtualenv venv`
> This will create a new virtual environment which you will need to "activate" every time before starting of stopping myFlaskProject.
> Activating is done by typing this: (please do so now)
> `venv\scripts\activate`
> Now, the last step is installing Flask, type the following:
> `pip install flask`

### Mac OS X
*Step1: Installing Python and VirtualEnv**
> Download and install Python from this [link](http://python.org/download/).
> Download and extract VirtualEnv, which can be found here: [link](https://pypi.python.org/pypi/virtualenv)
> Open up a terminal (if you have not already) and navigate to the folder where you extracted VirtualEnv
> Type the following and press enter
> `sudo python3 setup.py install`
> Now you have installed both Python And VirtualEnv. If you like you can remove the extracted folder.

**Step 2: Fetch the newest myFlaskProject build**
> Download the latest version of myFlaskProject through this [link](http://gitlab.ida.liu.se/ip-arbeten-2013/tdp003/repository/archive) (requires a valid LiU-ID).
> Extract the contents to a suitable location (choose a location wisely, as moving it later might cause issues).
> Open up a terminal (if you haven't done so already) and move to the extracted folder, then tdp003. Here we will initialise a virtual environment, so please run the following command: 
> `virtualenv venv`
> This will create a new virtual environment which you need to "activate" every time before starting or stopping myFlaskProject.
> Activating is done by typing this: (please do so now)
> `. venv/bin/activate`
> Now, the last step, is installing Flask
> `pip install flask`

### Linux
**Step 1: Install Python and VirtualEnv**
> If you have Debian/Ubuntu or similar, run this in your terminal:
> `sudo apt-get update && sudo apt-get install -y python3 virtualenv`
> If you have Fedora/RHEL or similar, run this in your terminal:
> `yum install python3 virtualenv`
> If you have Slackware, there are slackbuilds [here](http://slackbuilds.org/repository/14.0/python/python3/) and [here](http://slackbuilds.org/repository/14.0/python/virtualenv/).

**Step 2: Fetch the newest myFlaskProject build**
> Download the latest version of myFlaskProject through this [link](http://gitlab.ida.liu.se/ip-arbeten-2013/tdp003/repository/archive) (requires a valid LiU-ID).
> Extract the contents to a suitable location (choose a location wisely, as moving it later might cause issues).
> Open up a terminal (if you haven't done so already) and move to the extracted folder, then tdp003. Here we will initialise a virtual environment, so please run the following command: 
> `virtualenv venv`
> This will create a new virtual environment which you need to "activate" every time before starting or stopping myFlaskProject.
> Activating is done by typing this: (please do so now)
> `. venv/bin/activate`
> Now, the last step, is installing Flask
> `pip install flask`

## Managing the application
### Starting/Stopping the webserver
In order to start or stop the webserver you will need to open up a terminal and nagivate to the folder where you installed myFlaskProject.
Here you can type in one of the following commands and then press enter:
`python web/myFlaskProject.py start`
`python web/myFlaskProject.py stop` (not available to windows)

If you receive the following error message *Unable to import flask. Did you maybe forget to initialize venv?* you need to run this command and then try again:
`. venv/bin/activate` (or `venv\scripts\activate` if using Windows)

If you are using Linux or Mac OS X, the webserver will detach from your shell and run as a background process ("daemon").
This means that you will be able to logout from your account and the webserver will continue running.
However, if you are using windows, the webserver will run inside your terminal window. 
This means that if you close the window or log out, the webserver will shut down as well.

### User Manual
Please see the doc folder for a user manual

### Logging
The application will create a "log"-file in the tdp003-directory, which will record all access to the webserver.
Please do not modify the log-file while myFlaskProject is running, as doing so may cause it to stop logging and/or to shut down.

### PID
You may also notice a file named "pid". Please keep your paws off this file as it tracks the running process ID.