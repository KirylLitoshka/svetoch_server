import asyncio

from aiohttp import web


@web.middleware
async def handle_json_error(request, handler):
    try:
        return await handler(request)
    except asyncio.CancelledError:
        raise
    except Exception as e:
        return web.json_response({"success": False, "reason": f"{e.__class__.__name__}: {str(e)}"})
