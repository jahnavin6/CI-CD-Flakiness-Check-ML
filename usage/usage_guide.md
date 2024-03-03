# Usage Guide for CI-CD-Flakiness-Check-ML

## Getting Your Data Ready

1. Prepare your CSV file with the test execution data. Ensure it has columns for TestID, TestName, ExecutionTime, and Result.
Example format:

    ```
    TestID,TestName,ExecutionTime,Result
    1,LoginTest,0.5,Pass
    2,LogoutTest,0.35,Fail
    3,DataFetchTest,0.4,Pass
    ```

    Save this file in the `data` directory.

## Running the Analysis

2. Execute the analysis script with your CSV file by running:

    ```
    python src/classify_flakiness.py data/your_test_data.csv
    ```
This command analyzes your test data, appending a `Flakiness` column to indicate potential flakiness.

## Visualizing the Results

3. For detailed visualization, open the Jupyter notebook provided:

   ```
    jupyter notebook notebooks/flakiness_analysis.ipynb
   ```

    Run all cells in the notebook to visualize your test data analysis.

## Understanding Your Analysis

- The output CSV and Jupyter notebook visuals will help categorize your tests, showing which might be flaky.
- Use this information to target improvements in your testing process.

For more detailed customization or to add new data sources, you can modify the `classify_flakiness.py` script and the Jupyter notebook as needed.
