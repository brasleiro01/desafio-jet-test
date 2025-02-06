import pika
import threading
import time
import random
import json

# Parâmetros de configuração
RABBITMQ_HOST = 'rabbitmq-service'  # Alterar para o IP ou hostname do RabbitMQ
QUEUE_NAME = 'test_queue'
NUM_THREADS = 10  # Número de threads a serem usadas para gerar carga
MESSAGES_PER_THREAD = 1000  # Quantidade de mensagens a serem enviadas por thread
MESSAGE_SIZE = 1024  # Tamanho da mensagem em bytes, ajustável para gerar mais memória

# Função para enviar mensagens para o RabbitMQ
def send_message(channel):
    for _ in range(MESSAGES_PER_THREAD):
        # Gerando uma mensagem de carga
        message = 'A' * MESSAGE_SIZE  # Mensagem simulada de carga, ajustável conforme necessário
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=message
        )
        # Atraso opcional para controlar a taxa de envio
        time.sleep(random.uniform(0.001, 0.01))  # Simulando pequenas variações no envio de mensagens

# Função que será executada por cada thread
def thread_function():
    # Estabelece a conexão com o RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declara a fila (deve existir ou ser criada automaticamente)
    channel.queue_declare(queue=QUEUE_NAME)

    send_message(channel)  # Envia as mensagens

    # Fechar a conexão após o envio
    connection.close()

# Função principal que cria e executa as threads
def start_load_generator():
    threads = []

    # Cria e inicia as threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=thread_function)
        threads.append(thread)
        thread.start()

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

# Inicia o gerador de carga
if __name__ == "__main__":
    print(f"Começando a gerar carga para o RabbitMQ com {NUM_THREADS} threads...")
    start_load_generator()
    print("Carga gerada com sucesso!")
