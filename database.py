import sqlite3

database = 'database.sqlite'

def init_db():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("""
    CREATE table stats (
        id integer primary key,
        chat text,
        count integer
    );
    """)
    cursor.execute("""
    CREATE table commands (
        id integer primary key,
        command text,
        count integer
    );
    """)
    cursor.execute("""
    CREATE table user (
        id integer primary key,
        user_id text
    );
    """)
    cursor.execute("""
    CREATE table level (
        id integer primary key,
        chat text,
        level text,
        game text
    );
    """)
    cursor.execute("""
    CREATE table game (
        id integer primary key,
        chat text,
        game text
    );
    """)
    connect.commit()
    connect.close()

def check_user(user_id):
    result = {}
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM user WHERE user_id='" + str(user_id)+"'")
    res = cursor.fetchall()
    connect.close()
    try:
        if res[0]:
            result["not_exist"] = False
            result["user_id"] = res[0][1]
    except:
        result["not_exist"] = True
    return result

def add_user(user_id):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM user")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into user values ("+str(new_id)+",'"+str(user_id)+"')")
    connect.commit()
    connect.close()

def add_level(chat,level,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM level")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into level values ("+str(new_id)+",'"+str(chat)+"','"+str(level)+"','"+str(game)+"')")
    connect.commit()
    connect.close()

def set_level(chat,level,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM level WHERE chat='"+chat+"' and game='"+game+"'")
    result = cursor.fetchall()
    connect.close()
    if result:
        change_level(chat,level,game)
    else:
        add_level(chat,level,game)

def change_level(chat,level,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("UPDATE level SET level='"+str(level)+"' WHERE chat='"+chat+"' and game='"+game+"'")
    connect.commit()
    connect.close()

def add_game(chat,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM game")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into game values ("+str(new_id)+",'"+str(chat)+"','"+str(game)+"')")
    connect.commit()
    connect.close()

def set_game(chat,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM game WHERE chat='"+chat+"'")
    result = cursor.fetchall()
    connect.close()
    if result:
        change_game(chat,game)
    else:
        add_game(chat,game)

def change_game(chat,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("UPDATE game SET game='"+str(game)+"' WHERE chat='"+chat+"'")
    connect.commit()
    connect.close()

def set_stat(chat):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM stats WHERE chat='"+chat+"'")
    result = cursor.fetchall()
    connect.close()
    if result:
        increase(chat,result[0][-1]+1)
    else:
        add(chat)
    
def increase(chat,count):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("UPDATE stats SET count="+str(count)+" WHERE chat='"+chat+"'")
    connect.commit()
    connect.close()

def add(chat):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM stats")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into stats values ("+str(new_id)+",'"+str(chat)+"',1)")
    connect.commit()
    connect.close()

def set_stat_command(command):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM commands WHERE command='"+command+"'")
    result = cursor.fetchall()
    connect.close()
    if result:
        increase_command(command,result[0][-1]+1)
    else:
        add_command(command)
    
def increase_command(command,count):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("UPDATE commands SET count="+str(count)+" WHERE command='"+command+"'")
    connect.commit()
    connect.close()

def add_command(command):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM commands")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into commands values ("+str(new_id)+",'"+str(command)+"',1)")
    connect.commit()
    connect.close()

def get_db(table):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM "+table)
    result = cursor.fetchall()
    connect.close()
    return result

def get_game(chat):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM game WHERE chat = '"+chat+"'")
    result = cursor.fetchall()
    connect.close()
    return result

def get_level(chat,game):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM level WHERE game = '"+game+"' and chat = '"+chat+"'")
    result = cursor.fetchall()
    connect.close()
    return result

def get_chats_up_10():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM stats WHERE count >= 10")
    result = cursor.fetchall()
    connect.close()
    return result

def get_chats_down_10():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM stats WHERE count < 10")
    result = cursor.fetchall()
    connect.close()
    return result

if __name__ == '__main__': 
    init_db()
