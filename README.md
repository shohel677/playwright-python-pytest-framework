# Project documentation

E2E Test Framework with Playwright, Python, and Pytest
This repository contains a robust, scalable end-to-end (E2E) test automation framework built using Playwright, Python, and Pytest. It is designed for modern web applications and supports cross-browser testing, parallel execution, and detailed HTML reporting.

# Features

 Playwright for browser automation (Chromium, Firefox, WebKit)

 Pytest for test execution and fixture management

 HTML reporting with screenshots

 Logging system with both file and console output

 Page Object Model (POM) for clean, maintainable test code

 Custom markers for organizing smoke/regression suites

 Configurable test runs via CLI and pytest.ini

 Folder Structure

├── tests/

├── api/

├── data/

├── pages/                

├── conftest.py          

├── utils/               

├── reports/              

├── requirements.txt      

└── pytest.ini            


# Getting Started

# Install dependencies
> pip install -r requirements.txt

# Run tests and generate HTML report
pytest

To run sauce demo testcases: 

> pytest --url=https://www.saucedemo.com -m=regression

or 

> pytest --url=https://www.saucedemo.com -m=smoke

To run example testcase  

> pytest --url=https://rahulshettyacademy.com/AutomationPractice -m=details

To run apu test

> pytest -m=api
# Sample Report
Reports are generated under the reports/ directory after each run, including screenshots for passed or failed steps (if configured).


