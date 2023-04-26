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
]
