from sqlalchemy import create_engine, MetaData
from retrofun.config import settings


db_url = f'postgresql://{settings.user_name}:{settings.password}@{settings.host}:{settings.port}/{settings.database}'
engine = create_engine(db_url)


convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)