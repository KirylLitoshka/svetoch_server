from electricity.models import *
from sqlalchemy.sql import func, select, text
from views import DetailView, ListView, pretty_json, web

__all__ = [
    "AreasListView", "AreaDetailView", "CiphersListView", "CipherDetailView"
]


class AreasListView(ListView):
    model = areas


class AreaDetailView(DetailView):
    model = areas


class CiphersListView(ListView):
    model = ciphers


class CipherDetailView(DetailView):
    model = ciphers
