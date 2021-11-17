from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from config import connection_db

# Local host
#connection_db = "sqlite:///basedatos.db"
connection_db = "postgresql://ajojygondiwwws:c7a48242d23dfa345fbe78951184ef2b354e8252992dfd68de1781013909bc1d@ec2-54-147-76-191.compute-1.amazonaws.com:5432/dbcpd8j5459210"

Base = declarative_base()

engine = create_engine(connection_db)

Session = sessionmaker(bind=engine)