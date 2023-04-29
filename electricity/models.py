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

objects = sa.Table(
    "objects", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("cipher_id", sa.Integer, sa.ForeignKey("ciphers.id", ondelete="SET NULL"), nullable=True),
    sa.Column("area_id", sa.Integer, sa.ForeignKey("areas.id", ondelete="SET NULL"), nullable=True),
    sa.Column("calculation_factor", sa.Integer, default=1),
    sa.Column("subscriber_type", sa.Integer, nullable=False, default=1),
    sa.Column("break_percentage", sa.Float, nullable=False, default=0.0),
    sa.Column("is_closed", sa.Boolean),
    sa.Column("counting_point", sa.Integer, nullable=False, default=0),
    sa.Column("ee", sa.Integer, nullable=False, default=0)
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
