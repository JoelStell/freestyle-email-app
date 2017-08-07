<!-- # Record Alteration Control - Python

## Prerequisites

Follow the [Setup Guide](SETUP.md) to obtain and configure credentials for using the SendGrid service to send email. And for configuring a machine to run this application.

## Installation

Install Python 3.x.

Install source code:

```shell
git clone https://github.com/JoelStell/freestyle-email-app
cd freestyle-email-app/
```

Install package dependencies:

```shell
pip3 install -r requirements.txt
```

## Usage

This program for quality control of the junior accountants who work at my company. The program will allow the user to list, show, update and add new records. If the user updates or creates a new record an email will be sent for authorization. This is to add a control for any new or altered record entered into the system. The delete function has been removed for quality control as junior accountant do not have access to that right.

```shell
python3 app/email_me.py
```

## Deploying - not a funciton of this project

Optionally follow the [Deployer's Guide](DEPLOYING.md) to run the application on a Heroku server previously created during the setup process. -->
