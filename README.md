Análise de Acesso a Logs

Este script Python foi desenvolvido para analisar arquivos de log do servidor Nginx e identificar os IPs mais acessados durante um determinado intervalo de tempo. Ele extrai os IPs dos arquivos de log, contabiliza as ocorrências de cada IP e os classifica por número de acessos. Além disso, foi implementado um filtro para considerar apenas os registros dentro do intervalo de tempo das 18:00 às 06:00.

Como Usar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Baixe o arquivo analyze_logs.py neste repositório.
3. Coloque seus arquivos de log do Nginx no mesmo diretório do script ou especifique o caminho para os arquivos no código.
4. Execute o script com o comando python analyze_logs.py.
5. O script gerará um arquivo de texto chamado ips_mais_acessados_no_intervalo.txt com os IPs mais acessados dentro do intervalo de tempo especificado.

Pré-requisitos

    Python 3.x

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com sugestões de melhorias, correções de bugs ou novos recursos.
Licença

Este projeto está licenciado sob a Licença MIT.
