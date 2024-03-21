import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
db_name = os.getenv('POSTGRES_DB')
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}', echo=True)