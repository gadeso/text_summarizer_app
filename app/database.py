from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import pymysql

# Configuración de la base de datos para SQLAlchemy
username = "admin"
password = "12345678"
host = "summarizer-db.c9iyc4yeeeax.eu-north-1.rds.amazonaws.com"
port = 3306
database = "mydatabase"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

print(f"Connecting to database...")

try:
    # Crear el motor de la base de datos
    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    # Definición del modelo
    class QueryResponse(Base):
        __tablename__ = "queries_responses"
        
        id = Column(Integer, primary_key=True, index=True)
        query = Column(Text, nullable=False)
        response = Column(Text, nullable=False)

    # Función para inicializar la base de datos
    def init_db():
        Base.metadata.create_all(bind=engine)

    # Función para verificar la conexión
    def check_connection():
        try:
            with engine.connect() as connection:
                connection.execute("SELECT 1")
            return True
        except SQLAlchemyError:
            return False

    # Función para ejecutar consultas de inserción directamente
    def execute_insert_query(query, params):
        connection = pymysql.connect(
            host='datos-api-record.cp2aaumeq6eu.eu-north-1.rds.amazonaws.com',
            port=3306,
            user='admin',
            password='12345678',
            database='query_songs',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
            connection.commit()
        finally:
            connection.close()

except SQLAlchemyError as e:
    print(f"An error occurred: {e}")