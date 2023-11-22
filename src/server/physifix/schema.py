import graphene

class Query(graphene.ObjectType):
    # Define your queries here...
    pass

class Mutation(graphene.ObjectType):
    # Define your mutations here...
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
