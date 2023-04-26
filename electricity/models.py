import sqlalchemy as sa

__all__ = [
    "metadata", "areas", "ciphers", "rates"
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
