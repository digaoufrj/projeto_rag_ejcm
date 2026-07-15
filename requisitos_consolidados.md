# Documento de Consolidação de Requisitos — Sistema de Gestão Integrada Empresa Júnior

Este documento apresenta a especificação consolidada de Requisitos Funcionais (RF) e Requisitos Não Funcionais (RNF) para o sistema de gestão da **Empresa Júnior (Empresa Júnior de Consultoria em Microinformática)**. 

A consolidação unifica as visões de múltiplos stakeholders (Gerente de Projetos, Assessoria de Vendas, Desenvolvedora Front-end, Assessoria de Gestão de Pessoas e Líderes Técnicos) e alinha as funcionalidades às normas institucionais contidas no **Código de Ética** e no **Estatuto** da organização (Base de Conhecimento).

---

## 1. Requisitos Funcionais (RF)

### 1.1. Módulo de Gestão Comercial (CRM)
*   **RF01 - Gestão de Leads e Contatos:** O sistema deve permitir o cadastro, edição, exclusão lógica e visualização de contatos e leads para prospecção, contendo nome, empresa, cargo, e-mail, telefone, origem do lead e histórico completo de interações.
*   **RF02 - Pipeline de Vendas Visual (Kanban):** O sistema deve fornecer um quadro visual estilo Kanban para o acompanhamento do funil de vendas, permitindo mover os leads entre as etapas de: *Prospecção, Primeiro Contato, Diagnóstico, Proposta, Negociação, Fechado (Ganho)* e *Perdido*.
*   **RF03 - Registro e Centralização de Interações:** O sistema deve permitir o registro detalhado de todas as interações realizadas com o lead (reuniões, e-mails, ligações e mensagens), vinculando-as diretamente ao perfil do cliente.
*   **RF04 - Repositório de Propostas Comerciais e Contratos:** O sistema deve permitir o upload, armazenamento, organização e controle de versionamento de propostas comerciais e contratos em formato digital vinculados ao respectivo cliente, permitindo a recuperação de versões anteriores.
*   **RF05 - Transição Automática de Vendas para Projetos:** Ao marcar um lead como "Fechado (Ganho)", o sistema deve converter automaticamente as informações comerciais em um novo projeto no módulo de gerenciamento de projetos, preservando todo o histórico coletado e os documentos anexados.
*   **RF06 - Automação de Follow-up:** O sistema deve permitir a configuração de réguas de automação para disparar e-mails de acompanhamento (follow-up) ou criar tarefas automáticas para os assessores quando um lead permanecer inativo por um período pré-determinado em uma etapa do funil.
*   **RF07 - Dashboard de Desempenho Comercial:** O sistema deve gerar relatórios visuais e gráficos com indicadores de desempenho (KPIs), incluindo taxa de conversão do funil, tempo médio de fechamento, volume de novos leads e progresso em relação às metas anuais da Empresa Júnior.

