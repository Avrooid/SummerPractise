from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///price.sqlite")
query = '''
    CREATE TABLE price (
        id INTEGER PRIMARY KEY,
        name varchar,
        price integer
    )
'''
with engine.connect() as conn:
    conn.execute(text(query))

queryTwo = '''INSERT INTO price (name, price) VALUES ('test', '1000')'''
with engine.connect() as conn:
    for _ in range(0, 10):
        conn.execute(text(queryTwo))
    conn.commit()
