<h1 align="center">
  Leads -API
</h1>

Aplicação desenvolvida para poder escrever, atualizar e deletar leads. 

### URL API

https://alunos.kenzie.com.br/courses/66/pages/python-57-markdown?module_item_id=12883


<h2 align="center">
  Enpoints
</h2>

#

A API conta com 4 endpoints, sendo eles para criar, atualizar, deletar e pegar leads criados. Nehuma rota necessita de autenticação.

## Criar lead
#

`POST/leads - FORMATO DA REQUISIÇÃO`

```json
{
	"name": "John Doe",
	"email": "johndoe@email.com",
	"phone": "(xx)xxxxx-xxxx"
}
```

Caso a requisição seja bem sucedida receberá a resposta:

`POST/leads - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"data": {
		"name": "John Doe",
		"email": "johndoe@email.com",
		"phone": "(xx)xxxxx-xxxx",
		"creation_date": "Fri, 11 Feb 2022 15:21:43 GMT",
		"last_visit": "Fri, 11 Feb 2022 15:21:43 GMT",
		"visits": 1
	}
}
```


## Pegar leads
#

`GET/leads - FORMATO DA RESPOSTA - STATUS 200`

```json
{
	"leads": [
		{
			"name": "John Doe",
			"email": "johndoe@email.com",
			"phone": "(xx)xxxxx-xxxx",
			"creation_date": "Fri, 11 Feb 2022 15:21:43 GMT",
			"last_visit": "Fri, 11 Feb 2022 15:21:43 GMT",
			"visits": 1
		},
		{
			"name": "Doe John",
			"email": "doejohn@email.com",
			"phone": "(xx)xxxxx-xxxx",
			"creation_date": "Fri, 11 Feb 2022 11:21:42 GMT",
			"last_visit": "Fri, 11 Feb 2022 14:31:15 GMT",
			"visits": 2
		}
	]
}
```

## Atualizar leads
#

`PATCH/leads - FORMATO DA REQUISIÇÃO`

```json
{
	"email": "johndoe@email.com"
}
```

Caso a requisição seja bem sucedida receberá:

`STATUS 200`


## Delete lead
#

`DELETE/leads - FORMATO DA REQUISIÇÃO`

```json
{
	"email": "johndoe@email.com"
}
```
Caso a requisição seja bem sucedida receberá:

`STATUS 200`