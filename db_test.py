import helpers.db_helper as db
conn = db.get_db_connection()
if not conn:
    print("Failed to connect")
else:
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cur.fetchall()
    print("Tables:")
    for t in tables:
        print(t[0])
    
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'users'")
    cols = cur.fetchall()
    print("Users columns:")
    for c in cols:
        print(c[0])

    cur.execute("SELECT email, phone, reset_code FROM users LIMIT 5")
    rows = cur.fetchall()
    print("Users data:")
    for r in rows:
        print(r)
