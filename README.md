# Python Database Application for Amazon RDS PostgreSQL

## Overview

This repository contains Python scripts for setting up and manipulating data in an Amazon RDS PostgreSQL database. The scripts include DDL (Data Definition Language) for schema creation and DML (Data Manipulation Language) for managing data.

## Features

- **DDL Script**: Initializes the database schema.
- **DML Script**: Provides functionality for adding, updating, and deleting data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package installer)

### Setting up a Virtual Environment

It is recommended to create a virtual environment to manage the dependencies for your project and ensure that it does not impact other Python projects you're working on.

```bash
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Your virtual environment is now active.
```

### Installing Dependencies

With your virtual environment active, install the project dependencies using:

```
pip install -r requirements.txt
```

### Running the Data Scripts

Run **init.py** first and **dml.py** at last