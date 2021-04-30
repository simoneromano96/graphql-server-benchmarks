import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphene import Schema, String, ObjectType, Enum

# Faker
from faker import Faker
fake = Faker()

sentence = fake.sentence()
status = fake.random_element(elements = ('ACTIVE', 'COMPLETED'))

print(status)
print(sentence)

class TodoStatus(Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"

    @property
    def description(self):
        if self == TodoStatus.ACTIVE:
            return "Active Todo"
        elif self == TodoStatus.COMPLETED:
            return "Completed Todo"
        else:
            return 'The todo status'


class Todo(ObjectType):
    id = graphene.ID(required=True, description="The Todo ID")
    description = String(required=True, description="The Todo text")
    status = TodoStatus(required=True, description="The Todo status")


class Query(ObjectType):
    todos = graphene.Field(graphene.List(
        Todo), required=True, description="Get the list of all todos")

    def resolve_todos(self, root):
        return []


schema = Schema(query=Query)

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))
