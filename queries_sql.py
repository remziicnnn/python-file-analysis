import sqlite3


def get_connection(db_name="file_analysis.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


# ---------- SQL FONKSİYONLARI ----------

def get_all_files(cursor):
    cursor.execute("SELECT * FROM files")
    return cursor.fetchall()


def count_files_by_category(cursor):
    cursor.execute("""
        SELECT category, COUNT(*)
        FROM files
        GROUP BY category
    """)
    return cursor.fetchall()


def get_largest_files(cursor, limit=5):
    cursor.execute("""
        SELECT file_name, extension, size_kb
        FROM files
        ORDER BY size_kb DESC
        LIMIT ?
    """, (limit,))
    return cursor.fetchall()


def get_files_by_category(cursor, category):
    cursor.execute("""
        SELECT file_name, extension, size_kb
        FROM files
        WHERE category = ?
    """, (category.upper(),))
    return cursor.fetchall()


def search_files_by_name(cursor, keyword):
    cursor.execute("""
        SELECT file_name, extension, size_kb
        FROM files
        WHERE file_name LIKE ?
    """, (f"%{keyword}%",))
    return cursor.fetchall()


def get_files_larger_than(cursor, min_size_kb):
    cursor.execute("""
        SELECT file_name, extension, size_kb
        FROM files
        WHERE size_kb > ?
        ORDER BY size_kb DESC
    """, (min_size_kb,))
    return cursor.fetchall()


# ---------- YAZDIRMA ----------

def print_results(title, rows):
    print(f"\n=== {title} ===")
    if not rows:
        print("Kayıt bulunamadı.")
    for row in rows:
        print(row)


# ---------- MENÜ ----------

def show_menu():
    print("\n=== FILE ANALYSIS MENU ===")
    print("1 - Tüm dosyaları listele")
    print("2 - Kategoriye göre dosya sayısı")
    print("3 - En büyük dosyalar")
    print("4 - Belirli kategoriye ait dosyalar")
    print("5 - Dosya adına göre arama")
    print("6 - Belirli boyuttan büyük dosyalar")
    print("0 - Çıkış")


def get_user_choice():
    return input("Seçiminizi girin: ")


def run_menu():
    conn, cursor = get_connection()

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            print_results("All Files", get_all_files(cursor))

        elif choice == "2":
            print_results("Files Count by Category", count_files_by_category(cursor))

        elif choice == "3":
            limit = input("Kaç dosya listelensin? (default 5): ")
            limit = int(limit) if limit.isdigit() else 5
            print_results("Largest Files", get_largest_files(cursor, limit))

        elif choice == "4":
            category = input("Kategori adını girin (IMAGES, PDF, DOCS, ...): ")
            print_results(
                f"Files in category: {category}",
                get_files_by_category(cursor, category)
            )

        elif choice == "5":
            keyword = input("Aranacak kelimeyi girin: ")
            print_results(
                f"Search results for: {keyword}",
                search_files_by_name(cursor, keyword)
            )

        elif choice == "6":
            min_size = input("Minimum dosya boyutu (KB): ")
            if min_size.isdigit():
                print_results(
                    f"{min_size} KB'den büyük dosyalar",
                    get_files_larger_than(cursor, float(min_size))
                )
            else:
                print("Geçersiz boyut!")

        elif choice == "0":
            print("Programdan çıkılıyor 👋")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin!")

    conn.close()


if __name__ == "__main__":
    run_menu()
