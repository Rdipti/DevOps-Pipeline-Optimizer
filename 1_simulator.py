import csv
import random
from datetime import datetime, timedelta

# 1. Define our fake data parameters
repos = ['Backend-Auth', 'Payment-Gateway', 'User-Interface', 'Data-Pipeline']
statuses = ['Success', 'Failed', 'Success', 'Success'] # Weighted to succeed more often
error_types = ['None', 'Unit Test Failed', 'Dependency Timeout', 'Syntax Error']

# 2. Create and open a CSV file to write our fake logs
with open('build_logs.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['build_id', 'repository_name', 'status', 'duration_seconds', 'error_type', 'timestamp'])

    # 3. Generate 500 fake records
    for i in range(1, 501):
        repo = random.choice(repos)
        status = random.choice(statuses)
        duration = random.randint(30, 300) # Builds take between 30 and 300 seconds
        error = random.choice(error_types[1:]) if status == 'Failed' else 'None'
        
        # Create a fake timestamp from the last 7 days
        days_ago = random.randint(0, 7)
        timestamp = datetime.now() - timedelta(days=days_ago)
        
        writer.writerow([f"BLD-{1000+i}", repo, status, duration, error, timestamp.strftime("%Y-%m-%d %H:%M:%S")])

print("✅ Success: 'build_logs.csv' generated with 500 records!")