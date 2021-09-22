FROM tiangolo/uwsgi-nginx-flask

WORKDIR /python-flask
ADD . /python-flask
EXPOSE 5000
RUN python3 -m pip install -r requirements.txt
#RUN python3 -m pip install gunicorn

CMD ["gunicorn"  ,"--workers=2", "--timeout=5000","-b", "0.0.0.0:5000", "api:app"]
#CMD ["python", "api.py"]

