# desafio-jet-test
**Tarefas**

**1- Configuração de Rede (Networking)**

```
    1.1- Criar duas VCNs na OCI, separadas em diferentes domínios de falha ou regiões.
    -   criado duas vcn sendo uma em são paulo e outra em vinhedo
        vcn-sp1
        vcn-vi1
    1.2- Configurar VCN Peering entre as redes.
    -   Dynamic Routing Gateway Attachments     - drg-sp

    1.3- Criar as subnets e regras necessárias para suportar o tráfego entre os serviços.
    -   subnets     -oke-lb     - subnet criada para loadbalance
                    -oke-api    - subnet criada para aplicação
                    -oke-node   - subnet criada para comunicação dos nodes

    -   tabelas de roteamento   - oke-public    - para comunicação externa do cluster
                                - oke-private   - para comunicação interna do cluster
    
    -   gatway de internet      - ig-sp1

    -   lista de segurança      - oke-lb
                                - oke-api
                                - oke-node

    -   gateway nat             - oke-ngw

    -   gateway de serviço      - oke-sgw

    -   regras de entrada       -  liberação das portas tcp 6443, 12250 
    -   regras de saida         -          
```
#

**2- Provisionamento da Infraestrutura**

```
    2.1- Subir um cluster Kubernetes (OKE ou manual).
    -   criação do cluster "teste-marcus" setando a rede e subnets que foram criadas nos itens a cima
    -   3 nodes
    -   cluster simples

    2.2- Criar um Deployment do RabbitMQ configurado para escalar automaticamente.
    -   deployment criado manifests/rabbit.yaml com inclusão dos plugins necessário para ser gerado as metricas para o prometheus

    2.3- Configurar um HPA (Horizontal Pod Autoscaler) para o RabbitMQ baseado no consumo de CPU/memória.
    -   hpa criado manifests/hpa.yaml
```
#

**3- Testes de Estresse**

```
    3.1- Criar um gerador de carga que publique mensagens no RabbitMQ de forma massiva (por exemplo, usando Gatling, Locust, ou um simples script em Python com threads).
    - criado um script python para realizar a atividade consequentemente criei uma imagem docker para executar o mesmo dentro do cluster os arquivos estão na pasta /Docker-image/
    -   OBS- caso o container não suba pode rodar o scripit na própria maquina.

    3.2- O teste deve provocar um aumento de consumo e forçar o escalonamento automático do RabbitMQ.
    - escalonamento programado para até 20 replicas quando 
    o rabbit chegar em 30% de utilização de CPU
```
#

**4- Monitoramento e Observabilidade**

```
    4.1- Configurar Prometheus e Grafana para coletar métricas do RabbitMQ.
    -   stack do prometheus configurada para coletar as metricas do serviço do rabbit e integrado com o grafana

    4.2- Monitorar métricas como fila de mensagens, consumo de CPU/memória e taxa de processamento.
    -   serviços monitorados e exibido com o dashboard oficial do rabbit

    4.3- Configurar alertas no Grafana ou na OCI Monitoring para identificar picos de carga e escalonamento.
```
#    