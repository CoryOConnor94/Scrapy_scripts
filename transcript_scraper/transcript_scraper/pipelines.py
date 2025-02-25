# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging
import pymongo
import sqlite3

# class MongodbPipeline:
#    """Pipeline for connecting to and storing scraped data in MongoDB"""
#     collection_name = 'transcripts'
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient("mongodb+srv://{username}:{password}@cluster0.wi7qa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   # Connect to cluster
#         self.db = self.client['My_Database']    # Creates db when spider is opened
#
#     def close_spider(self, spider):
#         self.client.close()     # Close connection to db
#
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert_one(item)    # Insert scraped item to database
#         return item

class SQLitePipeline:
    """Pipeline for connecting to and storing scraped data in an SQLite db file"""

    def open_spider(self, spider):
        self.connection = sqlite3.connect('transcripts.db')     # Create database file
        self.c = self.connection.cursor()     # Create cursor object that will execute SQL queries
        # Try except block to catch table already exists error
        try:
            # Query
            self.c.execute("""
                CREATE TABLE transcripts(
                    title TEXT,
                    plot TEXT,
                    url TEXT
                )
            """)
            self.connection.commit()
        except sqlite3.OperationalError:
            pass


    def close_spider(self, spider):
        self.connection.close()     # Close connection to db

    def process_item(self, item, spider):
        print("Processing item:", item)  # Debugging
        self.c.execute("""
            INSERT INTO transcripts (title,plot,url) VALUES(?,?,?)
        """, (
            item.get('Title'),
            item.get('Plot'),
            item.get('Url')
        ))
        self.connection.commit()
        return item

