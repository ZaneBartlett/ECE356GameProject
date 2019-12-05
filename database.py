import mysql.connector


def set_winner(game_number, winner):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        query = "UPDATE game_info SET winner = %s WHERE game_id = %s"
        vals = (winner, game_number)
        cursor.execute(query, vals)
        cnx.commit()
    finally:
        cnx.close()


def get_winner(game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        cursor.execute("""
                           select * from game_info
                       """)
        game_data = cursor.fetchall()
        for game in game_data:
            if game_number == game[0]:
                winner = "Player" + str(game[10])

        return winner
    finally:
        cnx.close()


def get_inputs(game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        cursor.execute("""
                        select * from game_info
                    """)
        game_data = cursor.fetchall()
        for game in game_data:
            if game_number == game[0]:
                responses = (game[3], game[4], game[5])

        return responses
    finally:
        cnx.close()


def get_question(game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        cursor.execute("""
                    select * from game_info
                """)
        game_data = cursor.fetchall()
        for game in game_data:
            if game_number == game[0]:
                question = game[2]

        return question
    finally:
        cnx.close()


def get_game_number():
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        cursor.execute("""
                select * from game_info
            """)
        game_data = cursor.fetchall()
        current_game_number = game_data[0][0]
        for game in game_data:
            if current_game_number < game[0]:
                current_game_number = game[0]

        return current_game_number
    finally:
        cnx.close()


def get_game_state(game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        cursor.execute("""
                select * from game_info
            """)
        game_data = cursor.fetchall()

        for game in game_data:
            if game_number == game[0]:
                game_state = game[1]

        return game_state
    finally:
        cnx.close()


def are_players_ready(game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        cursor.execute("""
                   select * from game_info
               """)
        game_data = cursor.fetchall()

        for game in game_data:
            if game_number == game[0]:
                ready_states = (game[6] + game[7] + game[8] + game[9])

        if ready_states == 4:
            return True
        else:
            return False
    finally:
        cnx.close()


def insert_user_input(player_number, user_text, game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        if player_number == 1:
            query = "UPDATE game_info SET question = %s WHERE game_id = %s"
            vals = (user_text, game_number)
            cursor.execute(query, vals)
        elif player_number == 2:
            query = "UPDATE game_info SET answer1 = %s WHERE game_id = %s"
            vals = (user_text, game_number)
            cursor.execute(query, vals)
        elif player_number == 3:
            query = "UPDATE game_info SET answer2 = %s WHERE game_id = %s"
            vals = (user_text, game_number)
            cursor.execute(query, vals)
        elif player_number == 4:
            query = "UPDATE game_info SET answer3 = %s WHERE game_id = %s"
            vals = (user_text, game_number)
            cursor.execute(query, vals)
        cnx.commit()
    finally:
        cnx.close()


def new_game():
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        query = "INSERT INTO game_info (game_id, game_state, question, answer1, answer2, answer3, player1_ready, " \
                "player2_ready, player3_ready, player4_ready) "
        cursor.execute(query)
        cnx.commit()
    except:
        print("game initialization failed")
    finally:
        cnx.close()


def player_ready(player_number, game_number):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        if player_number == 1:
            query = "UPDATE game_info SET player1_ready = %s WHERE game_id = %s"
            vals = (1, game_number)
            cursor.execute(query, vals)
        elif player_number == 2:
            query = "UPDATE game_info SET player2_ready = %s WHERE game_id = %s"
            vals = (1, game_number)
            cursor.execute(query, vals)
        elif player_number == 3:
            query = "UPDATE game_info SET player3_ready = %s WHERE game_id = %s"
            vals = (1, game_number)
            cursor.execute(query, vals)
        elif player_number == 4:
            query = "UPDATE game_info SET player4_ready = %s WHERE game_id = %s"
            vals = (1, game_number)
            cursor.execute(query, vals)
        cnx.commit()
    finally:
        cnx.close()


def next_game_state(game_number, game_state):
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='my_game')
    try:
        cursor = cnx.cursor()
        game_state += 1
        query = "UPDATE game_info SET game_state = %s, player1_ready = %s, " \
                "player2_ready = %s, player3_ready = %s, player4_ready = %s WHERE game_id = %s"
        vals = (game_state, 0, 0, 0, 0, game_number)
        cursor.execute(query, vals)
        cnx.commit()
    finally:
        cnx.close()