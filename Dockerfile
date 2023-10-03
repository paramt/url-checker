FROM python:3.11-alpine

ADD check_links.py /check_links.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN chmod +x check_links.py
ENTRYPOINT ["/check_links.py"]
