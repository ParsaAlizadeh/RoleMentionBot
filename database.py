import psycopg2.extras


class Database:
    def __init__(self, url):
        self.db = psycopg2.connect(url, sslmode='require', cursor_factory=psycopg2.extras.NamedTupleCursor)

    def init_tables(self):
        cur = self.db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS roletable ("
                    "id SERIAL PRIMARY KEY,"
                    "user_id BIGINT NOT NULL,"
                    "group_id BIGINT NOT NULL,"
                    "role TEXT NOT NULL"
                    ");")
        self.db.commit()

    def select(self, master=True, **kwargs):
        req = "SELECT * FROM roletable WHERE " + " AND ".join(f"{key}=%s" for key in kwargs.keys())
        if not kwargs:
            req = "SELECT * FROM roletable"
        cur = self.db.cursor()
        cur.execute(req, list(kwargs.values()))
        result = cur.fetchall()
        if master:
            result = filter(lambda record: record.user_id != -1, result)
        return list(result)

    def insert(self, user_id, group_id, role):
        cur = self.db.cursor()
        cur.execute("INSERT INTO roletable(user_id, group_id, role) "
                    "VALUES (%s, %s, %s)", (user_id, group_id, role))
        return cur.rowcount

    def delete(self, **kwargs):
        req = "DELETE FROM roletable WHERE " + " AND ".join(f"{key}=%s" for key in kwargs.keys())
        if not kwargs:
            req = "DELETE FROM roletable"
        cur = self.db.cursor()
        cur.execute(req, list(kwargs.values()))
        return cur.rowcount

    def exist(self, group_id, role):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM roletable WHERE group_id=%s AND role=%s", (group_id, role))
        return bool(cur.fetchall())
