from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from database import Base, HabitScore
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST =os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')


DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

#Creating engine and session
def createngine():
    try:
        engine = create_engine(DATABASE_URL)
        # Testa a conexão executando uma query simples
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        print("Conexão bem-sucedida!")
        return engine
    except Exception as e:
        print(f"Erro na conexão: {e}")



def ingestdatatopostgres(df,engine):
    df.to_sql("habitscore",engine,if_exists= 'replace',index=False)

if __name__ == "__main__":
    createngine()

