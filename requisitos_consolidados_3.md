# Documento de Consolidação de Requisitos — Sistema Integrado de Gestão EJCM

Este documento apresenta a especificação consolidada de Requisitos Funcionais (RF) e Requisitos Não Funcionais (RNF) para o Sistema Integrado de Gestão da **EJCM (Empresa Júnior de Consultoria em Microinformática)**. 

A consolidação unifica as visões de múltiplos stakeholders (Gerente de Projetos, Assessora de Vendas, Desenvolvedora Front-End, Líderes Técnicos e Assessoras de Gestão de Pessoas), reconciliando redundâncias e alinhando as funcionalidades às normas do **Código de Ética** e do **Estatuto da EJCM**.

---

## 1. Requisitos Funcionais (RF)

### 1.1. Módulo de Gestão Comercial (CRM)
*   **RF01 - Gestão de Leads e Contatos:** O sistema deve permitir o cadastro, edição, visualização e exclusão de leads e contatos de prospecção, armazenando nome, empresa, cargo, e-mail, telefone, origem do lead e histórico completo de interações.
*   **RF02 - Pipeline de Vendas Visual (Kanban):** O sistema deve fornecer um quadro Kanban para o acompanhamento do funil de vendas, permitindo mover os leads entre as etapas de: *Prospecção, Primeiro Contato, Diagnóstico, Proposta, Negociação, Fechado (Ganho)* e *Perdido*.
*   **RF03 - Automação de Follow-up:** O sistema deve permitir a configuração de réguas de automação para disparar e-mails de acompanhamento ou gerar tarefas automáticas para os assessores quando um lead permanecer inativo por um período pré-determinado em uma etapa do funil.
*   **RF04 - Transição Automática para Projetos:** Ao marcar um lead como "Fechado (Ganho)", o sistema deve converter automaticamente as informações comerciais em um novo projeto no módulo de gerenciamento de projetos, preservando o histórico de interações, propostas e contratos.
*   **RF05 - Dashboard de Desempenho Comercial:** O sistema deve gerar relatórios visuais com indicadores (KPIs) de vendas, incluindo taxa de conversão do funil, tempo médio de fechamento, volume de novos leads e progresso em relação às metas anuais da EJCM.

### 1.2. Módulo de Gestão de Projetos e Sprints
*   **RF06 - Dashboard Unificado de Projetos:** O sistema deve fornecer uma visão consolidada de cada projeto ativo, exibindo em uma única tela o status atual, o progresso da sprint, os membros alocados (squad), documentos recentes e os próximos marcos (*milestones*).
*   **RF07 - Gestão de Sprints e Backlog:** O sistema deve permitir a criação, planejamento e gerenciamento de sprints, incluindo a manutenção de um backlog de produto, estimativa de esforço, priorização de demandas e acompanhamento visual via quadro Kanban.
*   **RF08 - Distribuição de Tarefas e Alocação de Squads:** O sistema deve permitir a criação de tarefas com atribuição de responsáveis, prazos, níveis de prioridade e checklists. Deve permitir também a alocação de membros da EJCM a squads específicos, definindo seus papéis (Ex: Desenvolvedor, Designer, Líder Técnico).
*   **RF09 - Registro de Tempo de Execução (Timesheet):** O sistema deve possuir uma funcionalidade integrada para registrar o tempo gasto pelos membros em cada tarefa, permitindo a extração de relatórios de produtividade e o registro do tempo real de execução associado à tecnologia e complexidade da tarefa.
*   **RF10 - Mapeamento do Ciclo de Vida do Projeto:** O sistema deve categorizar e acompanhar o progresso dos projetos de acordo com as etapas padrão da EJCM: *Pesquisa, Prototipação, Desenvolvimento, Entrega* e *Suporte*.
*   **RF11 - Controle de Linha de Base (Baseline) do Cronograma:** O sistema deve permitir salvar a versão inicial do cronograma (baseline) e registrar desvios de prazos ao longo do ciclo de vida do projeto, exibindo alertas visuais em caso de atrasos.

