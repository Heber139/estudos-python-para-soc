# Desafio 2: Fundamentos de Python - Condicionais (if/else)

Este script é a solução para o segundo desafio prático do treinamento "Python para SOC", com foco no uso de estruturas condicionais para tomar decisões.

## 🎯 Objetivo

Simular um processo de verificação de segurança, onde uma lista de endereços de IP é analisada e comparada com uma "lista negra" (blacklist) para decidir se uma ação de bloqueio é necessária.

## 🛠️ O que eu aprendi e pratiquei:

- **Estruturas Condicionais `if/else`:** Como fazer o programa tomar caminhos diferentes com base em uma condição.
- **Operador `in`:** A forma eficiente de verificar se um item existe dentro de uma lista.
- **Combinação de `for` e `if`:** Como aplicar lógica de decisão em cada item de uma lista.
- **f-strings:** Impressão de mensagens com dados dinâmicos de forma clara e legível.

## 🐍 Código da Solução

```python
# Lista de IPs que serão analisados quanto à segurança
ips_para_analisar = ['192.168.1.1', '8.8.8.8', '10.0.0.5', '1.1.1.1']

# Lista de IPs suspeitos ou maliciosos que devem ser bloqueados
ips_maliciosos = ['8.8.8.8', '1.1.1.1']

# Início da verificação de IPs
print("--- Iniciando verificação de IPs ---")

# Loop para verificar cada IP na lista de análise
for ip in ips_maliciosos:
    # Verifica se o IP atual está presente na lista de ips_maliciosos
    if ip in lista_negra_ips:
        # Alerta de que o IP é malicioso e será bloqueado
        print(f"ALERTA: O IP {ip} está na lista negra e será bloqueado!")
    else:
        # Informação de que o IP é considerado seguro
        print(f"INFO: O IP {ip} é seguro.")

# Indica que a verificação foi concluída
print("--- Verificação concluída ---")
