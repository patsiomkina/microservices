FROM python:latest
ADD master/master_rest_api.py /master/
ADD master/config.yaml /master/
ADD master/master_controller.py /master/
ADD tools/helper.py /master/tools/
ADD tools/variables.py /master/tools
WORKDIR /master/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt