# Juncus.tech

## Index

- [About](#about)

- [Getting Started](#getting-started)
- [Build using](#build-using)
- [Features](#features)
- [Author](#author)

## About

Juncus.tech is a python project that built base on Flask framework, with calculator function mainly focused on solving Canadian high-school level math problems and google form automated submitter that is capable of submitting multiple form data to google form response in clicks of button and generating corresponding visualizations from these submissions.

> The web app has been deployed on azure: https://juncus.azurewebsites.net/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

To be able to run the application, **Flask** and **Python** are required.(Recommended version: Python 3.7)

#### **Running**

To run the web app, first change the path of home in venv/pyvenv.cfg, then type following command in command line in your directory,
For Mac/Linux
```
$ source venv/Scripts/activate
$ flask run
```
For Window(First line of code prevent digital sign check)
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate
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

## Copyright

- [Ownership of copyright](ownership-of-copyright)
- [Copyright license](#copyright-license)
- [Data mining](#data-mining)
- [Permissions](#permissions)
- [Enforcement of copyright](#enforcement-of-copyright)
- [Infringing material](#infringing-material)

#### Ownership of copyright

I own the copyright in:

1. this website; and
2. the material on this website (including, without limitation, the text, computer code, images, artworks on this website).

#### Copyright license

We grant to you a worldwide non-exclusive royalty-free revocable license to:

1. View this website and the material on this website on a computer via a web browser;
2. Copy and store this website and the material on this website in      your web browser cache memory; and
3. Print pages from this website for your own [personal and non-commercial] use.

We do not grant you any other rights in relation to this website or the material on this website. In other words, all other rights are reserved.

For the avoidance of doubt, you must not adapt, edit, change, transform, publish, republish, distribute, redistribute, broadcast, rebroadcast or show or play in public this website or the material on this website (in any form or media) without our prior written permission.

#### Data mining

The automated and/or systematic collection of data from this website is prohibited.

#### Permissions

You may request permission to use copyright materials on this website by writing to 1527638985@qq.com

#### Enforcement of copyright

We take the protection of its copyright very seriously. If We discover

that you have used our copyright materials in contravention of the license above, we may bring legal proceedings against you seeking monetary damages and an injunction to stop you using those materials. You could also be ordered to pay legal costs.

If you become aware of any use of our copyright materials that contravenes or may contravene the license above, please report this by email to 1527638985@qq.com

#### Infringing material

If you become aware of any material on the website that you believe infringes your or any other person's copyright, please report this by email to 1527638985@qq.com

## Author

- [Wang Yang](https://github.com/NorthstarWang)