### 1.3. Módulo de Gestão Técnica, Requisitos e Conhecimento
*   **RF12 - Centralização de Repositórios e Artefatos Técnicos:** O sistema deve permitir vincular repositórios de código externos (GitHub, GitLab) e links de design (Figma) diretamente ao painel do projeto correspondente.
*   **RF13 - Editor de Documentação Técnica (Wiki):** O sistema deve fornecer um editor de texto estruturado (estilo Wiki) com suporte a Markdown para a criação, edição e organização de guias de arquitetura, setups e diagramas.
*   **RF14 - Cadastro, Versionamento e Rastreabilidade de Requisitos:** O sistema deve permitir o levantamento, especificação e versionamento dos requisitos do projeto (funcionais e não funcionais). O sistema deve permitir associar requisitos diretamente a tarefas do backlog, protótipos e entregáveis.
*   **RF15 - Módulo de Estimativa Baseado em Histórico:** O sistema deve fornecer uma ferramenta de busca e filtragem que permita ao Líder Técnico consultar tarefas semelhantes de projetos anteriores e seus respectivos tempos de execução para apoiar a estimativa de novos cronogramas.
*   **RF16 - Registro de Lições Aprendidas (Post-Mortem):** O sistema deve disponibilizar um formulário de fechamento de projeto para o registro de lições aprendidas, riscos mitigados, erros técnicos e soluções adotadas pela equipe.
*   **RF17 - Repositório de Conhecimento Institucional (Arquivo Histórico):** O sistema deve fornecer uma funcionalidade para arquivar projetos finalizados, garantindo que suas documentações, requisitos e códigos permaneçam acessíveis para consulta futura.

### 1.4. Módulo de Gestão de Pessoas (GP) e Programa de Trainees
*   **RF18 - Cadastro Unificado de Integrantes (Membros, Trainees e Alumni):** O sistema deve permitir o cadastro e gestão de dados pessoais e administrativos de membros, trainees e ex-membros (incluindo RG, CPF, endereço, cargo, assessoria, foto, data de entrada e histórico na organização).
*   **RF19 - Acompanhamento do Programa de Trainees:** O sistema deve disponibilizar um módulo para monitorar o progresso do treinamento técnico dos trainees, permitindo registrar tarefas realizadas, notas obtidas e feedbacks recebidos.
*   **RF20 - Registro de Avaliações, Feedbacks e Histórico de Movimentação:** O sistema deve permitir o agendamento, preenchimento e armazenamento de avaliações de desempenho periódicas e feedbacks formais, além de registrar automaticamente o histórico cronológico de promoções, mudanças de cargo, trocas de assessoria e desligamentos.
*   **RF21 - Monitor de Presença e Sanções (Código de Ética):** O sistema deve permitir o registro de presença em Reuniões Gerais (RG) e Assembleias Gerais. 
    *   O sistema deve emitir um alerta automático à Diretoria de Gestão de Pessoas quando um membro acumular **3 ausências recorrentes sem justificativa válida em RGs**.
    *   O sistema deve emitir um alerta imediato de processo de desligamento caso um membro falte a **uma Assembleia Geral sem justificativa válida**, em conformidade com o Código de Ética da EJCM.
*   **RF22 - Gestão de Pesquisas de Clima e Satisfação:** O sistema deve permitir a criação, agendamento e coleta de respostas de pesquisas de opinião, clima organizacional e satisfação interna, suportando formatos anônimos ou identificados.
*   **RF23 - Painel de Indicadores de GP (Dashboard):** O sistema deve disponibilizar um painel visual com gráficos e métricas consolidadas sobre clima organizacional, taxa de engajamento, turnover, absenteísmo e pendências de feedbacks/avaliações.
*   **RF24 - Exclusão Definitiva de Dados Sensíveis (Direito ao Esquecimento):** Em conformidade com a LGPD, o sistema deve permitir a exclusão permanente de dados pessoais sensíveis de ex-membros mediante solicitação, mantendo apenas dados históricos anonimizados para fins estatísticos.

### 1.5. Módulo de Documentos, Atas e Colaboração
*   **RF25 - Registro de Reuniões e Atas:** O sistema deve disponibilizar um módulo para agendamento de reuniões e preenchimento de atas (atas de reunião de diagnóstico, negociação ou técnicas), associando-as diretamente ao lead ou projeto correspondente.
*   **RF26 - Repositório de Documentos e Versionamento:** O sistema deve permitir o upload, organização em pastas e download de propostas comerciais, contratos, termos de voluntariado e NDAs, com suporte a controle de versão e histórico de alterações.
*   **RF27 - Geração Automatizada de Documentos:** O sistema deve gerar automaticamente contratos de voluntariado, termos administrativos e NDAs em formato PDF a partir de modelos pré-definidos, preenchendo-os com os dados cadastrais do membro armazenados no sistema.
*   **RF28 - Espaço Colaborativo de Comentários:** O sistema deve permitir que os membros da equipe insiram comentários, feedbacks e notas de revisão diretamente nos documentos técnicos e atas hospedados na plataforma.
*   **RF29 - Busca Global Indexada Avançada:** O sistema deve fornecer uma barra de pesquisa global que permita localizar rapidamente tarefas, atas de reuniões, decisões homologadas, integrantes e termos específicos dentro do conteúdo de documentos técnicos e propostas comerciais.

