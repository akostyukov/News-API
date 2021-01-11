FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

ENV APP_HOME=/news-api/
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

COPY Pipfile $APP_HOME
COPY Pipfile.lock $APP_HOME
RUN pip install pipenv
RUN pipenv install --system

COPY /src /news-api/src
