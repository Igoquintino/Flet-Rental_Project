## Aluguel de carrinhos de brinquedo para crianças:

1. Descrição do Projeto

O sistema gerenciará o aluguel de carrinhos de brinquedo, permitindo:
	•	Cadastro de carrinhos disponíveis para locação;
	•	Gerenciamento de clientes (pais ou responsáveis);
	•	Controle de aluguéis (datas de início e término, status dos carrinhos);
	•	Relatórios de uso e disponibilidade.

2. Funcionalidades Principais

2.1. Cadastro e Gerenciamento de Carrinhos

	•	Informações do carrinho:
	•	Nome ou modelo do carrinho;
	•	Categoria (ex.: elétrico, manual);
	•	Estado (disponível, alugado, manutenção);
	•	Data de aquisição e preço do aluguel.
	•	Atualizações:
	•	Alterar status do carrinho (ex.: manutenção, alugado);
	•	Remoção de carrinhos inativos.

2.2. Gerenciamento de Clientes

	•	Cadastro de pais ou responsáveis:
	•	Nome, e-mail, telefone, e endereço.
	•	Documentação (opcional, como CPF).
	•	Histórico de aluguéis por cliente.

2.3. Aluguéis

	•	Registro de aluguel:
	•	Carrinho alugado, cliente associado, data de início e fim.
	•	Status (ativo, finalizado).
	•	Regras:
	•	Não permitir alugar carrinhos já ocupados.
	•	Cobrar multas por devolução atrasada (opcional).

2.4. Relatórios e Consultas

	•	Listar carrinhos disponíveis e em uso.
	•	Histórico de aluguéis por carrinho e cliente.
	•	Relatório de uso geral (ex.: carrinhos mais alugados, duração média dos aluguéis).

3. Tecnologias Sugeridas

Backend

	•	Linguagem: Python (usando Flask ou Django).
	•	Banco de Dados: SQLite para simplicidade inicial, ou PostgreSQL para maior escalabilidade.

Frontend (Opcional)

	•	Framework: HTML, CSS, JavaScript (ou um framework como React para maior interatividade).

Extras

	•	Autenticação (para controle administrativo).
	•	Deploy: Usar Heroku, Render, ou AWS para hospedagem.

4. Estrutura de Banco de Dados

Tabela de Carrinhos

	•	id: Identificador único.
	•	nome: Nome ou modelo.
	•	categoria: Categoria do carrinho.
	•	estado: Disponível, alugado, manutenção.
	•	data_aquisicao: Data em que foi adquirido.
	•	preco_aluguel: Preço por aluguel.

Tabela de Clientes

	•	id: Identificador único.
	•	nome: Nome do responsável.
	•	email: E-mail de contato.
	•	telefone: Telefone de contato.
	•	endereco: Endereço.

Tabela de Aluguéis

	•	id: Identificador único.
	•	carrinho_id: ID do carrinho alugado (FK).
	•	cliente_id: ID do cliente (FK).
	•	data_inicio: Data de início do aluguel.
	•	data_fim: Data de término planejado.
	•	status: Ativo ou finalizado.

5. Rotas Backend

Clientes

	•	POST /api/clientes: Cadastrar cliente.
	•	GET /api/clientes: Listar clientes.
	•	GET /api/clientes/<id>: Obter dados de um cliente específico.

Carrinhos

	•	POST /api/carrinhos: Cadastrar carrinho.
	•	GET /api/carrinhos: Listar carrinhos (com filtros: disponíveis, em manutenção, etc.).
	•	PATCH /api/carrinhos/<id>: Atualizar status do carrinho.

Aluguéis

	•	POST /api/alugueis: Registrar um aluguel.
	•	GET /api/alugueis: Listar aluguéis (ativos e finalizados).
	•	PATCH /api/alugueis/<id>: Finalizar um aluguel.

6. Fluxo Inicial

	1.	Cadastro de carrinhos: Registre os carrinhos disponíveis para aluguel.
	2.	Cadastro de clientes: Registre os pais ou responsáveis.
	3.	Registro de aluguel: Escolha um carrinho e associe a um cliente.
	4.	Finalização de aluguel: Atualize o status do carrinho e registre a devolução.


    