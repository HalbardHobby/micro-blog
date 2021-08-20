FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=/usr/src/app
ENV FLASK_ENV=development

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
