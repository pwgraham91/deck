__author__ = 'GoldenGate'
from django import template
register = template.Library()

@register.filter
def first_two(list):
    if list is not None and len(list):
        return list[:2]

@register.filter
def aces_only(card):
    if card is not None and card.rank == "ace":
        return card

@register.filter
def rank_only(card, rank):
    if card is not None and card.rank == rank:
        return rank