FROM python:3.9-alpine
MAINTAINER gpiechnik2
LABEL Name=byship Version=1.0

# Install pip3
RUN apk add --update py-pip

# Copy and install app with single one dependency
COPY . /app
WORKDIR /app

# Install byship
RUN pip3 install -r requirements.txt
RUN pip install --editable .

ENTRYPOINT ["byship"]
