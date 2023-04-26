from electricity.models import *
from sqlalchemy.sql import and_, func, select, text
from views import DetailView, ListView, pretty_json, web

__all__ = [
    "AreasListView", "AreaDetailView", "CiphersListView", "CipherDetailView", "RatesListView", "RateDetailView"
]


class AreasListView(ListView):
    model = areas


class AreaDetailView(DetailView):
    model = areas


class CiphersListView(ListView):
    model = ciphers


class CipherDetailView(DetailView):
    model = ciphers


class RatesListView(ListView):
    model = rates

    async def get(self):
        async with self.request.app['db'].connect() as conn:
            max_dates = select(rates_history.c.rate_id, func.max(rates_history.c.entry_date).label("entry_date")) \
                .group_by(rates_history.c.rate_id).alias("max_dates")
            dates_with_value = select(
                rates_history.c.rate_id, max_dates.c.entry_date, rates_history.c.value).select_from(
                max_dates.join(rates_history, and_(
                    rates_history.c.rate_id == max_dates.c.rate_id,
                    rates_history.c.entry_date == max_dates.c.entry_date
                ))
            ).alias("dates_with_value")
            cursor = await conn.execute(
                select(rates, dates_with_value.c.entry_date, dates_with_value.c.value).select_from(
                    rates.join(dates_with_value, rates.c.id ==
                               dates_with_value.c.rate_id, isouter=True)
                ).order_by(rates.c.id)
            )
            result = [dict(row) for row in cursor.fetchall()]
            return web.json_response({"status": "success", "items": result}, dumps=pretty_json)


class RateDetailView(DetailView):
    model = rates
