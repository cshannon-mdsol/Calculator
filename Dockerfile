FROM python:3

ADD src /src

CMS [ "python", "./src/calculatorTests.py"]