### 1.2. Módulo de Gestão de Projetos e Engenharia
*   **RF08 - Dashboard Unificado de Projetos:** O sistema deve fornecer uma visão consolidada de cada projeto ativo, exibindo em uma única tela o status atual, o progresso da sprint, os membros alocados, os documentos recentes e os próximos marcos (*milestones*).
*   **RF09 - Gestão de Sprints e Backlog:** O sistema deve permitir a criação, planejamento e gerenciamento de sprints, incluindo a criação de um backlog de produto, estimativa de esforço, priorização de demandas e acompanhamento visual do progresso por meio de um quadro Kanban.
*   **RF10 - Mapeamento do Ciclo de Vida do Projeto (Fases da Empresa Júnior):** O sistema deve permitir categorizar e acompanhar o progresso das tarefas e do projeto de acordo com as etapas padrão de entrega da Empresa Júnior: *Pesquisa, Prototipação, Desenvolvimento* e *Entrega e Suporte*.
*   **RF11 - Distribuição de Tarefas e Alocação de Squads:** O sistema deve permitir a criação de tarefas (com prazos, prioridades e checklists), atribuição de responsáveis e alocação de membros da Empresa Júnior a squads específicos de projetos, definindo seus papéis (Ex: Desenvolvedor, Designer, Líder Técnico).
*   **RF12 - Registro de Tempo de Execução (Timesheet Integrado):** O sistema deve possuir uma funcionalidade integrada para registrar o tempo gasto pelos membros do squad em cada tarefa (com início/fim ou inserção manual), permitindo a extração de relatórios de produtividade e o registro do histórico de esforço por tecnologia e complexidade.
*   **RF13 - Módulo de Estimativa Baseado em Histórico:** O sistema deve fornecer uma ferramenta de busca e filtragem que permita ao Líder Técnico consultar tarefas semelhantes de projetos anteriores e seus respectivos tempos de execução para apoiar a estimativa de novos cronogramas.
*   **RF14 - Cadastro, Versionamento e Rastreabilidade de Requisitos:** O sistema deve permitir o levantamento, especificação e versionamento dos requisitos do projeto (funcionais e não funcionais), mantendo o histórico de alterações com justificativa e permitindo associá-los diretamente a tarefas do backlog, protótipos e entregáveis.
*   **RF15 - Controle de Linha de Base (Baseline) do Cronograma:** O sistema deve permitir salvar a versão inicial do cronograma (*baseline*) e registrar desvios de prazos ao longo do ciclo de vida do projeto, exibindo alertas visuais em caso de atrasos.
*   **RF16 - Centralização de Artefatos Técnicos e Integrações:** O sistema deve permitir vincular repositórios de código externos (GitHub, GitLab) e links de design/UX (Figma) diretamente ao painel do projeto correspondente.
*   **RF17 - Registro de Lições Aprendidas (Post-Mortem):** O sistema deve disponibilizar um formulário de fechamento de projeto para o registro de lições aprendidas, riscos mitigados, erros técnicos e soluções adotadas pela equipe.
*   **RF18 - Dashboard de Métricas de Produtividade Técnica:** O sistema deve gerar relatórios e gráficos com indicadores de desempenho técnico, como tempo médio de desenvolvimento por tipo de funcionalidade, taxa de retrabalho e desvio de estimativas.

### 1.3. Módulo de Gestão de Pessoas (GP) e Conformidade Ética
*   **RF19 - Cadastro Unificado de Membros, Trainees e Alumni:** O sistema deve permitir o cadastro, edição, consulta e exclusão de dados pessoais e administrativos de integrantes e ex-integrantes (incluindo RG, CPF, endereço, idade, cargo, assessoria correspondente, foto, histórico de alocação e status: ativo, inativo, trainee ou alumni).
*   **RF20 - Acompanhamento do Programa de Trainees:** O sistema deve disponibilizar um módulo específico para monitorar o progresso do treinamento técnico dos trainees, permitindo registrar tarefas realizadas, notas obtidas, feedbacks recebidos e avaliações de evolução.
*   **RF21 - Controle de Frequência e Penalidades Éticas (Alinhamento Normativo):** 
    *   O sistema deve permitir o registro de presença dos membros em **Reuniões Gerais (RG)** e **Assembleias Gerais (AG)**.
    *   O sistema deve disparar um alerta automático para a Diretoria de Gestão de Pessoas quando um membro acumular **3 (três) ausências recorrentes sem justificativa válida em RGs**, ou **1 (uma) ausência sem justificativa válida em Assembleia Geral**, para que seja iniciado o processo de desligamento do membro, conforme o *Código de Ética (Pág. 2)*.
