Feito por Igo Quintino  
**Flet** em um ambiente virtual no Linux:  
**Obs:** necessariamente essa intalação e execusão pode funcionar no windows, com até menos coisas para configurar, vai do seu gosto.


---

### **Instalação e Execução do Flet em Ambiente Virtual no Linux**

Este tutorial descreve o processo de criação e configuração de um ambiente virtual para o desenvolvimento de um projeto que utiliza a biblioteca **Flet**. Siga os passos abaixo para garantir uma instalação correta e evitar erros comuns.  
**Obs:** o nome que adotei para o ambiente virtual foi Rental_Project, mas pode escolher qualquer outro se quiser.  

#### **1. Criando um Ambiente Virtual**

1. **Abra o terminal e navegue até o diretório do projeto.**

2. **Crie o ambiente virtual utilizando o comando a seguir:**
   ```bash
   python3 -m venv Rental_Project
   ```
   - **`Rental_Project`** é o nome do ambiente virtual. Você pode escolher qualquer nome para o ambiente.
   - O comando **`python3 -m venv`** cria a estrutura de diretórios necessária para o ambiente virtual.

#### **2. Ativando o Ambiente Virtual**

Para ativar o ambiente virtual, execute o seguinte comando no terminal, dentro da pasta do projeto:
```bash
source Rental_Project/bin/activate
```

- Ao ativar o ambiente, você verá o nome do ambiente virtual no prompt do terminal, indicando que ele está em uso.

#### **3. Desativando o Ambiente Virtual**

Para desativar o ambiente virtual, basta digitar o seguinte comando no terminal:
```bash
deactivate
```
- Isso irá desativar o ambiente virtual e retornar ao ambiente Python global.

#### **4. Configurando o VSCode para Usar o Ambiente Virtual**

Se você estiver utilizando o **Visual Studio Code (VSCodAqui está a versão formalizada do seu texto, adaptada para servir como uma documentação clara e profissional de instalação e execução doe)** e não tiver configurado o executável do Python corretamente, siga as etapas abaixo para garantir que o VSCode utilize o ambiente virtual criado:

1. **Abra o Command Palette do VSCode:**
   - Pressione **Ctrl+Shift+P** (Windows/Linux) ou **Cmd+Shift+P** (Mac).

2. **Selecione a opção `Python: Select Interpreter`.**

3. **Escolha o interpretador Python correspondente ao ambiente virtual criado, que será exibido como:**
   ```plaintext
   python3.12.3 ('Rental_Project': venv)
   ```
   - Essa opção garante que o VSCode utilize o Python do ambiente virtual em vez do Python global.

#### **5. Configurando a Extensão Code Runner para Utilizar o Ambiente Virtual**

Se você estiver utilizando a extensão **Code Runner** para executar scripts Python, é necessário configurar a extensão para que ela use o ambiente virtual diretamente. Siga os passos abaixo:

1. **Abra as configurações do VSCode:**
   - Vá até **File > Preferences > Settings** ou pressione **Ctrl+,**.

2. **Pesquise por "Code Runner: Run In Terminal".**
   - Marque a caixa de seleção dessa opção. Isso fará com que o Code Runner execute os scripts diretamente no terminal, respeitando o ambiente virtual.

#### **6. Instalando o pip (se necessário)**

O **pip** é o gerenciador de pacotes do Python e, normalmente, já é instalado quando você cria um ambiente virtual. Caso não esteja instalado, você pode instalá-lo manualmente dentro do ambiente virtual com o seguinte comando:
```bash
python -m ensurepip --upgrade
```

#### **7. Instalando a Biblioteca Flet**

Para instalar a biblioteca **Flet** no ambiente virtual, utilize o comando `pip` da seguinte forma:
```bash
pip install flet
```
- Certifique-se de estar no terminal com o ambiente virtual ativado, pois isso garantirá que a biblioteca seja instalada no ambiente correto.

#### **8. Instalando Dependências no Ubuntu/Linux**

Caso ocorra algum erro relacionado a bibliotecas ausentes, especialmente ao usar o **Ubuntu** ou outras distribuições Linux, pode ser necessário instalar algumas dependências adicionais. Execute os seguintes comandos no terminal:

1. **Atualize o sistema:**
   ```bash
   sudo apt update
   ```

2. **Instale as dependências do MPV:**
   ```bash
   sudo apt install libmpv-dev libmpv2
   ```

3. **Crie um link simbólico para a biblioteca `libmpv.so.1`:**
   ```bash
   sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
   ```
   - Essa etapa pode ser feita globalmente, ou seja, fora do ambiente virtual, para evitar erros futuros relacionados a essas dependências.

#### **Conclusão**

Seguindo os passos descritos, você estará configurado para usar o **Flet** dentro de um ambiente virtual no **Linux**, garantindo que as bibliotecas e dependências necessárias estejam corretamente instaladas. Caso enfrente algum erro, revisite as etapas de instalação das dependências ou as configurações do VSCode.

lembrando que o exemplo.py é uma base para executar e por fim aparecer a caixa de executavel que estar utilizando o flet.
---
