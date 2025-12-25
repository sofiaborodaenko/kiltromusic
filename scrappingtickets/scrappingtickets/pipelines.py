# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

class ScrappingticketsPipeline:
    def process_item(self, item, spider):
        return item
    

class SaveToPostgreSQLPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            sslmode="require"
        )

        self.cur=self.conn.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS kiltro_tickets (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                         timestamp INTEGER,
                        band TEXT,
                        featured_band TEXT,
                        location TEXT,
                        link_id TEXT
                        );
            """)
        
        self.conn.commit()
    
    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO kiltro_tickets (
                        id,
                        date, 
                        timestamp,
                        band, 
                        featured_band, 
                        location, 
                        link_id
                        ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s
                        ) ON CONFLICT (id) DO NOTHING;
            """, (
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
