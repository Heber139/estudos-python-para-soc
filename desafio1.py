# Criando a lista de IPs para bloquear
ips_para_bloquear = ['8.8.8.8', '1.1.1.1', '9.9.9.9']

# Criando o dicionário com detalhes do incidente
detalhes_incidente = {
    'id': 775,
    'motivo': 'Múltiplas tentativas de login com falha',
    'analista_responsavel': 'Heber'
}

# Mostrando o motivo do incidente
print("Motivo do incidente:")
print(detalhes_incidente['motivo'])

# Iterando sobre a lista e mostrando a ação de bloqueio
print("--- Iniciando bloqueio de IPs ---")
for ip in ips_para_bloquear:
    print(f"Bloqueando o IP: {ip}")
