# Hospital Adminstration System


## High-level Description

The software is designed to be used by hospital managers to enter some daily information about their hospital, and officials to keep track of these information.

It has two separate interfaces, one for each type of users.

## Design

* The system is divided into 3 separate layers, each in it's own top-level directory:
    1. Data Layer: contains the database
    1. Application Layer: contains the back-end of the system which handles access to database and stats calculation
    1. GUI Layer: contains the user interface of the system
* We decided not to make the system password protected for the following reasons:
    1. It was not specifically required from the "client"
    1. We didn't feel it's necessary, considering that nobody will actually use this system
* A relational database, sqlite, is used in the data layer. At first, we were inclined to just use a simple `csv` file to keep track of the records, but then decided that it's time to try something outside our comfort zone.
* The system is written as a `python` library. The rationale behind choosing `python` is obvious. And the decision to make it into a library is just a convenience for us as developers and for any potential user to facilitate the setup process.

## Installation

We assume that if you're reading this, then you already have the source code downloaded and ready. If that's not the case, request the code from one of us, or if you have access to the `github` repository, clone it as follows:
* `git clone https://github.com/MennaEwas/Hospital-Adminstration-interface.git`

We recommend that you make a virtual environment to install the library in first. But this is completely optional.

1. cd to the directory containing the setup script `setup.py`
1. Run `pip install .`

Make sure that `pip3` is used not `pip2`. On unix systems you can use `pip3 install .`. On windows, make sure that `python 3.x` is the one included in the system `PATH`.

## Usage

1. cd to the high-level directory of the software `/hospital`.
1. Run `python hospital_system -u official` to run the system as an official, or `python hospital_system -u manager` to run as manager.

Make sure the `python 3.x` is used. On unix system, you can use `python3` instead of `python` to specify the python version.
