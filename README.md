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
   git clone <URL-do-repositorio>
   cd <diretorio-do-projeto>
   ```

2. Ative um ambiente virtual:
   ```bash
   python -m venv venv
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
   ```

5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Desenvolva a interface com o **Flet Framework**, consumindo as APIs criadas no backend.

---

## **Autor**

**[Igo Quintino]**

- 📧 Email: [igocastro.15@gmail.com]
- 🌐 Portfólio ou Website: [https://github.com/Igoquintino]
- 💼 LinkedIn: [Seu LinkedIn (opcional)]
---

Se você quiser adicionar links reais ou mais informações na seção de Autor, é só me avisar! 😊
