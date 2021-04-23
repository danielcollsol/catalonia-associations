from sqlalchemy import create_engine
import psycopg2


def load_df_to_postgres(dataframe, db_config, schema, table_name):
    engine = create_engine('postgresql://{username}:{password}@{host}:{port}/{dbname}'.format(
                                                                                  username = db_config['username'],
                                                                                  password = db_config['password'],
                                                                                  host = db_config['host'],
                                                                                  port = db_config['port'],
                                                                                  dbname = db_config['dbname'],
    ))
    dataframe.to_sql(table_name, engine,  schema=schema, if_exists='replace')




