### order-anymarket-fallback

O projeto tem como objetivo realizar uma chamada ao webhook do API Gateway passando o valor SYNC no tipo de evento, isso fará com que o serviço `ecommerce-job-anymarket` seja acionado e o mesmo faça a requisição de todos os pedidos de um intervalo de tempo (data atual - 1 dia) para verificar se algum ficou de fora da integração.

O script rodará via Rundeck uma vez ao dia as 4:00 am no ambiente de produção.