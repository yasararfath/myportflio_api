FROM python:3.9

WORKDIR '/portfolio'

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

CMD ["uvicorn","app.main:app","--port","8000"]