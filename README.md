# desafio_backend_iTFLEX

CRUD de usuário com autenticação e autorização.

### Objetivo

O desafio é criar API para gerenciamento de certificados e uma interface para consumir essas apis. O front e back devem ser contruidos separadamente utilizando conceito de RESTAPI. Deve-se poder cadastrar, listar, editar e deletar.
</br>
</br>

### Deploy no Heroku - Base URL

https://desafio-backend-itflex.herokuapp.com/

</br>

### Diagrama ER

</br>
</br>

![diagram_er](./diagram_er.png)

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
  $ gunicorn "app:create_app()"
  ```

### Endpoints

#### Lista certificados cadastrados

```
GET /api/certificates
```

</br>

#### Register new certificate

```
POST /api/certificates
```

- Need to send in the requisition body:

  - "username" obrigatório e único, permitindo caracteres `a-z` e `0-9` e máximo de caracteres 30.

  - "name" => obrigatório e máximo de caracteres deve ser 255
  - "description" => não é obrigatório
  - "groups" => lista com código do grupo
  - "expiration" => representa o número de dias que o certificado é valido, o número deve estar entre 10 e 3650.

**_Exemplo de envio_**

    {
        "username": "wesleydcm",
        "name": "Wesley da Costa Matos",
        "description": "",
        "groups": [1, 15],
        "expiration" 3650,
    }

**_Exemplo de resposta_**

    {
        "id": 1,
        "username": "wesleydcm",
        "name": "Wesley da Costa Matos",
        "description": "",
        "expiration": 3650,
        "expirated_at": "Fri, 10 Oct 2031 18:36:00 GMT",
        "created_at": "Tue, 12 Oct 2021 15:36:00 GMT",
        "updated_at": "Tue, 12 Oct 2021 15:36:00 GMT",
        "groups": [
            1,
            15
        ]
    }
