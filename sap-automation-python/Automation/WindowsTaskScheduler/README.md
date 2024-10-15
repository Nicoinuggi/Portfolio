# How to Create a Batch File to Run a Python Script 

To create a batch (.bat) file, follow these steps:

1. Open **Notepad** (or any text editor of your choice).
2. Copy and paste the following code into the editor.
## Batch File Code:

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
