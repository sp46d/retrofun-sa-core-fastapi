from sqlalchemy import Table, Column, Integer, String, ForeignKey
from retrofun.database import metadata

Product = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), unique=True, index=True, nullable=False),
    Column('manufacturer_id', Integer, ForeignKey('manufacturers.id'), nullable=False),
    Column('year', Integer, index=True, nullable=False),
    Column('cpu', String(32), nullable=True),
)

Manufacturer = Table(
    'manufacturers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), unique=True, nullable=False, index=True),
)

