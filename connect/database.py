from sqlmodel import SQLModel, create_engine


paolo_sqlite_file_name = "paolo.db"
sqlite_url = f"sqlite:///{paolo_sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)