# direSonar

Para rodar o projeto
1)Criar um bot no telegram
2)Inserir o token fornecido em bot>util
3)Fazer deploy do projeto em um domínio público
4)Criar um webhook acessando "https://api.telegram.org/bot<token>/setWebhook?url=<seu_dominio>/bot/event/"
5)Inserir python manage.py runserver no console

Atualmente o projeto está no ar e não possui interface para os usuários pois pode ser acessado a partir do @direSonar_bot no Telegram.

A função de mapeamento está descrita no em mapeamento>mapeamento.py e deve ser executada usando python3.


O código foi criado com  o framework Django, baseado em Python e a arquitetura segue o padrão sugerido. O deploy do código foi feito no Heroku mas não é persistente para o projeto, visto que para rodá-lo vpocê pode fazer deplpoy em seu próprio dominio opu utilizar o bot diretamente.
Para um ambiente de produção é necessária a integração com o sistema da clínica para agendamento de consultas e vizualização de agendamentos. Os dados usados são meramente ilustrativos.
