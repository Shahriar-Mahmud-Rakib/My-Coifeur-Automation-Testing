import helpers.db_helper as db
conn = db.get_db_connection()
if conn:
    cur = conn.cursor()
    cur.execute("SELECT email, phone, type_user, reset_code FROM users WHERE email='amrmuhamed9@gmail.com' OR email='test19@example.com' OR email='aalih.aaa986@gmail.com' OR phone='966512345600'")
    print(cur.fetchall())
    
    cur.execute("SELECT COUNT(*) FROM users")
    print("Total users:", cur.fetchone()[0])
