import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect("olympics2.db")
c = conn.cursor()

# Топ N спортсменов по числу медалей
top_n_athletes = 10
c.execute(f"""
SELECT
    athletes.name,
    COUNT(DISTINCT medals.medal) AS medal_count
FROM
    athletes
JOIN
    medals ON athletes.athlete_id = medals.athlete_id
GROUP BY
    athletes.name
ORDER BY
    medal_count DESC
LIMIT
    {top_n_athletes}
""")
print("Топ", top_n_athletes, "спортсменов по числу медалей:")
for row in c.fetchall():
    print(f"{row[0]}: {row[1]}")

# Топ N стран по числу медалей
top_n_countries = 10
c.execute(f"""
SELECT
    countries.name,
    COUNT(DISTINCT medals.medal) AS medal_count
FROM
    countries
JOIN
    athletes ON countries.country_id = athletes.country_id
JOIN
    medals ON athletes.athlete_id = medals.athlete_id
GROUP BY
    countries.name
ORDER BY
    medal_count DESC
LIMIT
    {top_n_countries}
""")
print("Топ", top_n_countries, "стран по числу медалей:")
for row in c.fetchall():
    print(f"{row[0]}: {row[1]}")

# Спортсмены с группировкой по странам
c.execute("""
SELECT
    countries.name,
    athletes.name
FROM
    countries
JOIN
    athletes ON countries.country_id = athletes.country_id
ORDER BY
    countries.name,
    athletes.name
""")
print("Спортсмены с группировкой по странам:")
for row in c.fetchall():
    print(f"{row[0]}: {row[1]}")

# Спортсмены с группировкой по видам спорта
c.execute("""
SELECT
    sports.name,
    athletes.name
FROM
    sports
JOIN
    athletes ON sports.sport_id = athletes.sport_id
ORDER BY
    sports.name,
    athletes.name
""")
print("Спортсмены с группировкой по видам спорта:")
for row in c.fetchall():
    print(f"{row[0]}: {row[1]}")

conn.close()
