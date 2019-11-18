import graphene

import alocca.stock.schema


class Query(alocca.stock.schema.Query, graphene.ObjectType):
    pass


class Mutation(alocca.stock.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,mutation=Mutation)