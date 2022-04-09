FROM python:latest
ADD keeper/keeper_rest_api.py /keeper/
ADD keeper/tools/news_database.py /keeper/tools/
ADD keeper/config.yaml /keeper/
ADD keeper/keeper_controller.py /keeper/
ADD tools/helper.py /keeper/tools/
ADD tools/variables.py /keeper/tools/
WORKDIR /keeper/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt