import pymysql


def init_db():
    con = pymysql.connect(host="localhost", user="root", passwd='')
    cursor = con.cursor()

    # create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS password_database")
    con.commit()

    # create user table
    query = """
    CREATE TABLE IF NOT EXISTS password_database.user
    (
        Username VARCHAR(30) NOT NULL,
        Password VARCHAR(64) NOT NULL,
        Country_of_origin VARCHAR(30) NOT NULL,
        id INT(10) PRIMARY KEY AUTO_INCREMENT,
        salt VARCHAR(100) NOT NULL,
        iv char(77) NOT NULL,
        key_salt VARCHAR(32) NOT NULL
    )
    """
    cursor.execute(query)
    con.commit()
