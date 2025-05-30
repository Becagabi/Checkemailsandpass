# 🔐 Senha Checker - Verificador de Vazamentos de Email e Senha

Este é um script em Python para verificação de **comprometimento de credenciais** (e-mail e senha) com base na API do [Have I Been Pwned](https://haveibeenpwned.com/) e em serviços simulados como **CyberNews** e **F-Secure**.

> 🐳 O script está preparado para execução em um container Docker com o nome `senha-checker`.

---

## 🚀 Funcionalidades

- Verifica se um e-mail foi exposto em vazamentos públicos.
- Verifica se uma senha já foi comprometida.
- Simula consultas em serviços como Mozilla Monitor, CyberNews e F-Secure.
- Retorna os resultados no terminal com ícones de alerta.

---

## 🐳 Executando com Docker

### 1. Build da imagem Docker
ID docker: 3991f3f1d9de028dceb17769deedbb24a99a7f680611b16f824c9452f8d1407a

```bash
docker build -t senha-checker .
 
