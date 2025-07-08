# Lista de IPs que serão analisados quanto à segurança
ips_para_analisar = ['192.168.1.1', '8.8.8.8', '10.0.0.5', '1.1.1.1']

# Lista negra de IPs suspeitos ou maliciosos que devem ser bloqueados
lista_negra_ips = ['8.8.8.8', '1.1.1.1']

# Início da verificação de IPs
print("--- Iniciando verificação de IPs ---")

# Loop para verificar cada IP na lista de análise
for ip in ips_para_analisar:
    # Verifica se o IP atual está presente na lista negra
    if ip in lista_negra_ips:
        # Alerta de que o IP é malicioso e será bloqueado
        print(f"ALERTA: O IP {ip} está na lista negra e será bloqueado!")
    else:
        # Informação de que o IP é considerado seguro
        print(f"INFO: O IP {ip} é seguro.")

# Indica que a verificação foi concluída
print("--- Verificação concluída ---")
