# schema.py

import strawberry
from example.graphql.mutations.mutation import Mutation
from example.graphql.queries.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
