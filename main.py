import sqlite3
import os


def create_database(db_name="file_analysis.db"):
    conn = sqlite3.connect(db_name)
    return conn


def create_tables(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            file_name TEXT NOT NULL,
            extension TEXT,
            size_kb FLOAT,
            category TEXT,
            folder_path TEXT,
            scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE (file_name, extension, folder_path)
        )
    ''')


def get_category(extension):
    ext_map = {
        ".jpg": "IMAGES",
        ".jpeg": "IMAGES",
        ".png": "IMAGES",
        ".gif": "IMAGES",

        ".pdf": "PDF",
        ".doc": "DOCS",
        ".docx": "DOCS",
        ".txt": "TEXT",

        ".mp3": "MUSIC",
        ".wav": "MUSIC",

        ".mp4": "VIDEOS",
        ".mkv": "VIDEOS",

        ".py": "PYTHON",
        ".ipynb": "NOTEBOOKS"
    }
    return ext_map.get(extension.lower(), "OTHER")


def insert_file(cursor, file_name, extension, size_kb, category, folder_path):
    cursor.execute('''
        INSERT INTO files (file_name, extension, size_kb, category, folder_path)
        VALUES (?, ?, ?, ?, ?)
    ''', (file_name, extension, size_kb, category, folder_path))


def file_exists(cursor, file_name, extension, folder_path):
    cursor.execute("""
        SELECT 1 FROM files
        WHERE file_name = ? AND extension = ? AND folder_path = ?
    """, (file_name, extension, folder_path))

    return cursor.fetchone() is not None


def scan_folder_and_insert(cursor, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)

            file_name, extension = os.path.splitext(file)
            size_kb = round(os.path.getsize(full_path) / 1024, 2)
            category = get_category(extension).upper()

            if file_exists(cursor, file_name, extension, root):
                print(f"Zaten var, atlandı → {file}")
                continue

            insert_file(
                cursor,
                file_name,
                extension,
                size_kb,
                category,
                root
            )

            print(f"Eklendi → {file}")


def main():
    conn = create_database()
    cursor = conn.cursor()

    try:
        create_tables(cursor)
        folder_to_scan = input("Taranacak klasör yolunu girin: ")
        scan_folder_and_insert(cursor, folder_to_scan)
        conn.commit()
        print("Dosyalar başarıyla eklendi ✅")

    except Exception as e:
        print("Hata:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
