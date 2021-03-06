# desafio_backend_iTFLEX

## Objetivo

</br>

> Criar API para gerenciamento de certificados e uma interface para consumir essas apis.
> O front e back devem ser contruidos separadamente utilizando conceito de RESTAPI.
> Deve-se poder cadastrar, listar, editar e deletar.

</br>

## Tecnologias empregadas:

- Linguagem:
  - Python 3
- Framework:
  - Flask
- Banco de dados e migração:
  - PostgreSQL
  - Flask-Migrate
- ORM:
  - Flask-SQLAlchemy
- Design pattens:
  - Blueprints
  - e design pattern Flask Factory.
- Deploy no Heroku
- entre outras.

<br>

### BASE URI - certificates

- https://desafio-backend-itflex.herokuapp.com/api/certificates

</br>

## Diagrama ER

</br>

![diagram_er](./diagram_er.png)

</br>
</br></br>

## Inicializando o app

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

<br><br>

## Endpoints

<br>

> ## Cadastro de certificados

<br>

    POST /api/certificates

- Corpo da requisição deve conter:

  - username
    - Deve ser único, somente caracteres de `a-z` e `0-9` com máximo de caracteres 30
  - name
    - Máximo de caracteres deve ser 255
  - description
    - Não é obrigatório
  - expiration
    - Representa o número de dias que o certificado é valido, o número deve estar entre 10 e 3650.
  - groups
    - lista com código dos grupos
      - 01: Adm
      - 15: Comercial
      - 30: RH
      - 45: TI

**_Exemplo de envio_**

```json
{
  "username": "wesleydcm",
  "name": "Wesley da Costa Matos",
  "description": "",
  "groups": [1, 15],
  "expiration": 3650
}
```

**_Exemplo de resposta_**

```json
{
  "id": 1,
  "username": "wesleydcm",
  "name": "Wesley da Costa Matos",
  "description": "",
  "expiration": 3650,
  "expirated_at": "Fri, 10 Oct 2031 18:36:00 GMT",
  "created_at": "Tue, 12 Oct 2021 15:36:00 GMT",
  "updated_at": "Tue, 12 Oct 2021 15:36:00 GMT",
  "groups": [1, 15]
}
```

<br><br></br>

> ## Lista todos certificados cadastrados

</br>

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

</br></br>

> ## Lista certificados de um username/name especifico

</br>

```
GET /api/certificates/of_the_username/<string:username>

ou

GET /api/certificates/of_the_name/<string:name>
```

**_Exemplo de envio_**

    GET /api/certificates/of_the_username/wesleydcm

**_Exemplo de resposta_**

```json
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
```

**Caso nao tenha certificados para um username, vocẽ deve ter o seguinte retorno:**

**_Exemplo de envio_**

    GET /api/certificates/of_the_username/batman

**_exemplo de resposta_**

```json
{
  "msg": "there are no certificates for username: batman"
}
```

<br>
<br>

> ## Atualiza certificados

<br>

```
PATCH /api/certificates/<int:id>
```

- É possivel atualizar os seguintes dados:

  - username
    - Deve ser único, somente caracteres de `a-z` e `0-9` com máximo de caracteres 30
  - name
    - Máximo de caracteres deve ser 255
  - description
    - Não é obrigatório
  - expiration
    - Representa o número de dias que o certificado é valido, o número deve estar entre 10 e 3650.
  - groups
    - lista com código dos grupos
      - 01: Adm
      - 15: Comercial
      - 30: RH
      - 45: TI

- Os campos a serem atualizados, têm as mesma restrições citadas no cadastro de certificados.

**Exemplo de update**

- Antes da atualização

  ```json
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
  ```

**_Exemplo de envio_**

```
PATCH /api/certificates/1
```

```json
{
    "name": "Python 3"
    "description": "Curso intermediario de Python 3",
    "expiration": 365,
    "groups": [45]
}
```

**_Exemplo de resposta_**

```json
{
  "id": 1,
  "username": "wesleydcm",
  "name": "Python 3",
  "description": "Curso intermediario de Python 3",
  "expiration": 365,
  "expirated_at": "Wed, 12 Oct 2022 15:36:00 GMT",
  "created_at": "Tue, 12 Oct 2021 15:36:00 GMT",
  "updated_at": "Wed, 13 Oct 2021 08:03:41 GMT",
  "groups": [
    {
      "code": 45,
      "group_name": "Programação"
    }
  ]
}
```

<br>
<br>

> ## Deletar certificados

<br>

```
DELETE /api/certificates/<int:id>
```

- Caso tenha sucesso a rota não retorna dados do certificado corpo, caso o id informado não exista, você terá a seguinte resposta

```json
{
  "msg": "certificate not found!"
}
```
