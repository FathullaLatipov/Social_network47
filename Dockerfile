FROM python:latest

COPY . /Social-network47

WORKDIR / Social-network47

RUN pip install -r requirements.txt

CMD ['uvicorn', 'main:app', '--reload', '--host=0.0.0.0', '--port=2525']