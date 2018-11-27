# SciDocParser (alias)

## About
(Under development)
Reading through scientific documents is an integral part of academic research. These papers often utilize numerous variables that are defined and ... . This tool aims to improve productivity by removing the need to scroll...

## Built With
  * [Python 3](https://www.python.org/) (version 3.7.1 or later)
  * [Django](https://www.djangoproject.com/) (version 2.1.3)
  * [OpenCV](https://www.opencv.org/) (version 3.4.3.18)
  * [PyTesseract](https://github.com/madmaze/pytesseract) (version 0.2.5)
  * [pdf2image](https://github.com/Belval/pdf2image) (version 1.1.0)
  * [Pillow](https://python-pillow.org/) (version 5.3.0)
  * [pytz](http://pytz.sourceforge.net/) (2018 July)
  * ...
  
## How to Use
To use the deployed web application, simply visit [notaurl.com](https://github.com/shoyo-inokuchi/SciDocParser)  

To run the web application for development purposes, follow the steps below.
### Prerequisites
Before proceeding, be sure that the latest version of Python 3 and pip are installed (version 3.7.1 or later). If not, you can visit the [official Python page](https://www.python.org/) to download Python 3. The pip package manager will be installed with Python 3 by default.

The packages required for development are listed in the preceding *Built With* section. It's recommended to first set up a [virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to isolate these packages from your other projects during development.

### Setting up a virtual environment
A virtual environment allows you to isolate packages and prevent them from interfering with other projects you may have on your computer. If you anticipate heavy use of virtual environments in the future, consider using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), which manages all of your virtual environments in one place.

Install virtualenv by typing into the command line:

    pip3 install virtualenv

For the sake of this demonstration, we will refer to our virtual environment as "test-venv".  
Make a directory for the virtual environment with:

    mkdir test-venv
  
Create the virtual environment with:

    virtualenv test-venv
    source test-venv/bin/activate

### Installation
After creating your virtual environment, obtain a local copy of this repository with:

    git clone https://github.com/shoyo-inokuchi/SciDocParser.git
   
Install the packages with:

    pip3 install -r requirements.txt
   
## Authors
  * Shoyo Inokuchi - _initial work_ - ...
  * Taiga Ono - _initial work_ - ...
  * Shota Kaieda - _initial work_ - ...
  
## Contributing
Any contributions for further development (testing, parser improvements, UI/UX improvements, etc.) are all welcome!
Submit an issue or pull request.

## License
To be determined.
