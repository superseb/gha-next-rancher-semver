FROM python:3.10-slim-buster

RUN apt update && apt -y upgrade

COPY . /
RUN pip3 install --no-cache-dir -r /requirements.txt

ENTRYPOINT [ "python", "/get-new-semver.py" ]
