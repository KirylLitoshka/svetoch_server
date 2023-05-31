from aiohttp import web
from sqlalchemy import delete, insert, select, update
from utils import pretty_json


class BaseView(web.View):
    model = None

    def __init__(self, request: web.Request) -> None:
        super().__init__(request)


class DetailView(BaseView):
    async def get(self):
        item_id = int(self.request.match_info["id"])
        print(item_id)
        async with self.request.app["db"].connect() as conn:
            cursor = await conn.execute(select(self.model).where(self.model.c.id == item_id))
            result = dict(cursor.fetchone())
            return web.json_response({"success": True, "item": result}, dumps=pretty_json)

    async def patch(self):
        item_id = int(self.request.match_info["id"])
        async with self.request.app["db"].begin() as conn:
            post_data = await self.request.json()
            await conn.execute(
                update(self.model).where(
                    self.model.c.id == item_id).values(**post_data)
            )
            return web.json_response({"success": True}, status=200, dumps=pretty_json)

    async def delete(self):
        item_id = int(self.request.match_info["id"])
        async with self.request.app["db"].begin() as conn:
            await conn.execute(
                delete(self.model).where(self.model.c.id == item_id)
            )
            return web.json_response({"success": True}, status=200, dumps=pretty_json)


class ListView(BaseView):
    async def get(self):
        async with self.request.app['db'].connect() as conn:
            cursor = await conn.execute(select(self.model).order_by(self.model.c.id))
            result = [dict(row) for row in cursor.fetchall()]
            return web.json_response({"success": True, "items": result}, status=200, dumps=pretty_json)

    async def post(self):
        async with self.request.app["db"].begin() as conn:
            post_data = await self.request.json()
            await conn.execute(insert(self.model).values(**post_data))
            return web.json_response({"success": True}, status=201, dumps=pretty_json)
