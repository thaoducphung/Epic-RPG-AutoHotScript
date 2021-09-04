import sqlite3
from sqlite3 import Error
import os
import re

dict_rubies = {
    'whyimpro#9865': None,
    'TKU#0536' : None,
    'NighD#4288': None,
}
stringA = "NOPE! you have 89 rubies \
Better luck next time, TKU !"
stringB = "<:normiefish:697940429999439872> **normie fish**: 103\n<:goldenfish:697940429500317727> **golden fish**: 400\n<:EPICfish:543182761431793715> **EPIC fish**: 2\n<:woodenlog:770880739926999070> **wooden log**: 2002\n<:EPIClog:541056003517710348> **EPIC log**: 231\n<:SUPERlog:541384398503673866> **SUPER log**: 21\n<:MEGAlog:545396411316043776> **MEGA log**: 12\n<:HYPERlog:546054891408457730> **HYPER log**: 1\n<:ULTRAlog:547252914654150666> **ULTRA log**: 1\n<:Apple:697940429668089867> **apple**: 307\n<:Banana:697940429483540522> **banana**: 6\n<:ruby:603304907650629653> **ruby**: 89\n<:wolfskin:541384010690199552> **wolf skin**: 43\n<:zombieeye:542483215122694166> **zombie eye**: 60\n<:unicornhorn:545329267425149112> **unicorn horn**: 32\n<:mermaidhairs:545721882805272596> **mermaid hair**: 45\n<:chip:546048827073757205> **chip**: 7\n<:potatocrop:818712007539818517> **potato**: 544\n<:carrotcrop:818712920820285450> **carrot**: 151\n<:breadcrop:818716266457071626> **bread**: 180"
stringC = "<:normiefish:697940429999439872> **normie fish**: 103\n<:goldenfish:697940429500317727> **golden fish**: 400\n<:EPICfish:543182761431793715> **EPIC fish**: 2\n<:woodenlog:770880739926999070> **wooden log**: 2002\n<:EPIClog:541056003517710348> **EPIC log**: 231\n<:SUPERlog:541384398503673866> **SUPER log**: 21\n<:MEGAlog:545396411316043776> **MEGA log**: 12\n<:HYPERlog:546054891408457730> **HYPER log**: 1\n<:ULTRAlog:547252914654150666> **ULTRA log**: 1\n<:Apple:697940429668089867> **apple**: 307\n<:Banana:697940429483540522> **banana**: 6\n<:wolfskin:541384010690199552> **wolf skin**: 43\n<:zombieeye:542483215122694166> **zombie eye**: 60\n<:unicornhorn:545329267425149112> **unicorn horn**: 32\n<:mermaidhairs:545721882805272596> **mermaid hair**: 45\n<:chip:546048827073757205> **chip**: 7\n<:potatocrop:818712007539818517> **potato**: 544\n<:carrotcrop:818712920820285450> **carrot**: 151\n<:breadcrop:818716266457071626> **bread**: 180"
# rubies_number = re.search(r'\d+', stringA.split('\n')[0]))
rubies_number = re.search(r'\*\*ruby\*\*: \d+', stringB)
if rubies_number:
    rubies_number = rubies_number.group(0)
else:
    rubies_number = 0
print('rubies_number',rubies_number)

print()

rubies_number = re.search(r'\*\*ruby\*\*: \d+', stringC)
if rubies_number:
    rubies_number = rubies_number.group(0)
else:
    rubies_number = 0
print('rubies_number',rubies_number)

question = "**EPIC NPC**: I have a special trade today!\nI will give **80 <:EPICwoodenlog:541056003517710348> EPIC logs** to the first player who gives me **40 <:woodenlog:770880739926999070> wooden logs**"
value =  "The first player who types the following sentence will get it!\n**OWO ME!!!**"
if "I have a special trade today" in question:
    print('You need to type this following text:')
    type_pattern = '\*\*[\w !]+\*\*' # **OWO ME!!!**
    type_text = re.search(type_pattern,value)
    print('type_text',type_text)
    type_text = type_text.group(0).replace("*","")
    print(type_text)
    print('END HERE!')

asdasd

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
    # finally:
        # if conn:
            # conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_rubies_user(conn, ruby_num): 
    insert_data_sql = \
    """
    INSERT INTO rubies(user_name,rubies) VALUES(?,?)
    """
    cur = conn.cursor()
    cur.execute(insert_data_sql, ruby_num)
    conn.commit()
    return cur.lastrowid


dir_path = os.path.dirname(os.path.realpath(__file__))

create_table_sql = \
"""CREATE TABLE IF NOT EXISTS rubies (
    user_name VARCHAR(20) PRIMARY KEY,
    rubies INTEGER NOT NULL
);"""



if __name__ == '__main__':

    

    database = os.path.join(dir_path,'db','ruby_pythonsqlite.db')

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create rubies table
        create_table(conn, create_table_sql)

    else:
        print("Error! cannot create the database connection.")

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, create_table_sql)
    else:
        print("Error! cannot create the database connection.")

    # insert data to table
    ruby_user = ('NighD#4288',10)
    ruby_id = create_rubies_user(conn, ruby_user)
