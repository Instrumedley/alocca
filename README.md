# Alocca

Everything for Alocca here

## Tech Stack

This project was built using Django (2.2.7), GraphQL with graphene library (2.1.8) and SQLite/MySQL database.

## Loading data into database
To load the instrument data into the database, go to the root project folder and run the following command

```bash
python3 manage.py loaddata input_format_data.json
```

## Accessing the GraphQL API

The docker container should have already started the server and made it accessible to you at:
```
http://127.0.0.1:8000/
```

If you would like to use a different port, you can always do

```
python3 manage.py runserver [port_number]
```
from the root project directory, replacing [port_number] with the desired value.

If you used the default port, The GraphQL API is available at

```
http://127.0.0.1:8000/graphql
```

## Example Queries

Here are a few queries you can do on the API:

**Query to fetch all Instruments, displaying their ids and name in return**
```
query{
    allInstruments {
        id,
        name,
    }
}
```
**Query to fetch all Portfolios,, displaying their ids and name in return**

```
query{
    allPortfolios {
        id,
        name,
    }
}
```

**Query Single Instrument based on a given id and display their name and symbol**
```
query{
  instrument(id: 1000) {
    name
    symbol
  }
}
```

**Query Single Portfolio based on a given id and display their name and description**
```
query{
  portfolio(id: 1000) {
    name
    description
  }
}
```

## Example Mutations

Here are just a few examples of mutations you can perform on the API


**Mutation to add a Portfolio and display its id, name and description**

```
mutation {
    createPortfolio(
        name: "Test Name", 
        description: "Test Description"
    ) 
    {
        id
        name
        description
    }
}
```
**Mutation to create a trade and display its id, buy_value and sell_value**

This mutation accepts the following parameters:
* portfolioId (required)
* instrumentId (required)
* volume (required)
* buyValue (required)
* sellValue (required)
* profitLoss (optional)

```
mutation {
  createTrade(
    portfolioId : 1,
    instrumentId: 3,
    volume: 4,
    buyValue: 3.33
    sellValue: 5.22
    profitLoss: 5.2
  )
  {
  	id
    buyValue
    sellValue
  }
}
```


**Mutation to update a portfolio of a given id.** 

Note: None will be created if id does not exist in DB
```
mutation updatePortfolio{
    updatePortfolio(id: 1, input:{
        name:"Tesseract2",
        description:"Acceptance2"
    })
    {
    portfolio{
        id
        name
    	description
    }
  }
}
```