*   **RF22 - Registro de Avaliações, Feedbacks e Pesquisas de Clima:** O sistema deve permitir o agendamento, preenchimento e armazenamento de avaliações de desempenho periódicas, feedbacks formais e aplicação de pesquisas de clima organizacional/satisfação interna de forma anônima ou identificada.
*   **RF23 - Geração Automatizada de Documentos de GP:** O sistema deve gerar automaticamente contratos de voluntariado, termos de confidencialidade (NDA) e certificados em formato PDF a partir de modelos pré-definidos, preenchendo-os com os dados cadastrais do membro.
*   **RF24 - Exclusão Definitiva de Dados Sensíveis (Conformidade LGPD):** O sistema deve disponibilizar uma funcionalidade de exclusão permanente e irrecuperável de dados pessoais sensíveis de ex-membros mediante solicitação, mantendo apenas dados históricos anonimizados para fins estatísticos e de histórico institucional.
*   **RF25 - Painel de Indicadores de GP:** O sistema deve disponibilizar um painel visual com métricas consolidadas sobre clima organizacional, taxa de engajamento, turnover, absenteísmo em reuniões e pendências de feedbacks.

### 1.4. Módulo de Gestão de Documentos, Conhecimento e Reuniões
*   **RF26 - Editor de Documentos e Wiki Integrada:** O sistema deve fornecer um editor de texto estruturado (suportando formatação em Markdown) para criação, edição e organização de documentos técnicos (arquitetura, guias de setup, diagramas) e administrativos associados a cada projeto ou assessoria.
*   **RF27 - Repositório Multiformato e Modelos (Templates):** O sistema deve permitir o upload de arquivos (PDF, imagens) e a integração de links do Google Drive, além de permitir que Líderes e Diretores criem e disponibilizem modelos (*templates*) de documentos (ex: especificação de arquitetura, atas, propostas).
*   **RF28 - Controle de Versão de Documentos:** O sistema deve manter um histórico de revisões para todas as documentações criadas na plataforma, registrando a data, hora, justificativa e o membro responsável por cada alteração.
*   **RF29 - Espaço Colaborativo de Comentários:** O sistema deve permitir que os membros da equipe insiram comentários, feedbacks e notas de revisão diretamente nos documentos hospedados na plataforma.
*   **RF30 - Registro de Reuniões e Atas:** O sistema deve disponibilizar um módulo para agendamento de reuniões e preenchimento de atas (atas de reunião de diagnóstico, negociação ou técnicas), associando-as diretamente ao projeto ou lead correspondente.
*   **RF31 - Registro de Decisões do Cliente (Rastreabilidade):** O sistema deve possuir um log específico para registrar decisões estratégicas e aprovações formais realizadas junto ao cliente, garantindo um histórico imutável para futuras consultas.
*   **RF32 - Busca Global Indexada:** O sistema deve fornecer uma barra de pesquisa global que permita localizar rapidamente tarefas, atas de reuniões, decisões homologadas, termos específicos dentro de documentos técnicos e propostas comerciais por meio de palavras-chave, tags, status ou filtros de data.

### 1.5. Administração do Sistema e Segurança
*   **RF33 - Controle de Acesso Baseado em Perfis (RBAC):** O sistema deve restringir a visualização, criação, edição e exclusão de dados de acordo com o perfil do usuário (Ex: Administrador, Diretoria, Assessora de GP, Líder Técnico, Membro, Trainee, Cliente). Clientes devem visualizar apenas informações autorizadas de seus próprios projetos.
*   **RF34 - Autenticação Unificada (Single Sign-On - SSO):** O sistema deve permitir o acesso de todos os usuários por meio de integração com a conta institucional do Google Workspace da Empresa Júnior.
*   **RF35 - Registro de Auditoria (Logs do Sistema):** O sistema deve registrar um histórico de auditoria imutável contendo as ações de criação, alteração e exclusão de dados sensíveis (requisitos aprovados, baselines, dados de clientes, propostas, contratos e cadastros de membros), identificando o usuário, data/hora e o impacto da ação.

---

## 2. Requisitos Não Funcionais (RNF)

