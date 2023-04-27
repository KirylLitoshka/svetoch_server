from aiohttp import web
from electricity.views import *

routes = [
    web.route("GET", "/areas", AreasListView),
    web.route("POST", "/areas", AreasListView),
    web.route("GET", "/areas/{id}", AreaDetailView),
    web.route("PATCH", "/areas/{id}", AreaDetailView),
    web.route("DELETE", "/areas/{id}", AreaDetailView),
    web.route("GET", "/ciphers", CiphersListView),
    web.route("POST", "/ciphers", CiphersListView),
    web.route("GET", "/ciphers/{id}", CipherDetailView),
    web.route("PATCH", "/ciphers/{id}", CipherDetailView),
    web.route("DELETE", "/ciphers/{id}", CipherDetailView),
    web.route("GET", "/rates", RatesListView),
    web.route("POST", "/rates", RatesListView),
    web.route("GET", "/rates/{id}", RateDetailView),
    web.route("PATCH", "/rates/{id}", RateDetailView),
    web.route("DELETE", "/rates/{id}", RateDetailView),
    web.route("GET", "/meters", MetersListView),
    web.route("POST", "/meters", MetersListView),
    web.route("GET", "/meters/{id}", MeterDetailView),
    web.route("PATCH", "/meters/{id}", MeterDetailView),
    web.route("DELETE", "/meters/{id}", MeterDetailView)
]
