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

### Endpoints

The Ackermann endpoint requires two parameters:
```
/api/ackermann?m=1&n=2
```

The factorial endpoint requires one parameter:
```
/api/factorial?n=3
```

The Fibonacci endpoint requires one parameter:
```
/api/fibonacci?n=5
```

All parameters are non-negative integers.

The expected response is an object with the attribute `result`:
```json
{"result": 7}
```

## Monitoring

---
Local monitoring can be done with the application log. It is also saved to a file.

A summary report is available running: 
```bash
python resources/reports.py
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

### Monitoring
The application logs are sent to CloudWatch. It is possible to create metrics and alerts.

### Cleanup
```bash
sls remove
```
