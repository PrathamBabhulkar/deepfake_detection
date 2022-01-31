# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

A flask app to detect video deepfakes.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Have the following python version

```
Python 3.9 64-bit
```

### Installing

A step by step series of examples that tell you how to get a development env running.

1. Install the dependencies using pyinstaller from ```requirements.txt```.
```
py -3.9-64 -m pip install -r requirements.txt
```

2. If ```dlib``` doesn't install on windows the use the ```dlib-19.22.99-cp39-cp39-win_amd64.whl``` file.
```
py -3.9-64 -m pip install dlib-19.22.99-cp39-cp39-win_amd64.whl
```

## Usage <a name = "usage"></a>

1. Go to the home directory and use python 3.9 to run ```main.py```.
```
py -3.9-64 main.py 
```

2. Use this command to send a post request with the video
```
curl -F file=@aagfhgtpmv.mp4 "http://127.0.0.1:5000/api"
```

3. After a while, you will recieve this response
```
{
  "message": "Fake",
  "success": true
}
```
