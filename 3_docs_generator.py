import sqlite3

conn = sqlite3.connect('devops_metrics.db')
cursor = conn.cursor()

# Get average build times
cursor.execute('SELECT repository_name, AVG(duration_seconds) FROM build_logs GROUP BY repository_name')
avg_times = cursor.fetchall()

# Generate a Markdown Document (Simulating Confluence)
with open('Weekly_Infrastructure_Report.md', 'w') as f:
    f.write("# 📊 Weekly DevOps Infrastructure Report\n\n")
    f.write("### Average Build Latency per Repository\n")
    for repo in avg_times:
        f.write(f"- **{repo[0]}**: {round(repo[1], 2)} seconds\n")

print("✅ Confluence-style Markdown report generated: 'Weekly_Infrastructure_Report.md'")

# Simulate creating a Jira Ticket for the slowest repo
slowest_repo = max(avg_times, key=lambda x: x[1])
if slowest_repo[1] > 150: # Threshold for a "slow" build
    print(f"\n🚨 JIRA TICKET AUTO-DRAFTED 🚨")
    print(f"Title: [PERFORMANCE] Investigate slow build times in {slowest_repo[0]}")
    print(f"Description: The average build time has exceeded 150 seconds (Current: {round(slowest_repo[1], 2)}s). Please optimize pipeline cache.")

conn.close()