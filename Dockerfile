FROM python:latest
LABEL authors="farid"

WORKDIR /src/
COPY requierments.txt src/
RUN pip install -U pip
COPY . /src/
RUN pip install -r requierments.txt


CMD ["python","manage.py", "runserver", "0.0.0.0:3000"]