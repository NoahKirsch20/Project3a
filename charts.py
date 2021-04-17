'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal


#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

    api_key = 'GR8VROXU8ASO7XHX'
    base_url = 'https://www.alphavantage.co/query?'
    params = { 'function': time_series,
                'symbol': stock_symbol,
                'interval': '60min',
                'outputsize': 'full',
                'apikey': api_key}
    
    response = requests.get(base_url, params=params)

    if "Error Message" in response.json() :
        print("The server is either down or you provided a ticker symbol that does not exist")
      
    else:

         while check_chart < 1:
        try:
            print("""
            Chart Types
            -------------------
            1. Bar
            2. Line
            """)
            chart_Choice = float(input("Please choose a chart type \n>>>: "))
            if chart_Choice <= 0:
                print("That's not a choice please enter either 1 or 2")
                
            else:
                if chart_Choice > 2:
                    print("That's not a choice please enter either 1 or 2")
                    
                else:
                    check_chart += 1
        except:
            print("That's not a number please choose a number")
            

        #test to print URL
        url = 'https://www.alphavantage.co/query?function=' + time_series + '&symbol=' + stock_symbol + '&interval=' + '30min' + '&apikey=' + api_key
        #JSON Will be conqured
        json_time_seriesDict = { 1: 'Time Series (60min)', 2: 'Time Series (Daily)', 3: 'Weekly Time Series', 4: 'Monthly Time Series'}
        json_response = response.json()
        time_json_object = json_time_seriesDict[time_Choice]

        json_date_key = []
        json_open = []
        json_high = []
        json_low = []
        json_close = []
        #Intraday function
        if time_Choice == 1:
            for date_key in json_response[time_json_object]:
                #real_date_key = datetime.datetime.strptime(date_key,"%Y-%m-%d %H:%M:%S")
            
            
                if date_E_Choice in date_key:

                    json_date_key.append(date_key)
                    
        
                    json_open.append(float(json_response[time_json_object][date_key]["1. open"]))
                    

                    json_high.append(float(json_response[time_json_object][date_key]["2. high"]))
                    
       
                    json_low.append(float(json_response[time_json_object][date_key]["3. low"]))
                    
                    json_close.append(float(json_response[time_json_object][date_key]["4. close"]))
        else:
        
            for date_key in json_response[time_json_object]:
                if time_Choice == 1:
                    real_date_key = datetime.datetime.strptime(date_key,"%Y-%m-%d %H:%M:%S")
                else:
                    real_date_key = datetime.datetime.strptime(date_key,"%Y-%m-%d")
                
                if real_date_key >= begin and real_date_key <= end:

                    json_date_key.append(date_key)
                    
        
                    json_open.append(float(json_response[time_json_object][date_key]["1. open"]))
                    

                    json_high.append(float(json_response[time_json_object][date_key]["2. high"]))
                    
       
                    json_low.append(float(json_response[time_json_object][date_key]["3. low"]))
                    
                    json_close.append(float(json_response[time_json_object][date_key]["4. close"]))
                
        #reverse the list so date can be in chronological order
        json_date_key.reverse()

        beg_date = datetime.datetime.strptime(date_B_Choice,"%Y-%m-%d")
        end_date = datetime.datetime.strptime(date_E_Choice,"%Y-%m-%d")
    
    
