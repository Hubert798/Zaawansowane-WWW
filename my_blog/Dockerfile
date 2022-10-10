FROM python:3.9
EXPOSE 8000
COPY . /opt/app/
COPY requirements.txt /opt/app/
WORKDIR /opt/app/
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD [ "/entrypoint.sh" ]