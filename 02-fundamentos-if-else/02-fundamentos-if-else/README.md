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
ips_para_analisar = ['192.168.1.1', '8.8.8.8', '10.0.0.5', '1.1.1.1']
lista_negra_ips = ['8.8.8.8', '1.1.1.1']

print("--- Iniciando verificação de IPs ---")

for ip in ips_para_analisar:
    if ip in lista_negra_ips:
        print(f"ALERTA: O IP {ip} está na lista negra e será bloqueado!")
    else:
        print(f"INFO: O IP {ip} é seguro.")

print("--- Verificação concluída ---")
