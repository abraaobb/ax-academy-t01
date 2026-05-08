# ax-academy-t01
Este é um trabalho em conjunto com os alunos do AX Academy - Turma Matutina

#### **1. "O Engajador Automático" (YouTube)**

O script abre o navegador, pesquisa por uma palavra-chave, clica no primeiro vídeo, espera 30 segundos (para contar a view) e clica no botão de **Like**.
• **Ação:** `Abrir URL` → `Digitar na busca` → `Click(Vídeo)` → `Wait(30s)` → `Click(Like)`.

#### **2. "Limpador de Inbox" (Gmail)**

Uma automação que seleciona todos os e-mails de promoções ou redes sociais que têm mais de 30 dias e clica no botão **Excluir**.
• **Ação:** `Filtrar busca` → `Selecionar todos` → `Click(Lixeira)`.

#### **3. "Auto-Apply" (LinkedIn)**

O robô percorre a lista de vagas de "Candidatura Simplificada", clica em cada uma e preenche o formulário básico com seus dados salvos.
• **Ação:** `Scroll down` → `Click(Easy Apply)` → `Preencher Form` → `Click(Enviar)`.

#### **4. "Minerador de Preços" (Amazon/Mercado Livre)**

O script entra na página de um produto que você quer muito, copia o preço e cola em uma planilha. Se o preço estiver abaixo de um valor $X$, ele te envia um alerta.
• **Ação:** `Abrir Produto` → `Ler Texto(Preço)` → `Se Preço < X` → `Enviar Notificação`.

#### **5. "Postador Multi-Redes" (Facebook/Twitter)**

Você escreve o texto uma vez em um arquivo local, e o robô abre o Facebook, cola e posta; depois abre o Twitter, cola e posta.
• **Ação:** `Abrir Site` → `Focar campo de texto` → `Colar` → `Click(Publicar)`.

#### **6. "Coletor de Notas Fiscais" (Site da Prefeitura/Sefaz)**

O robô faz login no portal da prefeitura, navega até a lista de notas do mês e clica no botão de **Download/Imprimir PDF** de cada uma delas.
• **Ação:** `Login` → `Navegar até Consultas` → `Loop(Click Download)`.

#### **7. "Atualizador de Dashboard" (Sites de Notícias)**

O navegador abre 5 abas de sites diferentes (ex: G1, CNN, Valor) e tira um **Print Screen** da manchete principal de cada um, salvando as imagens em uma pasta.
• **Ação:** `Abrir URL` → `Screenshot Elemento` → `Salvar Arquivo`.

#### **8. "Seguir Seguidores" (Instagram/Twitter)**

O script entra no perfil de um concorrente ou referência, clica na lista de seguidores e vai clicando em "Seguir" nos primeiros 20 perfis.
• **Ação:** `Abrir Seguidores` → `Loop(Click Seguir)` → `Sleep(Intervalo aleatório)`.

#### **9. "Gerador de Relatórios de Anúncios" (Meta Ads/Google Ads)**

O robô entra no gerenciador de anúncios, define a data para "Ontem", clica em "Exportar CSV" e move o arquivo para a sua pasta de relatórios.
• **Ação:** `Login` → `Selecionar Data` → `Click(Exportar)`.

#### **10. "Auto-Login de Manhã"**

Um script simples que, assim que você liga o PC, abre o navegador com todas as abas que você usa (E-mail, CRM, WhatsApp Web, Calendário) e já faz o login nelas.
• **Ação:** `Abrir Browser` → `Múltiplas URLs` → `Preencher Credenciais`.