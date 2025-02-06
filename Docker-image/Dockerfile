FROM python:3.9-slim

# Instalar pika
RUN pip install --upgrade pip
RUN pip install pika

# Copiar o script Python para o contêiner
COPY gerador_de_logs.py /gerador_de_logs.py

# Executar o script
CMD ["python", "/gerador_de_logs.py"]