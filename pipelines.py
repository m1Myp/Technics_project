import sqlite3

class SqliteDemoPipeline:

    def __init__(self):

        ## Create/Connect to database
        self.con = sqlite3.connect('demo.db')

        ## Create cursor, used to execute commands
        self.cur = self.con.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes(
            text TEXT,
            tags TEXT,
            author TEXT
        )
        """)


    def process_item(self, item, spider):

        ## Define insert statement
        self.cur.execute("""
            INSERT INTO quotes (text, tags, author) VALUES (?, ?, ?)
        """,
        (
            item['text'],
            str(item['tags']),
            item['author']
        ))

        ## Execute insert of data into database
        self.con.commit()
        return item