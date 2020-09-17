FROM jupyter/scipy-notebook

COPY requirements.txt .
COPY notebooks notebooks
COPY output output
COPY data data

RUN pip install -r requirements.txt 

