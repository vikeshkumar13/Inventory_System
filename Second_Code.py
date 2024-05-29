from openpyexcel import load_workbook
import pandas as pd


def Inventory():
    filename = 'database.xlsx'
    wb = load_workbook(filename=filename)
    ws = wb['Sheet1']

    desc = input('enter description of the details->')
    amount = float(input('amount->'))
    payment_mode = input('payment_mode->')
    mode_name = input('mode_name->')

    ws.cell(column=1, row=1, value='Description')
    ws.cell(column=2, row=1, value='Amount')
    ws.cell(column=3, row=1, value='Payment_mode')
    ws.cell(column=4, row=1, value='payment_mode_name')

    last_row = ws.max_row + 1
    ws.cell(column=1, row=last_row, value=desc)
    ws.cell(column=2, row=last_row, value=amount)
    ws.cell(column=3, row=last_row, value=payment_mode)
    ws.cell(column=4, row=last_row, value=mode_name)
    wb.save(filename)
    wb.close()


def milk_calculation():
    per_liter = 63
    filename = 'database.xlsx'
    wb = load_workbook(filename=filename)
    ws = wb['Sheet2']
    ws.cell(column=1, row=1, value="Liters_total")
    ws.cell(column=2, row=1, value="days")
    ws.cell(column=3, row=1, value="total_liters")
    ws.cell(column=4, row=1, value="price")
    ws.cell(column=5, row=1, value="TOTAL_AMOUNT")

    liter = float(input('Enter Liter->'))
    days = int(input('Enter days->'))
    total_liters_per_day = liter * days
    price_per_liter = total_liters_per_day * per_liter
    last_row = ws.max_row + 1
    ws.cell(column=1, row=last_row, value=liter)
    ws.cell(column=2, row=last_row, value=days)
    ws.cell(column=3, row=last_row, value=total_liters_per_day)
    ws.cell(column=4, row=last_row, value=price_per_liter)
    wb.save(filename)
    wb.close()


def display_inventory():
    df = pd.read_excel('database.xlsx', sheet_name='Sheet1')
    print(df)
    total = df['Amount'].sum()
    print('Total ->', total)


def display_milk():
    df = pd.read_excel('database.xlsx', sheet_name='Sheet2')
    print(df)
    total = df['price'].sum()
    print('total amount->', total)


def delete_row():
    filename = 'database.xlsx'
    wb = load_workbook(filename=filename)
    ws = wb['Sheet1']
    ws1 = wb['Sheet2']
    ws.delete_rows(2, 50)
    ws1.delete_rows(2, 50)
    print('data deleted')
    wb.save(filename)
    wb.close()