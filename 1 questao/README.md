1- Com base no layout abaixo, quais casos de testes você executaria para cobrir ao máximo todos os cenários da tela de cadastro da biblioteca. Como restrições, suponha que a senha tem que ter entre 6 e 10 caracteres.

- Testaria se aparecem as mensagens de erro ao tentar enviar o formulário sem nenhum dado preenchido e se elas estão compatíveis com suas labels;
- Testaria se a cada input enviado sem nenhum valor, se cada um possui uma mensagem de texto relacionada ou apenas o primeiro;
- Testaria se a cor de cada mensagem de erro é igual;
- Testaria se as mensagens de erro somem após inserir um valor dentro de seus respectivos inputs;
- Testaria se os placeholders de cada input estão compatíveis com suas labels de identificação e se eles somem ao serem inseridos dados dentro do input;
- Testaria se o campo "Nomes" aceita caracteres especiais/números, juntamente com o campo "Sobrenome";
- Testaria se é possível enviar apenas uma letra nos campos Nome/Sobrenome;
- Testaria se o campo "Email" aceita palavras sem ser um email propriamente dito;
- Testaria se o campo "Senha" ṕrotege a senha do usuário, tendo formato de "Password";
- Testaria se o campo "Senha" aceita senhas menores que 6 caracteres ou maior que 11 caracteres;
- Testaria se o campo "Telefone" possui um padrão que formata quando o usuário insere corretamente um número de telefone;
- Testaria se o campo "Telefone" envia números de telefone sem o identificador "9" ou sem o DDD do estado/país;
- Testaria se o campo "Telefone" aceita letras;
- Testaria se o campo "CEP" formata os números de forma que fique legível como um cep normalmente é;
- Testaria se o campo "CEP" aceita letras;
- Testaria se o campo "Sexo" pode ser digitado ou somente utilizado seu autocomplete, e caso possa ser digitado, se o texto digitado faz um filtro em seu autocomplete;
- Testaria se o checkbox de "Newsletter" é obrigatório por meio das mensagens de erro anteriormente citadas;
- Testaria se todas as labels estão com a escrita correta e pertencem àquela página;
