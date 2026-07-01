import sqlite3
import csv

# 1. Connect to a local database (it will create this file automatically)
conn = sqlite3.connect('devops_metrics.db')
cursor = conn.cursor()

# 2. Create a table using SQL
cursor.execute('''
CREATE TABLE IF NOT EXISTS build_logs (
    build_id TEXT, repository_name TEXT, status TEXT, 
    duration_seconds INTEGER, error_type TEXT, timestamp TEXT
)
''')
cursor.execute('DELETE FROM build_logs') # Clear old data if running multiple times

# 3. Load the CSV data into our SQL Database
with open('build_logs.csv', 'r') as file:
    dr = csv.DictReader(file)
    to_db = [(i['build_id'], i['repository_name'], i['status'], i['duration_seconds'], i['error_type'], i['timestamp']) for i in dr]

cursor.executemany("INSERT INTO build_logs VALUES (?, ?, ?, ?, ?, ?);", to_db)
conn.commit()

# 4. Run an advanced SQL Query to find failing repositories
print("🔍 Analyzing Database for Failing Repositories...")
cursor.execute('''
    SELECT repository_name, COUNT(*) as failure_count
    FROM build_logs
    WHERE status = 'Failed'
    GROUP BY repository_name
    ORDER BY failure_count DESC
''')

failing_repos = cursor.fetchall()
for repo in failing_repos:
    print(f"Repository: {repo[0]} | Failures: {repo[1]}")

conn.close()