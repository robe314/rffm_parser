## Ejecutar "docker build -t bot_png ."

FROM python
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "bot_telegram_png.py"]