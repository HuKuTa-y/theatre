from database import DatabaseConfig, DatabaseConnection


class MigrationManager:

    def __init__(self, config: DatabaseConfig):
        self.config = config
        self.connection = DatabaseConnection(self.config)

    def create_tables(self):
        # Initialize
        conn = self.connection.get_connection()
        cursor = conn.cursor()

        # Execution
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS category(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        content TEXT NOT NULL
                        )
            ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subsections(
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(100) NOT NULL,
                       content TEXT NOT NULL,
                       link VARCHAR(255) NOT NULL
                       )
            ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sources(
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(100) NOT NULL,
                       link VARCHAR(255) NOT NULL
                       )
            ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(100) NOT NULL,
                       id_chat DECIMAL(10, 0)
                       )
            ''')
        
        conn.commit()

        # Deinitialize
        cursor.close()
        conn.close()