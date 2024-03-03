# CI-CD-Flakiness-Check-ML
# Data Format

Each CSV file should contain test execution records with the following columns:
- TestID: Unique identifier for the test
- TestName: Name of the test
- ExecutionTime: Time taken for the test to execute (optional for flakiness analysis)

Example:
TestID,TestName,ExecutionTime
- 1,LoginTest,0.5
- 2,SignupTest,0.7

