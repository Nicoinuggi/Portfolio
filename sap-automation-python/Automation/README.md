Para crear un archivo Bat, puedes crear un bloc de notas y guardarlo con extension ".bat" y luego para llamar a tu codigo de python puedes poner lo siguiente:

@echo off
:: Path to your python script 
start /B /wait "" python "C:\Users\SAP_integration.py"
echo Proceso finalizado.Cerrando en...
timeout /t 5
exit

