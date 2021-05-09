# Mathematical Web Service
A REST API that calculates mathematical functions.


## Install

---

It is recommended to create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

To install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

---
To run the app:
```bash
flask run
```

## Run tests

---
To run the tests:
```bash
pytest
```

## Deploy

---

### Prerequisites

- [npm](https://www.npmjs.com/get-npm)
- [Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/quick-start/)
- Configure [AWS credentials](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

### Install
```bash
npm install
```

### Local tests
It is possible to emulate AWS Lambda and API Gateway on the local machine:
```bash
sls wsgi serve
```

### Deploy to AWS
```bash
sls deploy
```

### Cleanup
```bash
sls remove
```
