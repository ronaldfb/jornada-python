##Como Funciona
**Este script Python automatiza o processo de cadastro de produtos em um sistema web específico, simulando as ações de um usuário real. A seguir, uma explicação detalhada de cada etapa:

**Inicialização:

Importação de bibliotecas: Carrega as bibliotecas pyautogui e pandas, essenciais para a interação com a interface gráfica e o tratamento de dados, respectivamente.
Configuração: Define o tempo de pausa entre cada ação, permitindo ajustar a velocidade da automação.
Acesso ao Sistema:

Abertura do navegador: Abre o navegador padrão do sistema e acessa a página de login da plataforma.
Preenchimento do formulário de login: Localiza os campos de e-mail e senha na página e preenche-os com as credenciais definidas no script.
Importação dos dados:

Leitura do arquivo CSV: Carrega os dados dos produtos a serem cadastrados a partir de um arquivo CSV. Cada linha do arquivo representa um produto.
Cadastro dos produtos:

Iteração sobre os dados: Percorre cada linha do DataFrame (estrutura de dados do pandas) que representa os dados do CSV.
Preenchimento do formulário: Para cada produto:
Localiza os campos do formulário de cadastro (código, marca, tipo, etc.) na tela.
Preenche cada campo com o valor correspondente da linha atual do DataFrame.
Simula o pressionamento da tecla Tab para passar para o próximo campo.
Envia o formulário para cadastrar o produto.
Gerenciamento da interface:

Rolagem da página: Após cada cadastro, realiza uma rolagem para cima na página, garantindo que o próximo formulário esteja visível.

Em resumo:

O script funciona como um robô virtual, realizando de forma repetitiva e precisa as tarefas de acessar um sistema, preencher formulários e enviar dados. Ele elimina a necessidade de interação manual do usuário, aumentando a eficiência e reduzindo o risco de erros.
