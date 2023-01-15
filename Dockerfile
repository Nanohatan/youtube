#Grab the latest alpine image
FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./web/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
RUN pip install google-api-python-client
RUN pip install oauth2client

# Add our code
ADD ./web /opt/web/
WORKDIR /opt/web

# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# Run te app.  CMD is required to run on Heroku
# $PORT is set by Heroku

CMD gunicorn --bind 0.0.0.0:8080 wsgi 