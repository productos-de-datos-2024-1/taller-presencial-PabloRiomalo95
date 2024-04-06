"""Create database and tables for the project"""

import json
import logging
import os.path
import sqlite3


CONFIG_FILE = "src/2_database/config.json"
SQL_SCRIPT = "src/2_database/create_table.sql"


try :
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
except:
    raise FileNotFoundError(f"File {CONFIG_FILE} not found")


## C:\Users\Pablo\Documents\taller-presencial-PabloRiomalo95\datalake

logging.basicConfig(
    filename=os.path.join(
        config["LOGS_DIR"],
        config["CREATE_DATABASE_LOG"],
    ),
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def create_database():
    """Creates the database file."""
    database = os.path.join(
        config["DATABASE_DIR"],
        config["DATABASE_NAME"],
    )
    conn = sqlite3.connect(database)
    conn.close()


def load_sql_script():
    """Loads sql script from file"""
    logging.info("Reading script for creating house price table")
    try :
        with open(SQL_SCRIPT, 'r') as f:
            sql_script = f.read()
    except:
        raise FileNotFoundError(f"File {SQL_SCRIPT} not found")

    # if not pkg_resources.resource_exists(__name__, SQL_SCRIPT):
    #     raise FileNotFoundError(f"File {SQL_SCRIPT} not found")
    # with pkg_resources.resource_stream(__name__, SQL_SCRIPT) as file:
    #     sql_script = file.read().decode("utf-8")
    return sql_script


def create_tables(sql_script):
    """Creates tables"""
    logging.info("Starting table creation")
    database = os.path.join(config["DATABASE_DIR"], config["DATABASE_NAME"])
    conn = sqlite3.connect(database)
    conn.execute(sql_script)
    conn.commit()
    conn.close()
    logging.info("Table creation completed")


def main():
    """Orchestrates database creation"""
    create_database()
    sql_script = load_sql_script()
    create_tables(sql_script)


if __name__ == "__main__":
    main()
