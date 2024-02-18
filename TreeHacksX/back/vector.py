import pandas as pd
from sqlalchemy import create_engine, text
from scipy.spatial.distance import cosine
import time
import together
from transcript_analysis.topic_classification import *
from transcript_analysis.sentiment_analysis import *

threshold = 0.5

def create_connection():
    username = 'SUPERUSER'
    password = 'SYS2' # Replace password with password you set
    hostname = 'localhost'
    port = '1972'
    namespace = 'USER'
    CONNECTION_STRING = f"iris://{username}:{password}@{hostname}:{port}/{namespace}"

    engine = create_engine(CONNECTION_STRING)
    conn = engine.connect()
    client = together.Together()
    return client, conn

def insert_users(client, conn):
    # sql = f"""
    # DROP TABLE users
    # """
    # result = conn.execute(text(sql))
    # Load 
    for user_id in range(1, 3):
        # sql = f"""
        # DROP TABLE memory_user{str(user_id)}
        # """
        # result = conn.execute(text(sql))
        sql = f"""
        CREATE TABLE memory_user{str(user_id)} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        value INT,
        topic INT,
        sentiment INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        result = conn.execute(text(sql))

def insert_photos(client, conn, csv_path):

    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Load 
    sql = f"""
    DROP TABLE pictures
    """
    result = conn.execute(text(sql))

    # Load 
    sql = f"""
        CREATE TABLE pictures (
        image_id INT PRIMARY KEY,
        image_link VARCHAR(2000),
        user_id INT,
        description VARCHAR(2000),
        description_vector VECTOR(DOUBLE, 768)
        )
        """
    result = conn.execute(text(sql))

    # Generate embeddings for all descriptions at once. Batch processing makes it faster
    outputs = client.embeddings.create(input=df['description'].tolist(), model='togethercomputer/m2-bert-80M-2k-retrieval')

    # Add the embeddings to the DataFrame
    df['description_vector'] = [outputs.data[i].embedding for i in range(len(df['description']))]

    for index, row in df.iterrows():
        sql = text("""
            INSERT INTO pictures
            (image_id, image_link, user_id, description, description_vector) 
            VALUES (:image_id, :image_link, :user_id, :description, TO_VECTOR(:description_vector))
        """)

        conn.execute(sql, {
            'image_id': row['image_id'], 
            'image_link': row['image_link'],  # Provide actual image data here
            'user_id': row['user'],
            'description': row['description'], 
            'description_vector': str(row['description_vector']), 
        })

    sql = f"""
    SELECT * from pictures
            """
    result = conn.execute(text(sql))
    # print(result.fetchall())


def insert_stat_card_data(conn):

    # Load 
    sql = f"""
    DROP TABLE stat_card_data
    """
    result = conn.execute(text(sql))

    # Load 
    sql = f"""
    CREATE TABLE stat_card_data (
    stat_name TEXT NOT NULL,
    stat_value TEXT NOT NULL,
    change_indicator TEXT NOT NULL
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO stat_card_data (stat_name, stat_value, change_indicator) VALUES
    ('Cognitive Performance Score', '0.76', '-8%'),
    ('Total Memory Cards Attempted', '26', '+7'),
    ('Mood Today', 'Sad', '-1'),
    ('Top Memory Category', 'Family & Relations', '0')
    """
    result = conn.execute(text(sql))


def insert_line_chart_data(conn):

    # Load 
    sql = f"""
    DROP TABLE line_chart_data
    """
    result = conn.execute(text(sql))
    # Load 
    sql = f"""
    CREATE TABLE line_chart_data (
    date TEXT NOT NULL,
    cosine_similarity_score FLOAT
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO line_chart_data (date, cosine_similarity_score) VALUES
    ('Mon, Feb 12', 0.1),
    ('Tue, Feb 13', 0.6),
    ('Wed, Feb 14', 0.3),
    ('Thu, Feb 15', 0.2),
    ('Fri, Feb 16', 0.35),
    ('Sat, Feb 17', 0.15),
    ('Sun, Feb 18', 0.45)
    """
    result = conn.execute(text(sql))


def insert_mood_chart_data(conn):

    # Load 
    sql = f"""
    DROP TABLE mood_chart_data
    """
    result = conn.execute(text(sql))

    # Load 
    sql = f"""
    CREATE TABLE mood_chart_data (
    date TEXT NOT NULL,
    mood INT
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO mood_chart_data (date, mood) VALUES
    ('Mon, Feb 12', -1),
    ('Tue, Feb 13', 0),
    ('Wed, Feb 14', 0),
    ('Thu, Feb 15', 1),
    ('Fri, Feb 16', -1),
    ('Sat, Feb 17', 1),
    ('Sun, Feb 18', 0)
    """
    result = conn.execute(text(sql))


def insert_pie_chart_data(conn):
    
    # Load 
    sql = f"""
    DROP TABLE pie_chart_data
    """
    result = conn.execute(text(sql))
    # Load 
    sql = f"""
    CREATE TABLE pie_chart_data (
    category TEXT NOT NULL,
    value INT,
    fill TEXT NOT NULL
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO pie_chart_data (category, value) VALUES
    ('Health', 27, 'var(--red-7)'),
    ('Family', 46, 'var(--green-7)'),
    ('Retirement', 14, 'var(--purple-7)'),
    ('Hobbies', 13, 'var(--blue-7)'),
    ('Technology', 8, 'var(--yellow-7)'),
    ('Housing', 22, 'var(--pink-7)')
    """
    result = conn.execute(text(sql))


def insert_bar_chart_data(conn):
        
    # Load 
    sql = f"""
    DROP TABLE bar_chart_data
    """
    result = conn.execute(text(sql))

    # Load 
    sql = f"""
    CREATE TABLE bar_chart_data (
    date TEXT NOT NULL,
    remember INT,
    no_remember INT
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO bar_chart_data (date, mood) VALUES
    ('Mon, Feb 12', 12, -4),
    ('Tue, Feb 13', 23, -7),
    ('Wed, Feb 14', 13, -18),
    ('Thu, Feb 15', 15, -9),
    ('Fri, Feb 16', 10, -5),
    ('Sat, Feb 17', 20, -10),
    ('Sun, Feb 18', 15, -5)
    """
    result = conn.execute(text(sql))


def insert_radar_chart_data(conn):
    
    # Load 
    sql = f"""
    DROP TABLE radar_chart_data
    """
    result = conn.execute(text(sql))

    # Load 
    sql = f"""
    CREATE TABLE radar_chart_data (
    topic TEXT NOT NULL,
    value INT,
    fullMark INT
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO radar_chart_data (topic, value, fullMark) VALUES
    ('Health', 83, 150),
    ('Family', 128, 150),
    ('Retirement', 86, 150),
    ('Hobbies', 65, 150),
    ('Technology', 12, 150)
    """
    result = conn.execute(text(sql))


def insert_tabular_data(conn):
    # Load 
    sql = f"""
    DROP TABLE tabular_data
    """
    result = conn.execute(text(sql))
    # Load 
    sql = f"""
    CREATE TABLE tabular_data (
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    interest TEXT NOT NULL
    )
    """
    result = conn.execute(text(sql))

    sql = f"""
    INSERT INTO tabular_data (name, username, interest) VALUES
    ('Brad Pita', 'bradpita', 'Family'),
    ('Scarlet Johamster', 'scarletjohamster', 'Health'),
    ('Leonardo DiCappuccino', 'leonardodicappuccino', 'Retirement'),
    ('Taylor Swiss', 'taylorswiss', 'Hobbies'),
    ('Katy Cherry', 'katycherry', 'Housing'),
    ('Justin Thyme', 'justinthyme', 'Technology'),
    ('Oprah Windfree', 'oprahwindfre', 'Health'),
    ('Johnny Depth', 'johnnydepth', 'Family'),
    ('Harry Stylesheet', 'harrystylesheet', 'Retirement')
    """
    result = conn.execute(text(sql))


def get_photo(conn, user_id):
    sql = text(f"""
    SELECT image_id, image_link FROM pictures 
    WHERE user_id = {user_id}
    LIMIT 1
    """)
    results = conn.execute(sql).fetchall()
    id, link = results[0]
    return { 'id': id, 'link': link }

def check_similarity(client, conn, image_id, description, user_id):

    output = client.embeddings.create(input=[description], model='togethercomputer/m2-bert-80M-2k-retrieval')
    embedding = output.data[0].embedding
    sql = text(f"""
    SELECT description, description_vector FROM pictures 
    WHERE image_id = {image_id}
    """)
    results = conn.execute(sql, {'search_vector': str(embedding)}).fetchall()
    ground_truth = [float(i) for i in str(results[0][1]).split(',')]
    description = results[0][0]
    score = 1 - cosine(ground_truth, embedding)
    print(f"Similarity score: {score}")
    memsql = f"""
    INSERT INTO memory_user{str(user_id)} (value, topic, sentiment) VALUES (:value, :topic, :sentiment);
    """
    topic = topic_classification(description)
    sentiment = sentiment_analysis(description)

    try:
        topicInt = int(topic.strip())
    except:
        topicInt = 0 # in case llm hallucinates
    
    try:
        sentimentInt = int(sentiment.strip())
    except:
        sentimentInt = 0 # in case llm hallucinates
    if score <= threshold:
        print(f"This is below the required threshold to pass, please try again!")
        result = conn.execute(text(memsql), {'value': 0, 'topic': topicInt, 'sentiment': sentimentInt})
        return { 'result': False }

    sql = text(f"""
    SELECT TOP 1 * FROM pictures 
    WHERE user_id != {user_id}
    ORDER BY VECTOR_DOT_PRODUCT(description_vector, TO_VECTOR(:search_vector)) DESC
    """)
    results = conn.execute(sql, {'search_vector': str(embedding)}).fetchall()

    prompt = f"""
    Imagine you are an chat introducer starting off a chat between two seniors, introducing two seniors to each other who share a similar memory. Provide information and guiding questions to help them get to know each other.
    Senior 1 has a memory related to {description}. Senior 2 has a memory related to {results[0][3]}. Think about how to connect these two memories together.
    Now start introducing the 2 seniors, describing them to each other and provide some guiding questions for them (do not include any conversations from the seniors, imagine this is ONLY the first message):
    """

    output = together.Complete.create(
        prompt = prompt,
        model = "meta-llama/Llama-2-70b-chat-hf", 
        max_tokens = 256,
        temperature = 0.8,
        top_k = 60,
        top_p = 0.6,
        repetition_penalty = 1.1,
        stop = ['<human>', '\n\n']
        )

    print(output['output']['choices'][0]['text'])

    result = conn.execute(text(memsql), {'value': 1, 'topic': topicInt, 'sentiment': sentimentInt})


    return {'result': True, 'output': output['output']['choices'][0]['text']}

if __name__ == "__main__":
    client, conn = create_connection()
    insert_photos(client, conn, "data/photos.csv")
    insert_users(client, conn)
    check_similarity(client, conn, 1, "Educational tool for human success", 1)
    check_similarity(client, conn, 1, "Ice skating with my favorite grandchildren", 1)
    sql = text(f"""
    SELECT * from memory_user1
    """)
    results = conn.execute(sql).fetchall()
    print(results)

    