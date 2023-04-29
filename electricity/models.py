import sqlalchemy as sa

__all__ = [
    "metadata", "areas", "ciphers", "rates", "rates_history", "meters", "workshops"
]

metadata = sa.MetaData()

areas = sa.Table(
    "areas", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String, nullable=False, unique=True)
)

ciphers = sa.Table(
    "ciphers", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("code", sa.String, nullable=True),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("rate_id", sa.Integer, sa.ForeignKey(
        "rates.id", ondelete="SET NULL"), nullable=True
              )
)

rates = sa.Table(
    "rates", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String, nullable=False)
)

rates_history = sa.Table(
    "rates_history", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("rate_id", sa.Integer, sa.ForeignKey(
        "rates.id", ondelete="CASCADE")),
    sa.Column("entry_date", sa.Date, nullable=False),
    sa.Column("value", sa.Float, nullable=False),
    sa.UniqueConstraint("rate_id", "entry_date", name="idx_rate_id_entry_date")
)

meters = sa.Table(
    "meters", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("capacity", sa.Integer, nullable=False),
    sa.UniqueConstraint("title", "capacity", name="idx_name_capacity")
)

workshops = sa.Table(
    "workshops", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String, unique=True, nullable=False)
)

object_meters = sa.Table(
    "object_meters", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("object_id", sa.Integer, sa.ForeignKey("objects.id", ondelete="CASCADE")),
    sa.Column("meter_id", sa.Integer, sa.ForeignKey("meters.id", ondelete="SET NULL"), nullable=True),
    sa.Column("meter_number", sa.String, nullable=True),
    sa.Column("meter_installation_date", sa.Date, nullable=True),
    sa.Column("meter_last_reading", sa.Float, default=0.0),
    sa.Column("meter_heating_percentage", sa.Float, default=0.0)
)
