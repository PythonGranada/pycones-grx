FROM python:3.6-slim

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PORT=8000
EXPOSE $PORT

RUN apt-get update \
    && apt-get install --no-install-recommends -qy git curl bash


RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

COPY requirements.txt /
RUN pip install -r /requirements.txt


WORKDIR /project-root

COPY compose/develop_server.sh /
RUN chmod +x /develop_server.sh

CMD /develop_server.sh start $PORT
