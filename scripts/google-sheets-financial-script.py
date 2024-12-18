import gspread
from oauth2client.service_account import ServiceAccountCredentials

def create_google_sheets_financial_projection():
    """
    Create a comprehensive financial projection spreadsheet for S.E.P.T 
    using Google Sheets API.
    
    Prerequisites:
    1. Install required libraries: 
       pip install gspread oauth2client
    2. Set up Google Cloud project and service account
    3. Download service account JSON key
    """
    # Google Sheets API Authentication Setup
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    # Path to your service account credentials JSON file
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'path/to/your/service_account_credentials.json', 
        scope
    )
    client = gspread.authorize(creds)
    
    # Create a new Google Sheet
    spreadsheet = client.create('S.E.P.T Financial Projection')
    
    # Sheets to create
    sheet_names = [
        'Overview', 
        'Revenue Estimates', 
        'Cost Estimates', 
        'Profit Calculations', 
        'Time Estimates', 
        'Data Visualization'
    ]
    
    # Create worksheets
    for name in sheet_names:
        spreadsheet.add_worksheet(title=name, rows=100, cols=20)
    
    # Revenue Estimates Sheet
    revenue_sheet = spreadsheet.worksheet('Revenue Estimates')
    revenue_data = [
        ['Revenue Stream', 'Short-Term (6 months)', 'Long-Term (5 years)'],
        ['Individual Subscriptions', 50000, 600000],
        ['Enterprise Integrations', 20000, 300000],
        ['API Access Fees', 15000, 200000],
        ['Total Revenue', 
         '=SUM(B2:B4)', 
         '=SUM(C2:C4)']
    ]
    revenue_sheet.update('A1:C5', revenue_data)
    
    # Cost Estimates Sheet
    cost_sheet = spreadsheet.worksheet('Cost Estimates')
    cost_data = [
        ['Cost Category', 'Short-Term (6 months)', 'Long-Term (5 years)'],
        ['Development Costs', 100000, 500000],
        ['Marketing Expenses', 30000, 150000],
        ['Operational Costs', 20000, 100000],
        ['Total Costs', 
         '=SUM(B2:B4)', 
         '=SUM(C2:C4)']
    ]
    cost_sheet.update('A1:C5', cost_data)
    
    # Profit Calculations Sheet
    profit_sheet = spreadsheet.worksheet('Profit Calculations')
    profit_data = [
        ['Calculation', 'Short-Term (6 months)', 'Long-Term (5 years)'],
        ['Total Revenue', 
         '=\'Revenue Estimates\'!B5', 
         '=\'Revenue Estimates\'!C5'],
        ['Total Costs', 
         '=\'Cost Estimates\'!B5', 
         '=\'Cost Estimates\'!C5'],
        ['Net Profit', 
         '=B2-B3', 
         '=C2-C3'],
        ['Profit Margin (%)', 
         '=IF(B2<>0, B4/B2*100, 0)', 
         '=IF(C2<>0, C4/C2*100, 0)']
    ]
    profit_sheet.update('A1:C5', profit_data)
    
    # Time Estimates Sheet
    time_sheet = spreadsheet.worksheet('Time Estimates')
    time_data = [
        ['Milestone', 'Short-Term (6 months)', 'Long-Term (5 years)'],
        ['Alpha Launch', 'Month 3', '-'],
        ['Beta Release', 'Month 6', '-'],
        ['Full Product Launch', '-', 'Year 1'],
        ['Enterprise Integration', '-', 'Year 2'],
        ['Global Expansion', '-', 'Year 5']
    ]
    time_sheet.update('A1:C6', time_data)
    
    # Overview Sheet
    overview_sheet = spreadsheet.worksheet('Overview')
    overview_data = [
        ['Key Metrics', 'Short-Term', 'Long-Term'],
        ['Total Revenue', 
         '=\'Revenue Estimates\'!B5', 
         '=\'Revenue Estimates\'!C5'],
        ['Total Costs', 
         '=\'Cost Estimates\'!B5', 
         '=\'Cost Estimates\'!C5'],
        ['Net Profit', 
         '=B2-B3', 
         '=C2-C3'],
        ['Profit Margin (%)', 
         '=IF(B2<>0, B4/B2*100, 0)', 
         '=IF(C2<>0, C4/C2*100, 0)']
    ]
    overview_sheet.update('A1:C5', overview_data)
    
    # Optional: Set up sharing permissions
    spreadsheet.share('your_email@example.com', perm_type='user', role='owner')
    
    print(f"Financial projection spreadsheet created: {spreadsheet.title}")
    print(f"Spreadsheet URL: {spreadsheet.url}")

def main():
    create_google_sheets_financial_projection()

if __name__ == "__main__":
    main()
