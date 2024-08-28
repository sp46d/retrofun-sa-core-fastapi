from sqlalchemy import create_engine, MetaData
from retrofun.config import settings

# url_object = URL.create(
#     settings.sql_dialect,
#     username=settings.user_name,
#     password=settings.password,
#     host=settings.host,
#     port=settings.port,
#     database=settings.database,
# )
engine = create_engine(settings.db_url)

metadata = MetaData()