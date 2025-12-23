# 📂 Python File Analysis System

Bu proje, belirlenen bir klasör ve alt klasörler içerisindeki dosyaları tarayarak  
dosya bilgilerini **SQLite veritabanına kaydeden** ve bu veriler üzerinde  
**SQL sorguları ile analiz yapılmasını sağlayan** bir **Python CLI uygulamasıdır**.

---

## 🚀 Özellikler

- 📁 Klasör ve alt klasörleri otomatik tarama  
- 💾 Dosya bilgilerini SQLite veritabanına kaydetme  
- 🧠 Dosyaları uzantılarına göre otomatik kategorize etme  
- 🔁 Aynı dosyanın tekrar eklenmesini önleme (UNIQUE kontrolü)  
- 📊 SQL sorguları ile detaylı veri analizi  
- 🖥️ Menü tabanlı kullanıcı arayüzü (CLI)

---

## 🛠️ Kullanılan Teknolojiler

- Python 3  
- SQLite3  
- os modülü  
- SQL  
  - SELECT  
  - INSERT  
  - WHERE  
  - GROUP BY  
  - ORDER BY  
  - LIKE  

---

## ▶️ Kullanım Kılavuzu

### 1️⃣ Klasör Tarama ve Veritabanına Kayıt

Ana programı çalıştırmak için:

```bash
python main.py
```
Program çalıştığında:

- Kullanıcıdan **taranacak klasör yolu** istenir  
  - Örnek: `C:\Users\remzi\test4`

- Belirtilen klasör ve **alt klasörler otomatik olarak taranır**

- Aşağıdaki bilgiler **SQLite veritabanına kaydedilir**:
  - Dosya adı  
  - Uzantı  
  - Dosya boyutu (KB)  
  - Kategori  
  - Klasör yolu  

- Daha önce eklenmiş dosyalar **tekrar eklenmez**


2️⃣ SQL Sorguları ile Veri Analizi
Veritabanı üzerinde analiz yapmak için:

```bash
python queries_sql.py
```
Program çalıştığında aşağıdaki menü görüntülenir:

1 - Tüm dosyaları listele
2 - Kategoriye göre dosya sayısı
3 - En büyük dosyalar
4 - Belirli kategoriye ait dosyalar
5 - Dosya adına göre arama
6 - Belirli boyuttan büyük dosyalar
0 - Çıkış

## 📌 Projenin Amacı

Bu proje;

- Python ile **dosya sistemi işlemlerine hakimiyeti**
- SQLite ile **veritabanı oluşturma ve yönetimini**
- SQL **temel ve orta seviye sorgu bilgisini**
- Menü tabanlı **CLI uygulama geliştirme becerisini**

göstermek amacıyla geliştirilmiştir.
