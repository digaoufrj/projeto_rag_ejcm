# Documento de Consolidação de Requisitos — Sistema de Gestão Integrada (EJCM)

Este documento apresenta a especificação consolidada de Requisitos Funcionais (RF) e Requisitos Não Funcionais (RNF) para o sistema de gestão integrada da **EJCM (Empresa Júnior de Consultoria em Microinformática)**. 

A consolidação unifica as visões de múltiplos stakeholders (Gerente de Projetos, Assessora de Vendas, Desenvolvedora Front-end, Assessora de Gestão de Pessoas e Líderes Técnicos), eliminando redundâncias, resolvendo conflitos de escopo e integrando as regras de negócio extraídas dos documentos institucionais da EJCM (Código de Ética e Estatuto).

---

## 1. Requisitos Funcionais (RF)

Os requisitos funcionais foram organizados em módulos lógicos para refletir a estrutura operacional da empresa júnior.

### Módulo 1: Plataforma, Segurança e Colaboração (Core)
*   **RF01 - Autenticação Unificada (Single Sign-On - SSO):** O sistema deve permitir o acesso de todos os usuários por meio de uma única credencial de login integrada à conta institucional do Google Workspace da EJCM.
*   **RF02 - Controle de Acesso Baseado em Perfis (RBAC):** O sistema deve restringir a visualização, criação, edição e exclusão de dados de acordo com o perfil do usuário (Ex: Administrador, Diretoria, Assessoria de GP, Assessoria de Vendas, Gerente de Projetos, Líder Técnico, Membro, Trainee e Cliente).
    *   *Regra de Negócio:* Clientes só podem visualizar informações autorizadas de seus próprios projetos. Dados sensíveis de membros (feedbacks, avaliações, dados pessoais) são restritos à GP e Diretoria.
*   **RF03 - Registro de Auditoria (Logs de Sistema):** O sistema deve registrar de forma imutável todas as ações de criação, leitura, alteração e exclusão (CRUD) realizadas sobre dados sensíveis (dados de membros, propostas comerciais, contratos e requisitos de projetos), identificando o usuário responsável, data e hora.
*   **RF04 - Busca Global Indexada:** O sistema deve fornecer uma barra de pesquisa global que permita localizar rapidamente leads, clientes, projetos, tarefas, atas de reuniões, decisões homologadas e termos específicos dentro do conteúdo de documentos técnicos anexados (PDF, Markdown ou notas estruturadas).
*   **RF05 - Registro de Atas de Reunião:** O sistema deve disponibilizar um módulo para criação, edição e armazenamento de atas de reuniões (diagnósticos, negociações, reuniões de squad ou institucionais), associando-as diretamente ao lead, projeto ou membro correspondente.
*   **RF06 - Central de Notificações e Lembretes:** O sistema deve enviar notificações internas e por e-mail sobre prazos de tarefas, reuniões agendadas, pendências de assinaturas de documentos, preenchimento de pesquisas de clima e alertas de inatividade de leads.

### Módulo 2: Gestão Comercial (CRM)
*   **RF07 - Gestão de Leads e Contatos:** O sistema deve permitir o cadastro, edição, exclusão e visualização de contatos e leads para prospecção, contendo nome, empresa, cargo, e-mail, telefone, origem do lead e histórico completo de interações.
*   **RF08 - Pipeline de Vendas Visual (Kanban):** O sistema deve fornecer um quadro visual para o acompanhamento do funil de vendas, permitindo mover os leads entre as etapas de: *Prospecção, Primeiro Contato, Diagnóstico, Proposta, Negociação, Fechado (Ganho)* e *Perdido*.
*   **RF09 - Registro de Interações:** O sistema deve permitir o registro detalhado de todas as interações realizadas com o lead (reuniões, e-mails, ligações e mensagens), vinculando-as diretamente ao perfil do cliente.
*   **RF10 - Repositório e Versionamento de Propostas e Contratos:** O sistema deve permitir o upload, armazenamento e organização de propostas comerciais e contratos em formato digital vinculados ao respectivo cliente, mantendo o histórico de versões e permitindo a recuperação de arquivos anteriores.
*   **RF11 - Automação de Follow-up:** O sistema deve permitir a configuração de réguas de automação para disparar e-mails de acompanhamento ou criar tarefas automáticas para os assessores quando um lead permanecer inativo por um período pré-determinado em uma etapa do funil.
*   **RF12 - Transição Automática de Vendas para Projetos:** Ao marcar um lead como "Fechado (Ganho)", o sistema deve converter automaticamente as informações comerciais em um novo projeto no módulo de gerenciamento de projetos, herdando o histórico de interações, atas de diagnóstico, propostas e contratos.

### Módulo 3: Gestão e Execução de Projetos
*   **RF13 - Dashboard Unificado de Projetos:** O sistema deve fornecer uma visão consolidada de cada projeto ativo, exibindo em uma única tela o status atual, o progresso da sprint, os membros alocados (squad), os documentos recentes e os próximos marcos (*milestones*).
*   **RF14 - Gestão de Sprints e Backlog:** O sistema deve permitir que o Gerente de Projetos e o Líder Técnico criem, planejem e gerenciem sprints, incluindo a criação de um backlog de produto, estimativa de esforço, priorização de demandas e acompanhamento visual por meio de um quadro Kanban.
*   **RF15 - Distribuição e Acompanhamento de Tarefas:** O sistema deve permitir a criação de tarefas, atribuição de responsáveis (membros do squad), definição de prazos, níveis de prioridade e checklist de subtarefas.
*   **RF16 - Registro de Tempo de Execução (Timesheet):** O sistema deve possuir uma funcionalidade integrada para registrar o tempo gasto pelos membros do squad em cada tarefa, permitindo a extração de relatórios de produtividade e o registro do tempo real de execução associado à tecnologia utilizada.
*   **RF17 - Alocação e Gestão de Squads:** O sistema deve permitir alocar membros da EJCM a squads específicos de projetos, definindo seus papéis (Ex: Desenvolvedor, Designer, Líder Técnico, Gerente de Projetos).
*   **RF18 - Registro de Decisões do Cliente (Rastreabilidade):** O sistema deve possuir um log específico para registrar decisões estratégicas, alterações de escopo e aprovações formais realizadas junto ao cliente, garantindo um histórico imutável para futuras consultas.
*   **RF19 - Mapeamento do Ciclo de Vida do Projeto (Fases da EJCM):** O sistema deve categorizar e acompanhar o progresso do projeto de acordo com as etapas de entrega da EJCM: *Pesquisa, Prototipação, Desenvolvimento, Entrega* e *Suporte*.

### Módulo 4: Engenharia de Software e Gestão do Conhecimento
*   **RF20 - Centralização de Repositórios e Artefatos Técnicos:** O sistema deve permitir vincular repositórios de código externos (GitHub/GitLab) e links de design (Figma) diretamente ao painel do projeto correspondente.
*   **RF21 - Editor de Documentação Técnica (Wiki/Markdown):** O sistema deve fornecer um editor de texto estruturado com suporte a Markdown para criação, edição e organização de documentos técnicos (arquitetura, guias de setup, diagramas) associados a cada projeto.
*   **RF22 - Padronização de Documentos (Templates):** O sistema deve permitir a criação e disponibilização de modelos (*templates*) de documentos (ex: especificação de arquitetura, atas de reuniões técnicas, guias de deploy, propostas comerciais) para uso padronizado pelas equipes.
*   **RF23 - Gestão, Versionamento e Rastreabilidade de Requisitos:** O sistema deve permitir o levantamento, especificação e versionamento dos requisitos do projeto (funcionais e não funcionais), permitindo associá-los a tarefas do backlog, protótipos e entregáveis, além de manter um histórico de alterações com justificativa.
*   **RF24 - Controle de Linha de Base (Baseline) do Cronograma:** O sistema deve permitir salvar a versão inicial do cronograma (baseline) e registrar desvios de prazos ao longo do ciclo de vida do projeto, exibindo alertas visuais em caso de atrasos.
*   **RF25 - Registro de Lições Aprendidas (Post-Mortem) e Arquivo Histórico:** O sistema deve disponibilizar um formulário de fechamento de projeto para o registro de lições aprendidas, riscos mitigados, erros técnicos e soluções adotadas. Projetos finalizados devem ser arquivados, mantendo sua documentação acessível para consultas futuras.
*   **RF26 - Módulo de Estimativa Baseado em Histórico:** O sistema deve fornecer uma ferramenta de busca e filtragem que permita ao Líder Técnico consultar tarefas semelhantes de projetos anteriores e seus respectivos tempos de execução reais para apoiar a estimativa de novos cronogramas.

### Módulo 5: Gestão de Pessoas (GP) e Conformidade Ética
*   **RF27 - Cadastro Unificado de Membros, Trainees e Alumni:** O sistema deve permitir o cadastro, edição, consulta e exclusão de dados pessoais e administrativos de integrantes e ex-integrantes (incluindo RG, CPF, endereço, idade, cargo, assessoria, foto, histórico de alocação e trajetória na organização).
*   **RF28 - Acompanhamento do Programa de Trainees:** O sistema deve disponibilizar um módulo para monitorar o progresso do treinamento técnico dos trainees, permitindo registrar tarefas realizadas, notas obtidas e feedbacks recebidos.
*   **RF29 - Registro de Avaliações, Feedbacks e Pesquisas de Clima:** O sistema deve permitir o agendamento, preenchimento e armazenamento de avaliações de desempenho periódicas, feedbacks formais e aplicação de pesquisas de clima organizacional (de forma anônima ou identificada).
*   **RF30 - Geração Automatizada de Documentos de GP:** O sistema deve gerar automaticamente contratos de voluntariado, termos de confidencialidade (NDA) e certificados em formato PDF a partir de modelos pré-definidos, preenchendo-os com os dados cadastrais do membro.
*   **RF31 - Integração de Formulários de Processo Seletivo:** O sistema deve possuir integração com ferramentas de formulários digitais externos para coletar, consolidar e atualizar dados cadastrais de novos membros e trainees de forma automática.
*   **RF32 - Controle de Presença e Sanções Éticas (Código de Ética):** O sistema deve permitir o registro de presença dos membros em Reuniões Gerais (RG) e Assembleias Gerais (AG).
    *   *Regra de Negócio 1 (RG):* O sistema deve emitir um alerta automático para a Diretoria de Gestão de Pessoas quando um membro acumular 3 (três) ausências recorrentes sem justificativa válida em RGs, para fins de abertura de processo de desligamento (conforme *Código de Ética, pág. 2*).
    *   *Regra de Negócio 2 (AG):* O sistema deve emitir um alerta imediato de desligamento para a Diretoria de Gestão de Pessoas caso um membro falte a uma Assembleia Geral sem justificativa prévia validada pelo Conselho Consultivo e Diretoria Executiva (conforme *Código de Ética, pág. 2*).
*   **RF33 - Exclusão Definitiva de Dados Sensíveis (Direito ao Esquecimento):** Em conformidade com a LGPD, o sistema deve permitir a exclusão permanente e irrecuperável de dados pessoais sensíveis de ex-membros mediante solicitação, mantendo apenas dados históricos anonimizados para fins de estatísticas institucionais.

### Módulo 6: Relatórios e Dashboards Executivos
*   **RF34 - Painel de Indicadores de GP:** O sistema deve disponibilizar gráficos e métricas consolidadas sobre clima organizacional, taxa de engajamento, turnover, absenteísmo em reuniões e satisfação das equipes.
*   **RF35 - Dashboard de Desempenho Comercial:** O sistema deve gerar relatórios visuais com indicadores de desempenho (KPIs) de vendas, incluindo taxa de conversão do funil, tempo médio de fechamento, volume de novos leads e progresso em relação às metas anuais.
*   **RF36 - Dashboard de Métricas de Produtividade de Projetos:** O sistema deve gerar relatórios com indicadores de desempenho técnico, como tempo médio de desenvolvimento por tipo de funcionalidade, taxa de retrabalho, desvio de estimativas e desvios em relação à baseline do cronograma.

---

## 2. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais definem os critérios de qualidade, restrições técnicas e padrões de segurança do sistema.

### Segurança, Privacidade e Conformidade
*   **RNF01 - Conformidade com a LGPD e Criptografia:** O sistema deve garantir a conformidade com a Lei Geral de Proteção de Dados (LGPD). Todos os dados pessoais sensíveis (como CPF, RG e dados de saúde de membros) e informações confidenciais de clientes (contratos e propostas) devem ser criptografados em repouso (banco de dados) e em trânsito (utilizando protocolo HTTPS/TLS).
*   **RNF02 - Autenticação Multifator (MFA):** O sistema deve exigir autenticação multifator (MFA) para usuários com perfis administrativos (como Assessoria de GP, Diretoria e Administradores) que possuem acesso a dados confidenciais e cadastros gerais.
*   **RNF03 - Auditabilidade de Escopo:** Qualquer alteração em requisitos de projetos previamente aprovados deve gerar um log de auditoria imutável contendo data, hora, usuário responsável e o impacto estimado no projeto, impedindo alterações retroativas sem autorização especial do administrador.

### Desempenho e Escalabilidade
*   **RNF04 - Desempenho de Busca e Consultas:** O mecanismo de busca global e as consultas ao banco de dados histórico de tarefas, estimativas e membros devem retornar resultados relevantes em um tempo máximo de 2 segundos, mesmo sob condições normais de rede e com alto volume de dados acumulados.
*   **RNF05 - Escalabilidade da Arquitetura:** A arquitetura do sistema deve ser escalável, permitindo o aumento contínuo do volume de dados (leads, atas, propostas, projetos e registros históricos de membros) e do número de usuários ativos simultâneos sem degradação do desempenho do software.

### Usabilidade e Interface
*   **RNF06 - Compatibilidade Multiplataforma e Responsividade:** O sistema deve ser uma aplicação baseada na web (SaaS) responsiva, compatível com os principais navegadores do mercado (Chrome, Firefox, Safari, Edge) e otimizada para uso em computadores pessoais (desktops e notebooks) de diferentes sistemas operacionais (Windows, macOS e Linux).
*   **RNF07 - Usabilidade e Baixa Fricção:** A interface do sistema deve ser intuitiva, projetada para minimizar cliques. O processo para criar, editar ou salvar um documento técnico ou ata não deve exigir mais do que 3 cliques. O editor de documentação deve suportar formatação em Markdown e atalhos de teclado semelhantes a ferramentas de mercado (Notion/Google Docs).
*   **RNF08 - Facilidade de Aprendizado (Curva de Aprendizado):** O sistema deve possuir uma interface intuitiva que permita que novos membros da EJCM consigam operar funções básicas de cadastro, consulta e atualização de tarefas com um treinamento básico de, no máximo, 20 minutos.

### Confiabilidade, Disponibilidade e Recuperação
*   **RNF09 - Disponibilidade (Uptime):** O sistema deve apresentar uma taxa de disponibilidade mínima de 99,5% (uptime), operando de forma contínua 24/7.
*   **RNF10 - Confiabilidade e Salvamento Automático:** O sistema deve possuir um mecanismo de salvamento automático em tempo real para a edição de documentos, atas de reuniões e descrições de tarefas, evitando a perda de dados por falhas de conexão ou fechamento acidental do navegador.
*   **RNF11 - Backup e Recuperação de Desastres:** O sistema deve realizar rotinas de backup diárias e automáticas de toda a base de dados e arquivos armazenados. Em caso de falhas críticas, o tempo máximo de recuperação (RTO - Recovery Time Objective) deve ser de, no máximo, 4 horas.
*   **RNF12 - Consistência e Validação de Dados:** O sistema deve possuir mecanismos de validação sintática (ex: validação de formato de CPF, e-mail, CNPJ e datas) no recebimento de dados via formulários ou integrações para mitigar erros humanos e inconsistências na base de dados centralizada.

### Interoperabilidade
*   **RNF13 - Interoperabilidade e Exportação de Dados:** O sistema deve permitir a exportação de relatórios, cronogramas, backlogs e dados cadastrais em formatos estruturados e legíveis por outras ferramentas de mercado (como CSV, PDF e XLSX), bem como a importação de dados de planilhas e integração com ferramentas legadas (Google Drive, Notion, GitHub).