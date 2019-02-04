FROM alpine:3.8
MAINTAINER Mirek

RUN apk add python3 py-pip && python3 -m ensurepip && pip install --upgrade pip && pip install flask
# RUN easy_install pip

# prepare app folder
# WORKDIR /app
RUN mkdir /app

# copy app and templates to the container
COPY app.py /app
COPY templates /app

# ENTRYPOINT ["python"]

# run the app using python
CMD ["python", "/app/app.py"]
