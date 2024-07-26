import aiosqlite


DATABASE = "db.db"


async def init_db():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS files (
                unique_id TEXT PRIMARY KEY,
                file_id TEXT NOT NULL,
                file_type TEXT NOT NULL
            )
        """)
        await db.commit()


async def add_file(unique_id, file_id, file_type):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("INSERT INTO files (unique_id, file_id, file_type) VALUES (?, ?, ?)", (unique_id, file_id, file_type))
        await db.commit()


async def get_file(unique_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT file_id, file_type FROM files WHERE unique_id = ?", (unique_id,)) as cursor:
            return await cursor.fetchone()
