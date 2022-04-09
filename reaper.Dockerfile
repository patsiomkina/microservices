FROM python:latest
ADD reaper/reaper_rest_api.py /reaper/
ADD reaper/tools/http_client.py /reaper/tools/
ADD reaper/tools/rss_parser.py /reaper/tools/
ADD reaper/config.yaml /reaper/
ADD reaper/reaper_controller.py /reaper/
ADD tools/helper.py /reaper/tools/
ADD tools/variables.py /reaper/tools/
WORKDIR /reaper/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt