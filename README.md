# LabEngSoft2-Psychologist

Requisitos do sistema (por ordem de prioridade):  
-Escolher psicólogos dentro de uma lista  
-Visualizar info do psicólogo + local de atendimento  
-Agendar consultas  
-Enviar comprovantes de pagamento. Aparentemente consultas com psicólogo podem ser pagas antes ou depois, o profissional decide. Seria mais prático pedir o pagamento antes para confirmar o agendamento (?)  
-Trocar mensagens (após 1ª consulta?)  
-Cadastrar plano de saúde e filtrar profissionais que atendem aquele plano??  

Tabelas do banco de dados

Informações do Paciente:  
ID do Paciente (chave primária)  
Nome Completo  
Data de Nascimento  
Gênero  
Endereço  
Número de Contato  
Endereço de Email  
Ficha Médica  
Plano de saúde(?)  
Histórico de Consultas (relacionamento com a tabela de consultas)  

Informações do Psicólogo:  
ID do Psicólogo (chave primária)  
Nome Completo  
Especialização  
Anos de Experiência  
Qualificações/Certificações  
Horários de Trabalho (pode ser uma tabela separada para flexibilidade)  
Taxa de Consulta  
Contato e Informações de Localização (endereço do consultório, telefone, email)  
Planos de saúde atendidos(?)  

Agendamento de Consultas:  
ID da Consulta (chave primária)  
ID do Paciente (chave estrangeira, relacionada à tabela do paciente)  
ID do Psicólogo (chave estrangeira, relacionada à tabela do psicólogo)  
Data e Hora da Consulta  
Duração da Consulta  
Status da Consulta (agendada, concluída, cancelada)  
Notas ou Comentários (detalhes adicionais sobre a consulta)  

Pagamentos (se aplicável):  
ID do Pagamento (chave primária) (?)  
ID da Consulta (chave estrangeira, relacionada à tabela de consultas)  
Valor Pago  
Data e Hora do Pagamento  
Método de Pagamento (cartão de crédito, débito, dinheiro, plano de saúde(?))  
Status do Pagamento (pendente, concluído, cancelado)  

Histórico Médico do Paciente (opcional, informações sensíveis):  
ID do Histórico (chave primária) (?)  
ID do Paciente (chave estrangeira, relacionada à tabela do paciente)  
Descrição do Histórico Médico  
Anexos (pode ser usado para armazenar arquivos, como resultados de exames)  

Autenticação e Segurança:  
Informações de login (se o sistema suportar login de usuários)  
Hashes de Senha (nunca armazene senhas em texto claro)  
Tokens de Sessão ou JWTs (para controle de sessão, especialmente em APIs)  
