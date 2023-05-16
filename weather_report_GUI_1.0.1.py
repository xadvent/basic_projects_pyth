import requests, json, os
import tkinter as f
os.system('cls' if os.name == 'nt' else 'clear')


information_all = []    #   list to hold request.get()

def get_entry_value():
    entry_input = entry.get().lower()
    print("this is what you entered: ", entry_input)

    base_url = 'http://api.weatherstack.com/current'
    api_key = '?access_key=37ab9bf82b0317cb9724abca5e72f301'
    query = f'&query={entry_input.lower()}'
    whole_url = base_url + api_key + query
    try: 
        webpage = requests.get(whole_url)
        if webpage.status_code == 200:
            data = webpage.json()
            current = data['current']
            input_city()
            generate_temp(current)                 #   Running into issues - probably with .json and how it's pulling the information
            generate_description(current)  
            generate_feelslike(current)        #   Probably the same thing
        else: 
            entry.delete(0, f.END)
            entry.insert(0, "Error in Get Request")
    except requests.exceptions.ConnectionError:
        entry.delete(0, f.END)
        entry.insert(0, "Connection Failed...")
    except:
        entry.delete(0, f.END)
        entry.insert(0, 'City not Found...')



def input_city():
    string = entry.get()
    capitalized_string = string.capitalize()
    city_placeholder.config(text=capitalized_string)

def generate_temp(current):
    temp = current["temperature"]
    if temp == '':
        entry.delete(0, f.END)
        entry.insert(0, 'Not Found')
    else:
        temperature_placeholder.config(text=f'{temp}°C')
    

def generate_description(current):
    description = current['weather_descriptions']
    description_placeholder.config(text=f'{description}')


def generate_feelslike(current):
    feelslike = current['feelslike']
    feelslike_placeholder.config(text=feelslike)







window = f.Tk()                         #   Creating Window
window.rowconfigure([0,1,2,3,4,5], minsize=30, weight=1)
window.columnconfigure([0,1,2,3], minsize=30, weight=1)
window.config(bg='black')

frame1 = f.Frame(master=window, height=30, bg='black')
frame1.grid(row=0, rowspan=5)





greeting = f.Label(master=window,       #   Window Title
    text='Weather App',
    background='black',
    foreground='white',
    )
greeting.grid(row=0,column=0,columnspan=4)


city_listing = f.Label(master=window, fg='white', bg='black', text='City: ')
city_listing.grid(row=1, column=0)
city_placeholder = f.Label(master=window, fg='white', bg='black', text='NA')
city_placeholder.grid(row=1, column=1, columnspan=2)


temperature_listing = f.Label(master=window, fg='white', bg='black', text='Temperature: ')
temperature_listing.grid(row=2,column=0)
temperature_placeholder = f.Label(master=window, fg='white', bg='black', text='NA')
temperature_placeholder.grid(row=2, column=1, columnspan=2)


description_listing = f.Label(master=window, fg='white', bg='black', text='Description: ')
description_listing.grid(row=3, column=0)
description_placeholder = f.Label(master=window, fg='white',bg='black', text='NA')
description_placeholder.grid(row=3, column=1, columnspan=2)


feelslike_listing = f.Label(master=window, fg='white', bg='black', text='Feels like: ')
feelslike_listing.grid(row=4, column=0)
feelslike_placeholder = f.Label(master=window, fg='white', bg='black', text='NA')
feelslike_placeholder.grid(row=4, column=1, columnspan=2)




button = f.Button(master=window, fg='white', bg='black', text=':)', command=get_entry_value)
button.grid(row=5, column=2)

entry =f.Entry(master=window, fg='white', bg='grey', text='Type Here')
entry.grid(row=5, column=1)            #    Inputting Country

asking = f.Label(master=window, fg='white', bg='black', text='Enter City:')
asking.grid(row=5, column=0)

information_button = f.Label(master=window, text='Click to Confirm', fg='white', bg='black')
information_button.grid(row=5, column=3)   #    How to







window.mainloop()


