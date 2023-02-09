"""
Este código em Python utiliza a biblioteca socket para realizar um scan de IP e porta na sua rede local. Ele define duas funções: ip_scan e main.

A função ip_scan aceita dois argumentos: ip_range e port_range. Ela itera sobre os endereços IP e as portas informadas,
criando um socket para cada combinação de endereço IP e porta. A função connect_ex é usada para verificar se o host e a porta estão ativos ou inativos. Os resultados são exibidos na tela como um print.

A função main obtém o endereço IP da máquina local e gera a faixa de IPs na sua rede local. Em seguida, 
chama a função ip_scan com a faixa de IPs e uma lista de portas a serem verificadas.

O código é executado ao final com a verificação if __name__ == '__main__'. Isso significa que o código será executado somente se ele for o arquivo 
principal e não se ele for importado como uma biblioteca em outro código.
"""

import socket

# Função que realiza o scan de IP e porta
def ip_scan(ip_range, port_range):
    # Loop sobre cada endereço IP na faixa
    for ip in ip_range:
        # Loop sobre cada porta na lista de portas
        for port in port_range:
            # Criar o socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Definir timeout para 0,5 segundos
            sock.settimeout(0.5)
            # Tentar conectar ao endereço IP e porta especificados
            result = sock.connect_ex((ip, port))
            # Verificar se a conexão foi bem-sucedida
            if result == 0:
                print(f'O host {ip}:{port} está ativo')
            else:
                print(f'O host {ip}:{port} está inativo')
            # Fechar o socket
          

# Função principal que gerencia o processo de scan
def main():
    # Obter o endereço IP da máquina local
    hostname = socket.gethostbyname(socket.gethostname())
    # Gerar a faixa de IPs na rede local
    ip_range = [f'{hostname.rsplit(".", 1)[0]}.{i}' for i in range(1, 256)]
    # Lista de portas a serem verificadas
    port_range = [21, 22, 80, 443, 8080]
    # Realizar o scan de IP e porta
    ip_scan(ip_range, port_range)

# Verifica se o código está sendo executado como o arquivo principal
if __name__ == '__main__':
    # Executar a função principal
    main()
