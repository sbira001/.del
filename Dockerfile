FROM python:latest
ADD server.py /server/
WORKDIR /server/
EXPOSE 12121
CMD [ "python3", "/server/server.py" ]
