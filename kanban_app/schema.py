# kanban_app/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Column, Card

class CardType(DjangoObjectType):
    class Meta:
        model = Card

class ColumnType(DjangoObjectType):
    class Meta:
        model = Column

class CreateCard(graphene.Mutation):
    card = graphene.Field(CardType)

    class Arguments:
        content = graphene.String(required=True)
        column_id = graphene.ID(required=True)

    def mutate(self, info, content, column_id):
        column = Column.objects.get(pk=column_id)
        card = Card(content=content, column=column)
        card.save()
        return CreateCard(card=card)

class UpdateCard(graphene.Mutation):
    card = graphene.Field(CardType)

    class Arguments:
        card_id = graphene.ID(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, card_id, content):
        card = Card.objects.get(pk=card_id)
        card.content = content
        card.save()
        return UpdateCard(card=card)

class RemoveCard(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        card_id = graphene.ID(required=True)

    def mutate(self, info, card_id):
        try:
            card = Card.objects.get(pk=card_id)
            card.delete()
            return RemoveCard(success=True)
        except Card.DoesNotExist:
            return RemoveCard(success=False)

class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
    update_card = UpdateCard.Field()
    remove_card = RemoveCard.Field()

class Query(graphene.ObjectType):
    columns = graphene.List(ColumnType)

    def resolve_columns(self, info):
        return Column.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
