# How to Create a Batch File to Run a Python Script 

To create a batch (.bat) file, follow these steps:

1. Open **Notepad** (or any text editor of your choice).
2. Copy and paste the following code into the editor.
### Batch File Code:
```bat
@echo off
:: Path to your Python script
start /B /wait "" python "C:\Users\SAP_integration.py"
echo Process finished. Closing in...
timeout /t 5
exit
```
3. Save the file with the `.bat` extension (e.g., `run_sap_integration.bat`)
4. **Schedule the Batch File** using **Windows Task Scheduler** to ensure regular updates that align with the Power BI data refresh cycles.

## How to Schedule the Batch File with WTS:
1. Open Windows Task Scheduler.
2. In the right-hand panel, click on Create Basic Task....
3. Give your task a name (e.g., SAP Integration Update).
4. Select the trigger for when you want the task to run.
5. Choose the action Start a Program.
6. In the Program/script field, browse to your .bat file.
7. Set any additional triggers or conditions as needed and click Finish.
