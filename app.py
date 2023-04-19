from aiohttp import web


def create_app():
    application = web.Application()
    return application


if __name__ == "__main__":
    web.run_app(create_app(), host="localhost", port=8000)
