# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class NewsPipeline:
    def __init__(self) -> None:
        self.create_conn()
        self.create_table()

    def create_conn(self):
        database_path = 'my_database.db'
        # Create a connection to the SQLite database
        self.connection = sqlite3.connect(database_path)
        # Create a cursor object using the connection
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS news_table
                  ( date TEXT, author TEXT,title TEXT,content TEXT)''')


    def process_item(self, item, spider):
        data_to_insert=(item["date"],item["author"],item["title"],item["content"])
        self.store_data(self,data_to_insert)
        return item
    
    def store_data(self,data_to_insert):
        self.cursor.executemany('INSERT INTO news_table (date, author, title,content) VALUES (?, ?, ?,?)', data_to_insert)
        self.connection.commit()