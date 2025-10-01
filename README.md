#  Sistema com Docker e Reverse Proxy

Este projeto é a solução para o **Desafio DevOps do ITEP**, visando **containerizar duas aplicações web simples** e configurar um **Reverse Proxy (Nginx)** para gerenciar o tráfego entre elas.  

O objetivo foi cumprir todos os requisitos mínimos e implementar diferenciais focados em **boas práticas de Automação, Segurança e Portabilidade**.

---

## 📦 Como Executar o Projeto

**Pré-requisitos**:  
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  
- `make` (para automação com Makefile)

### Passos:

```bash
# 1. Clonar o repositório
git clone [SEU-REPOSITORIO]
cd [SEU-REPOSITORIO]

# 2. Subir os containers (build + run em modo detached)
make up

# 3. Ver logs dos containers
make logs 

# 4. Parar os containers
make down

## 🌐 URLs para Teste

Após a execução, acesse:

| Rota                  | Descrição                                | Status |
|-----------------------|------------------------------------------|--------|
| http://localhost/     | Página de Boas-Vindas (Nginx)            | OK     |
| http://localhost/app1 | Proxy Reverso → Container app1 (Flask)   | OK     |
| http://localhost/app2 | Proxy Reverso → Container app2 (Flask)   | OK     |

```

## Arquitetura da Solução

### Tecnologias

- **Orquestração**: Docker Compose (v3.8)
- **Aplicações Web**: Python 3.9 + Flask
- **Reverse Proxy**: Nginx (imagem `nginx:alpine`)
- **Automação**: Makefile

### Comunicação entre Containers

- **app1**: roda Flask na porta 5000
- **app2**: roda Flask na porta 5001
- **nginx**: expõe apenas a porta 80 e redireciona para `app1` e `app2` via Service Discovery do Docker

## Requisitos e Diferenciais

| Item                  | Implementação                          | Justificativa                                   |
|-----------------------|-----------------------------------------|------------------------------------------------|
| 3 Containers          | app1, app2, nginx                      | Microsserviços independentes                    |
| Porta 80 Exposta      | Apenas nginx expõe "80:80"             | Centralização do tráfego                        |
| Comunicação por Nome  | server app1:5000 / server app2:5001    | Portabilidade, sem IP fixo                      |
| Healthchecks          | Definidos nos 3 serviços               | Monitoramento de saúde                          |
| Restart Policies      | restart: always                        | Resiliência em falhas                           |
| Variáveis de Ambiente | Portas injetadas via environment       | Separação de código e configuração              |
| Segurança             | Usuário appuser não-root nos containers| Menos privilégios = mais seguro                 |
| Automação             | Makefile (up, down, logs, clean)       | Produtividade e consistência                    |

## Desafios encontrados e Aprendizados

###

### Roteamento de Proxy Reverso e o Erro 404 (Not Found)
- Dificuldade: O erro mais desafiador foi o Nginx retornar 404 Not Found ao acessar /app2. A princípio, acreditava-se ser um erro de comunicação ou porta, mas o teste com docker exec -it nginx_container curl revelou que o Nginx estava se comunicando perfeitamente, mas o Flask estava rejeitando a rota.

- O que o Erro Ensina: A depuração provou a regra de roteamento do Nginx: a sintaxe proxy_pass http://app2_server/ é crucial. O caractere / no final remove o prefixo /app2/ da requisição original, enviando apenas / para o Flask (que só responde à sua rota raiz), resolvendo a ambiguidade. Este é um detalhe que só se aprende na prática e na pesquisa de documentação.

### Erros de Inicialização e a Sintaxe do Nginx
- Dificuldade: Na primeira tentativa de execução, o Nginx falhou repetidamente ao carregar o nginx.conf devido a erros de sintaxe (como aspas simples incorretas em comandos return).
- O que o Erro Ensina: Demonstrou a importância da rigidez sintática de ferramentas de infraestrutura (como Nginx) em comparação com linguagens de programação. A depuração foi focada em logar a saída do Nginx e corrigir linha por linha.

## Dicas de Debug

- Ver logs: `make logs` ou `docker-compose logs -f`
- Testar internamente: `docker exec -it <container> sh` e usar `curl`
- Imagens limpas: manter comandos separados no Dockerfile para melhor cache

---

## Recursos Úteis

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Nginx](https://nginx.org/en/docs/)

## Melhorias Futuras

- Configurar SSL/TLS autoassinado no Nginx para habilitar HTTPS (porta 443)
- Criar manifestos Kubernetes (Kind) para rodar a mesma arquitetura em cluster
- Tornar o nginx.conf dinâmico com variáveis de ambiente via script de entrypoint

---

## Autor

### Rennan Carneiro
### Projeto desenvolvido como parte do Desafio DevOps - ITEP
