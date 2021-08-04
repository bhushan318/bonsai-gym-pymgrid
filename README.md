# Bonsai Gym Pymgrid

A python library for integrating Bonsai brains with Pymgrid environment using Open AI Gym.


## Installation

One of the requirements `bonsai-common` is not located on pypi and must be installed from the github repo

`$ pip install git+https://github.com/microsoft/bonsai-common`

Install the latest bonsai-gym-pymgrid from github.

`$ pip install git+https://github.com/bhushan318/bonsai-gym-pymgrid

## Usage

Once installed, import `bonsai_gym-pymgrid` in order to access
base class `GymSimulator3`, which implements all of the
environment-independent Bonsai SDK integrations necessary to
train a Bonsai BRAIN to play an pymgrid using OpenAI Gym simulator.
