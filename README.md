<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Finance Backend</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/triac-tech/finance-back)](https://github.com/triac-tech/finance-back/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/triac-tech/finance-back)](https://github.com/triac-tech/finance-back/pulls)
[![Repository size](https://img.shields.io/github/repo-size/triac-tech/finance-back?color=56BEB8)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.
- Python 3.10
- Git

```
Give examples
```

## Installing

A step by step series of examples that tell you how to get a development env running.

### Clone Project:

```
git clone git@github.com:triac-tech/finance-back.git
```

### Create Virtual Environment:

```
python -m venv 'NameEnv'
```

### Activate Virtual Environment:

Windows:
```
'NameEnv'\Scripts\activate
```
Linux:
```
source 'NameEnv'\bin\activate
```
### Migrate
```
python manage.py migrate
```

### Run Server
```
python manage.py runserver
```

### Usig Code Formater
Create folder `.vscode` in vscode IDE and after the file `settings.json`

Copy and paste the code:
```
{
    "isort.args":["--profile", "black"],
    "[python]": {
        "editor.formatOnSave": true,
    },

    "editor.rulers": [
        80
    ],
    "files.trimFinalNewlines": true,
    "files.trimTrailingWhitespace": true,
    "python.defaultInterpreterPath": "~/triactech/env/bin/python",
    "python.formatting.blackPath": "~/triactech/env/bin/black",
    "python.formatting.provider": "black",
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Path": "~/triactech/env/bin/flake8",
    "python.linting.pylintEnabled": false,
    "python.linting.enabled": true,
  }
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Language Programmation
- [Django](https://www.djangoproject.com/) - Server Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Server API Framework
- [VueJs](https://vuejs.org/) - Web Framework (Frontend)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References

Developed by [TriacTech](https://github.com/triac-tech/) © all rights reserved
