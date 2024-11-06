
# Aplicação Web de Investimentos

## Descrição do Projeto
Este projeto é uma aplicação web voltada para investimentos, desenvolvida para conectar investidores e empresários em uma plataforma de oportunidades financeiras. Investidores podem visualizar propostas de empresas e decidir onde aplicar seu capital, enquanto empresários podem cadastrar suas empresas e propostas de investimento. A aplicação está estruturada em quatro módulos principais para garantir uma organização clara e funcionalidade específica para cada tipo de usuário.

## Status do Projeto
**Concluído** ✅

## Tecnologias Utilizadas
- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Banco de Dados**: SQL

## Funcionalidades Principais
- **Autenticação**: Cadastro e login de usuários
- **Perfil do Investidor**: Acesso a oportunidades de investimento
- **Perfil do Empresário**: Cadastro de empresas e gerenciamento de propostas de investimento
- **Redirecionamento e Validação**: Utilização de mensagens de erro constantes e redirecionamento de rotas para uma navegação mais intuitiva e segura

## Estrutura dos Módulos (Apps)

1. **Core**:  
   É o núcleo da aplicação, onde estão as funcionalidades e configurações principais compartilhadas entre os módulos.

2. **Usuários**:  
   Responsável pelo cadastro, login e gerenciamento de informações dos usuários. Esse módulo garante autenticação e segurança para investidores e empresários.

3. **Empresários**:  
   Permite que empresários cadastrem suas empresas, criem e gerenciem propostas de investimento, proporcionando um espaço para atrair capital.

4. **Investidores**:  
   Este módulo é dedicado aos investidores, que podem navegar nas empresas cadastradas e investir naquelas que desejarem. 

## Boas Práticas Adotadas
- **Organização do Código**: Aplicação estruturada em módulos independentes para cada funcionalidade, o que facilita a manutenção e escalabilidade.
- **Mensagens de Erro e Validação**: Utilização de constantes para mensagens de erro, proporcionando consistência e facilidade na manutenção.
- **Redirecionamento de Rotas**: Configuração de rotas para direcionar os usuários de acordo com suas permissões e status na aplicação, melhorando a experiência de navegação.

## Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
2. Entre no diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Realize as migrações para o banco de dados:
   ```bash
   python manage.py migrate
   ```
6. Execute o servidor:
   ```bash
   python manage.py runserver
   ```

## Contribuições
Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, crie uma _issue_ ou envie um _pull request_.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido com ❤️ por Henrique Ribeiro
```

Esse `README.md` descreve as principais informações sobre o projeto, organização dos módulos, e como executá-lo, além de incluir instruções sobre contribuições e licença.