### 2.1. Segurança e Conformidade
*   **RNF01 - Segurança e Proteção de Dados (LGPD):** O sistema deve garantir a conformidade com a Lei Geral de Proteção de Dados (LGPD), criptografando dados pessoais sensíveis (como CPF, RG e dados de saúde) e comerciais tanto em repouso quanto em trânsito (utilizando protocolo HTTPS/TLS).
*   **RNF02 - Autenticação Multifator (MFA):** O sistema deve exigir autenticação multifator (MFA) para usuários com perfis administrativos (como a Assessoria de GP e Administradores) que possuem acesso a dados confidenciais.
*   **RNF03 - Auditabilidade de Escopo:** Qualquer alteração em requisitos de projetos previamente aprovados deve gerar um log de auditoria imutável contendo data, hora, usuário responsável e o impacto estimado no projeto.

### 2.2. Desempenho e Escalabilidade
*   **RNF04 - Desempenho de Busca:** O mecanismo de busca global por documentos, propostas históricas, tarefas e estimativas deve retornar resultados relevantes em um tempo máximo de **2 segundos**, mesmo sob alto volume de dados acumulados.
*   **RNF05 - Escalabilidade da Arquitetura:** A arquitetura do sistema e o banco de dados devem ser dimensionados para suportar o crescimento contínuo do volume de registros históricos (leads, atas, propostas, projetos, membros e respostas de pesquisas) ao longo das gestões sem degradação do desempenho geral.

### 2.3. Usabilidade e Interface
*   **RNF06 - Compatibilidade Multiplataforma e Responsividade:** O sistema deve ser uma aplicação web responsiva, compatível com os principais navegadores do mercado (Chrome, Firefox, Safari, Edge) e otimizada prioritariamente para computadores pessoais (desktops e notebooks), focando em alta densidade de informação para tarefas administrativas.
*   **RNF07 - Facilidade de Adoção e Baixa Fricção:** 
    *   O processo para criar, editar ou salvar um documento técnico não deve exigir mais do que **3 cliques**.
    *   A interface do editor de documentos deve suportar atalhos de teclado semelhantes a ferramentas de mercado (como Notion e Google Docs).
    *   O sistema deve possuir uma interface intuitiva que permita que novos membros realizem operações básicas de cadastro e consulta com um treinamento de, no máximo, **20 minutos**.

### 2.4. Disponibilidade e Confiabilidade
*   **RNF08 - Alta Disponibilidade (Uptime):** O sistema deve apresentar uma taxa de disponibilidade mínima de **99,5%** de tempo de atividade (*uptime*), calculada mensalmente, garantindo o acesso contínuo aos membros.
*   **RNF09 - Confiabilidade e Salvamento Automático:** O sistema deve possuir um mecanismo de salvamento automático em tempo real para a edição de documentos, atas de reuniões e descrições de tarefas, evitando a perda de dados por falhas de conexão ou fechamento acidental do navegador.
*   **RNF10 - Backup e Recuperação de Desastres:** O sistema deve realizar rotinas de backup diárias e automáticas de toda a base de dados e arquivos armazenados, com tempo máximo de recuperação (RTO) de até **4 horas** em caso de falhas críticas.
*   **RNF11 - Consistência e Sincronização de Dados:** O sistema deve operar com uma base de dados centralizada e garantir a sincronização em tempo real das atualizações de cadastros e status de projetos, aplicando validações sintáticas rígidas (ex: formato de CPF, e-mail e datas) para evitar duplicidades e inconsistências.

### 2.5. Interoperabilidade e Integrações
*   **RNF12 - Interoperabilidade de Dados (Importação/Exportação):** O sistema deve permitir a exportação de relatórios, cronogramas, backlogs e dados cadastrais em formatos estruturados e legíveis por outras ferramentas de mercado (como CSV, PDF e XLSX), bem como a importação de dados de planilhas e formulários externos de forma automatizada.