# BAKERY - API de Venda de Bolos

A API "Bakery" tem como objetivo fornecer um site de venda de bolos pela internet. 

O usuário poderá:
- cadastrar-se, 
- escolher um produto da base de dados, 
- calcular o preço total do pedido, 
- fazer um pedido,
- consultar o pedido, a data e o endereço de entrega.

---
## Como executar 

Clonar o repositório e, em seguida, ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente recomendado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Uma vez criado um ambiente, para ativá-lo, execute o comando:

```bash
(base)$ conda activate env
```

![alt text](/img/image-1.png)

Automáticamente ficará em andamento o ambiente "env". Para instalar as dependências descritas no arquivo 'requirements.txt' do projeto execute o comando:

```
(env)$ pip install -r requirements.txt
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Fazer click em "Swagger UI" para acessar a documentação da API.

![alt text](/img/image-2.png)

Na API será possível ver as diferentes requisições que podem ser feitas:

![alt text](/img/image-3.png)

Para adicionar um novo cliente, clicar na opção "POST /clientes", depois clicar em "Try it out" e, em seguida, preencher os campos com os dados do cliente e executar:

![alt text](/img/image-4.png)

![alt text](/img/image-5.png)

Uma vez feito o POST do cliente novo, recebemos a resposta com o código 200 e os dados do cliente.

![alt text](/img/image-6.png)

Se o cliente já existir na base de dados, o servidor retornará uma mensagem e não será possível cadastrar o cliente novamente:

![alt text](/img/image-7.png)

A tabela de "produtos" contém alguns produtos já cadastrados. O usuário não tem a opção de adicionar novos produtos à base, mas pode consultar todos os produtos disponíveis.

Para consultar os produtos na base de dados, clicar em "GET /produtos" e depois em "Try it out". Nesse caso, não será necessário preencher nenhum campo.

![alt text](/img/image-9.png)

Para fazer um pedido, clicar na opção "POST /pedidos" e depois em "Try it out". Para adicionar um pedido, o cliente tem que estar cadastrado na base. Se não estiver cadastrado, não será possível adicionar um pedido.

![alt text](/img/image-10.png)

Os dados do pedido que serão salvos na base de dados são: CPF do cliente, endereço de entrega, preço final e data de inserção do pedido.

![alt text](/img/image-11.png)

Se informar um CPF que não foi cadastrado na base, a mensagem retornada será: 404 Not Found.

![alt text](/img/image-12.png)

Finalmente, para consultar os pedidos feitos pelo usuário, utilizar o "GET /pedidos/" e informar o CPF do cliente. 

![alt text](/img/image-13.png)

Logo depois de executar, será possível ver a resposta com o código 200 e a lista de pedidos feitos pelo cliente com os respectivos preços, datas de inserção e endereços de entrega.

![alt text](/img/image-14.png)








