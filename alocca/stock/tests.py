# TRIED TO IMPLEMENT SOME TESTS HERE BUT DID NOT FIND MUCH HELP WITH THE EXAMPLES FROM GRAPHENE DOCUMENTATION

from graphene.test import Client
from alocca.schema import schema


def test_query_all_portfolios():
    client = Client(schema)

    executed = client.execute('''
        query{
            allPortfolios {
                id,
                name,
            }
        }'''
                              )

    assert executed == {
        'data': {
            "allPortfolios": [
                {
                    "id": "1",
                    "name": "Tesseract2"
                },
                {
                    "id": "2",
                    "name": "Testeeesdfde"
                },
                {
                    "id": "3",
                    "name": "Testeeesdfde"
                },
                {
                    "id": "4",
                    "name": "Testeeesdsdsdfde"
                },
                {
                    "id": "5",
                    "name": "Testeeesdsdsdfde"
                },
                {
                    "id": "6",
                    "name": "Testeeesdsssddsdsddsdfde"
                }
            ]
        }
    }
