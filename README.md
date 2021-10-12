# desafio_backend_itflex

CRUD de usuário com autenticação e autorização.

### Objetivo

O desafio é criar API para gerenciamento de certificados e uma interface para consumir essas apis. O front e back devem ser contruidos separadamente utilizando conceito de RESTAPI. Deve-se poder cadastrar, listar, editar e deletar.
</br>
</br>

### Deploy no Heroku - Base URL

https://desafio-backend-itflex.herokuapp.com/

</br>
</br>

### Inicializando o app

</br>

1. Crie e ative o venv (ambiente virtual);

   ```
   $ python -m venv venv
   ```

2. Instale as dependências do projeto;

   ```
   $ pip install -r requirements.txt
   ```

3. Crie um banco de dados postgreSQL

</br>

4.  Crie e configure o .env com base no arquivo .env.example, em seguida substitua com as informações do seu banco de dados

    ```
    SQLALCHEMY_DATABASE_URI=postgresql://seuUsuário:suaSenha@localhost:5432/seuBanco
    ```

    </br>

5.  Atualize o banco de dados

    ```
    $ flask db migrate
    $ flask db upgrade
    ```

</br>

- **Rode, e teste as rotas**

  ```
  $ flask run
  ```
