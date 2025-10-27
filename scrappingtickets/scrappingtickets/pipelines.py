# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

class ScrappingticketsPipeline:
    def process_item(self, item, spider):
        return item
    

class SaveToMySQLPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASS"),
            database = os.getenv("DB_NAME")
        )

        # create cursor, used to execute commands
        self.cur = self.conn.cursor()

        # sets up the table for us 
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS kiltro_tickets (
                        id INTEGER PRIMARY KEY,
                        date VARCHAR(255),
                        timestamp INTEGER,
                        band VARCHAR(255),
                        featured_band VARCHAR(255),
                        location VARCHAR(255), 
                        link_id VARCHAR(255)
                        )
                        """)
        
        #, PRIMARY KEY (id)
        
    def process_item(self, item, spider):

        self.cur.execute(""" 
            insert ignore into kiltro_tickets (
                        id,
                        date, 
                        timestamp,
                        band, 
                        featured_band, 
                        location, 
                        link_id
                        ) values (
                        %s, %s, %s, %s, %s, %s, %s
                        )""", (
                                int(item['id'][0][8:14]),
                                item['date'],
                                item['timestamp'],
                                item['band'],
                                item['featured band'],
                                item['loc'],
                                str(item['id'][0])
                        ))
        
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    
