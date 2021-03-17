# Juncus.tech

## Index

- [About](#about)

- [Getting Started](#getting-started)
- [Build using](#build-using)
- [Features](#features)
- [Author](#author)

## About

Juncus.tech is a python project that built base on Flask framework, with calculator function mainly focused on solving Canadian high-school level math problems and google form automated submitter that is capable of submitting multiple form data to google form response in clicks of button and generating corresponding visualizations from these submissions.

> The web app has been deployed on azure: https://juncus-tech.azurewebsites.net

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

To be able to run the application, **Flask** and **Python** are required.(Recommended version: Python 3.7)

#### **Running**

To run the web app, type following command in command line in your directory,

```
$ source venv/Scripts/activate
$ flask run
```

You will see output similar as below,

```
FLASK_APP = app.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder C:/...
C:\...\Juncus.tech\venv\Scripts\python.exe -m flask run
 * Serving Flask app "app.py"
 * Environment: development
 * Debug mode: off 
```

And you can see the web app running on http://127.0.0.1:5000/

## Build using

- Python 3.7 - Language
- Bootstrap 4 Keen Theme - UI Framework
- Vue.js - Web Framework
- Flask - Server Framework

## Features

- Calculators

  - Decibel Calculator

    Convert decibel to energy flux or compare two decibels intensity.

  - Earthquake Magnitude Calculator

    Convert earthquake magnitude to Joules or compare two magnitudes based on Richter scale.

- Form submission generator(Project Friend-Free)

  - Web Crawling

    User key in the google form URL that ends in "/viewform" and the number of submission they required, the server uses [beautiful soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to get the html and transfers the result back to front-end using [ajax](https://api.jquery.com/jquery.ajax/), the data is stored in front-end using [Vue.js](https://vuejs.org/index.html).

  - Graph generate

    The graphs are created using [apexChart.js](https://apexcharts.com/) according to the data that stored in [Vue.js](https://vuejs.org/index.html) and the numbers which are determined by users.

  - Form submissions

    The forms will be submitted using requests and by using [socket.io](https://socket.io/), users will be able to see the real-time process status of the submissions.

## Author

- [Wang Yang](https://github.com/NorthstarWang)
