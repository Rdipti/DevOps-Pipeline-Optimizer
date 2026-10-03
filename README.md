# DevOps-Pipeline-Performance-Optimizer

I built this personal project to get a better handle on how large-scale infrastructure teams (like the ones at BMW) track their performance. The goal was simple: simulate a high-traffic software environment, find the bottlenecks using SQL, and automate the boring parts of the reporting process.

## Why I built this

I’m interested in the "Software Development Infrastructure" space. I wanted to move beyond just theory and see how Python and SQL actually interact with DevOps tools like Jira or Confluence. This was my way of bridging the gap between data validation (which I’ve done before) and automated infrastructure management.

## What’s inside

- **Pipeline Simulator (`1_simulator.py`)**: A Python script that creates a realistic log of thousands of software builds. It tracks things like how long a build takes and why it might fail.

- **Data Warehouse (`2_sql_analyzer.py`)**: I used SQLite to store and query the logs. This script filters the data to show exactly which parts of the infrastructure are struggling.

- **Reporting Engine (`3_docs_generator.py`)**: This pulls the data and formats it into a summary report. It also includes a logic check that "drafts" a Jira ticket if build times get too high—basically, it flags problems before a human has to go looking for them.

## Getting it running

1. Make sure you have Python 3 installed.

2. Clone this repo to your machine.

3. Run the scripts in order:
   - `python3 1_simulator.py` (to generate the data)
   - `python3 2_sql_analyzer.py` (to run the SQL analysis)
   - `python3 3_docs_generator.py` (to generate the final report)

## Lessons learned

The biggest challenge was handling the data flow between the scripts. I ran into a few "no such table" errors early on, which taught me a lot about how databases need to be initialized before they can be queried. It really gave me a new appreciation for why documentation and structured data are so critical in a fast-moving DevOps environment.
