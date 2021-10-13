# desafio_backend_iTFLEX

CRUD de certificados.

</br>

> ## Objetivo

</br>

O desafio é criar API para gerenciamento de certificados e uma interface para consumir essas apis. O front e back devem ser contruidos separadamente utilizando conceito de RESTAPI. Deve-se poder cadastrar, listar, editar e deletar.

</br>
</br>

> ## Deploy no Heroku - Base URL

<br>

- https://desafio-backend-itflex.herokuapp.com/

</br></br>

> ## Diagrama ER

</br>

![diagram_er](./diagram_er.png)

</br>
</br></br>

> ## Inicializando o app

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

<br><br></br></br>

> ## Endpoints

<br></br>

> ### POST - Cadastro de certificados

<br>

    POST /api/certificates

- Precisa enviar no corpo da requisição:

  - "username" obrigatório e único, permitindo caracteres `a-z` e `0-9` e máximo de caracteres 30.
  - "name" => obrigatório e máximo de caracteres deve ser 255
  - "description" => não é obrigatório
  - "groups" => lista com código dos grupos
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

<br><br></br>

> ### GET - Lista certificados cadastrados
>
> </br>

```
GET /api/certificates
```

<br>

- orderna certificados por username

  ```
  GET /api/certificates?order_by=username
  ```

<br>

- orderna certificados por name

  ```
  GET /api/certificates?order_by=name
  ```

</br></br></br>

> ### GET - Lista certificados de um username/name especifico

</br>

```
GET /api/certificates/of_the_username/<string:username>

ou

GET /api/certificates/of_the_name/<string:name>
```

**_Exemplo_**

    GET /api/certificates/of_the_username/wesleydcm

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
        {
          "code": 1,
          "group_name": "Adm"
        },
        {
          "code": 15,
          "group_name": "Comercial"
        }
      ]
    }

**_Caso nao tenha certificados para um username, vocẽ deve ter o seguinte retorno:_**

    GET /api/certificates/of_the_username/batman

```
    {
      "msg": "there are no certificates for username: batman"
    }
```

<br>
<br>

> ### Delete - Certificados

<br>

```
DELETE /api/certificates/<int:id>
```
