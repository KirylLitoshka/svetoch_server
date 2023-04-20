from electricity.models import *
from views import BaseView, DetailView, ListView

__all__ = [
    "AreasListView", "AreaDetailView"
]


class AreasListView(ListView):
    model = areas


class AreaDetailView(DetailView):
    model = areas
