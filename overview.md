## Overview

main.py is a python script that extracts, transforms and saves data from the random user api.

## Set up Details & Instructions

Set up your virtual environment using the requirements.txt file.

Run main.py to extract, transform and save the data.

The log file will be saved as randomuser_log.log

The utils file contains all of my code for the interview.

## Known limitation or Inefficiencies.

Securing the venv with poetry or pipenv or conda would be better than using a requirements.txt file.

The code does not handle paginations in the API since I was unable to find it's limit.

To fix this one could limit the number of requests upon an arbitrary number.

If the process ran into an error, it would not be able to restart or continue mid process.

I catch general errors and log them to the log file.

Saving the data to CSV is not storage efficient.

A python class could be used to encapsulate these functions together.

I did not write any unit tests for the code.

I did not write a shell script for when this needs to be executed.

Importing all libraries instead of just the ones I need for example import requests instead of from requests import get.