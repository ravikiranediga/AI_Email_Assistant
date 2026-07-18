import sqlite3

DB_NAME = "emails.db"


def get_connection():

    conn = sqlite3.connect(DB_NAME)

    return conn
def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS emails (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            prompt TEXT NOT NULL,

            tone TEXT NOT NULL,

            generated_email TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conn.commit()

    conn.close()

def save_email(
    prompt,
    tone,
    generated_email
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO emails
        (
            prompt,
            tone,
            generated_email
        )
        VALUES
        (?, ?, ?)
        """,
        (
            prompt,
            tone,
            generated_email
        )
    )

    conn.commit()

    conn.close()
def get_all_emails():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        id,
        prompt,
        tone,
        generated_email,
        created_at
        FROM emails
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
def clear_history():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM emails
        """
    )

    conn.commit()

    conn.close()