### 1.6. Segurança, Controle de Acesso e Auditoria
*   **RF30 - Controle de Acesso Baseado em Perfis (RBAC):** O sistema deve restringir a visualização e edição de dados de acordo com perfis de acesso parametrizados (Ex: Administrador, Diretoria, Assessora de GP, Gerente de Projetos, Líder Técnico, Membro, Trainee e Cliente). Clientes devem visualizar apenas informações autorizadas de seus respectivos projetos.
*   **RF31 - Autenticação Unificada (SSO):** O sistema deve permitir o acesso de todos os usuários por meio de integração com a conta institucional do Google Workspace da EJCM.
*   **RF32 - Registro de Auditoria (Logs):** O sistema deve registrar um histórico de auditoria imutável contendo as ações de criação, leitura, alteração e exclusão (CRUD) de dados sensíveis (dados de membros, propostas, contratos, requisitos aprovados e baselines de cronogramas), identificando o usuário, data e hora da ação.

---

## 2. Requisitos Não Funcionais (RNF)

### 2.1. Segurança e Conformidade
*   **RNF01 - Conformidade com a LGPD:** O sistema deve garantir a proteção de dados pessoais e sensíveis em conformidade com a Lei Geral de Proteção de Dados (LGPD), aplicando criptografia em repouso (banco de dados) e em trânsito (protocolo HTTPS/TLS).
*   **RNF02 - Autenticação Multifator (MFA):** O sistema deve exigir autenticação multifator (MFA) para usuários com perfis administrativos (como Diretoria e Assessoria de GP) que possuem acesso a dados confidenciais e cadastros de membros.

### 2.2. Desempenho e Escalabilidade
*   **RNF03 - Desempenho de Busca e Carregamento:** O mecanismo de busca global e as consultas ao banco de dados histórico devem retornar resultados relevantes em um tempo máximo de **2 segundos**, mesmo sob condições normais de rede e com alto volume de dados acumulados.
*   **RNF04 - Escalabilidade da Arquitetura:** A arquitetura do sistema deve ser dimensionada para suportar o crescimento contínuo do volume de registros históricos (leads, atas, propostas, projetos, membros e respostas de pesquisas) sem degradação do desempenho geral do software.

### 2.3. Usabilidade e Interface
*   **RNF05 - Compatibilidade Multiplataforma e Responsividade:** O sistema deve ser uma aplicação web responsiva, compatível com os principais navegadores do mercado (Chrome, Firefox, Safari, Edge) e otimizada prioritariamente para uso em computadores desktop e notebooks, focando em alta densidade de informação.
*   **RNF06 - Facilidade de Adoção e Baixa Curva de Aprendizado:** O sistema deve possuir uma interface intuitiva que permita que novos membros realizem operações básicas de cadastro e consulta com no máximo **20 minutos** de treinamento, e que a operação completa do sistema seja dominada com um treinamento básico de no máximo **2 horas**.
*   **RNF07 - Fluxo Simplificado (Baixa Fricção):** O processo para criar, editar ou salvar um documento técnico ou ata não deve exigir mais do que **3 cliques**, minimizando etapas burocráticas no editor de documentos.

### 2.4. Confiabilidade e Disponibilidade
*   **RNF08 - Alta Disponibilidade (Uptime):** O sistema deve apresentar uma taxa de disponibilidade mínima de **99,5%** em regime de operação contínua (24/7).
*   **RNF09 - Salvamento Automático:** O sistema deve possuir um mecanismo de salvamento automático em tempo real para a edição de documentos, atas de reuniões, wikis e descrições de tarefas, evitando a perda de dados por falhas de conexão.
*   **RNF10 - Backup e Recuperação de Desastres (DR):** O sistema deve realizar rotinas de backup diárias e automáticas de toda a base de dados e arquivos armazenados. O tempo máximo de recuperação (RTO) em caso de falhas críticas deve ser de até **4 horas**.
*   **RNF11 - Consistência e Validação de Dados:** O sistema deve possuir mecanismos de validação sintática (ex: validação de formato de CPF, e-mail e datas) no recebimento de dados via integrações ou formulários para mitigar inconsistências na base de dados.

### 2.5. Interoperabilidade
*   **RNF12 - Facilidade de Importação e Exportação:** O sistema deve permitir a importação em lote de dados de membros e leads via arquivos estruturados (CSV ou XLSX) e a exportação de relatórios, cronogramas e backlogs em formatos legíveis e padronizados (PDF, CSV e XLSX).