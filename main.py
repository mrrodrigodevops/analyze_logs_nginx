import ipaddress
from datetime import datetime

# Lista de arquivos de log
log_files = ['access.log']

# Dicionário para contar ocorrências de IPs
ip_count = {}

# Função para verificar se um timestamp está dentro do intervalo de tempo especificado (23:00 às 05:00)
def is_within_time_range(timestamp):
    time_format = '%d/%b/%Y:%H:%M:%S'
    time_obj = datetime.strptime(timestamp, time_format)
    hour = time_obj.hour
    return hour >= 23 or hour < 5

# Iterar sobre todos os arquivos de log
for file in log_files:
    with open(file, 'r') as f:
        # Ler o conteúdo do arquivo linha por linha
        for line in f:
            # Extrair IP e timestamp
            parts = line.split(' ')
            ip = parts[0]
            timestamp = parts[3][1:]
            # Verificar se o timestamp está dentro do intervalo de tempo especificado
            if is_within_time_range(timestamp):
                try:
                    # Tentar criar um objeto de endereço IP a partir da string
                    ip_obj = ipaddress.ip_address(ip)
                    # Adicionar o IP ao dicionário de contagem
                    ip_count[ip] = ip_count.get(ip, 0) + 1
                except ValueError:
                    # Ignorar linhas que não contêm um IP válido no início
                    continue

# Classificar os IPs por número de ocorrências
sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)

# Nome do arquivo de saída
output_file = 'ips_mais_acessados_no_intervalo.txt'

# Abrir o arquivo de saída em modo de escrita
with open(output_file, 'w') as f:
    # Escrever os IPs mais acessados no arquivo
    f.write("IPs mais acessados no intervalo de tempo das 23:00 às 05:00:\n")
    for ip, count in sorted_ips:
        f.write(f"{ip}: {count} vezes\n")

print(f"Resultados salvos em '{output_file}'.")
