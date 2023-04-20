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
            return web.json_response({"success": True, "data": result})

    async def patch(self):
        item_id = int(self.request.match_info["id"])
        async with self.request.app["db"].begin() as conn:
            post_data = await self.request.json()
            await conn.execute(
                update(self.model).where(
                    self.model.c.id == item_id).values(**post_data)
            )
            return web.json_response({"status": "success"}, status=200)

    async def delete(self):
        item_id = int(self.request.match_info["id"])
        async with self.request.app["db"].begin() as conn:
            await conn.execute(
                delete(self.model).where(self.model.c.id == item_id)
            )
            return web.json_response({"status": "success"}, status=200)


class ListView(BaseView):
    async def get(self):
        async with self.request.app['db'].connect() as conn:
            cursor = await conn.execute(select(self.model).order_by(self.model.c.id))
            result = [dict(row) for row in cursor.fetchall()]
            return web.json_response(data=result, status=200, dumps=pretty_json)

    async def post(self):
        async with self.request.app["db"].begin() as conn:
            post_data = await self.request.json()
            await conn.execute(insert(self.model).values(**post_data))
            return web.json_response({"status": "success", "input_value": post_data}, status=201, dumps=pretty_json)
