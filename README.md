# **Projeto: Aluguel de Carrinhos de Brinquedo**

Este projeto tem como objetivo gerenciar o aluguel de carrinhos de brinquedo para crianças, oferecendo funcionalidades como cadastro de carrinhos, gerenciamento de clientes e controle de aluguéis.

## **Tecnologias Utilizadas**

- **Backend:**
  - Framework: [Django](https://www.djangoproject.com/)
  - Extensão: [Django REST Framework (DRF)](https://www.django-rest-framework.org/) para a criação de APIs.

- **Frontend:**
  - Framework: [Flet](https://flet.dev/), utilizado para desenvolvimento da interface do usuário.

## **Funcionalidades**

- **Carrinhos:**
  - Cadastro e gerenciamento de carrinhos disponíveis para aluguel.
  - Controle de status: disponível, alugado, em manutenção.
  
- **Clientes:**
  - Cadastro de pais ou responsáveis.
  - Histórico de aluguéis por cliente.

- **Aluguéis:**
  - Registro de aluguéis com controle de datas de início e término.
  - Relatórios de carrinhos mais alugados e controle de devoluções.

---

## **Como Executar o Projeto**

1. Clone o repositório:
   ```bash
   git clone <URL-do-repositorio> #é so copiar a URL desse projeto aqui
   cd <diretorio-do-projeto>
   ```

2. Ative um ambiente virtual:
   ```bash
   python -m venv <nome-que-quiser>  
   python3 -m venv <nome-que-quiser> # Sem os sinais de <>, porque em algumas máquinas o primeiro comando pode não funcionar devido à versão do Python instalada.
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   python3 manage.py migrate # por conta da versão do python, use esse se preciso
   ```

5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   python3 manage.py createsuperuser # por conta da versão do python, use esse se preciso
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   python3 manage.py runserver # por conta da versão do python, use esse se preciso
   ```

7. Desenvolver a interface com o **Flet Framework**, consumindo as APIs criadas no backend.  
ainda precisar ser implementado
---

## **Autor**

**Igo Quintino**

- 📧 Email: igocastro.15@gmail.com
- 🌐 Portfólio ou Website: https://github.com/Igoquintino
