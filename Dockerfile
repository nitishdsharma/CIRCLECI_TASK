FROM python:alpine3.7
WORKDIR /app
COPY webservice.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["/usr/local/bin/python", "webservice.py"]
