Scan de IP e Porta em Python

Este código em Python permite realizar um scan de IP e porta na sua rede local.
Requisitos

    Python 3.x
    Biblioteca socket

Uso

O código irá obter automaticamente o endereço IP da máquina local e gerar a faixa de IPs na sua rede local. Em seguida, verificará se os hosts na faixa de IP estão ativos e se os ports 21, 22, 80, 443 e 8080 estão abertos ou fechados.

Os resultados serão exibidos na tela como um print, informando se o host e a porta estão ativos ou inativos.
Considerações

    O tempo de execução do código pode ser prolongado dependendo da quantidade de hosts na sua rede.
    A detecção de atividade de um host depende da configuração do firewall e do sistema operacional do host.
    É importante ter cuidado ao usar este código, pois ele pode ser considerado como uma forma de invasão de privacidade. Certifique-se de ter autorização para realizar scans em sua rede local.
