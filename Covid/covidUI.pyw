from tkinter import Label, Tk,ttk,Button ,messagebox,Text,END
from threading import Thread
from covid import Covid
import webbrowser
covid = Covid()
main = Tk()
main.title('Covid')
main.geometry('250x200')
main.resizable(False,False)
main.iconbitmap('favicon.ico')
labelTop = Label(main,text = "Choose your country")
labelTop.place(x=5, y=0)
intro = Label(main,text = "Complete medicine for all Corona victims")
intro.place(x=5, y=150)

def github():
    webbrowser.open('https://github.com/ClickCyber')
    
def covids(country):
    DataJson = covid.get_status_by_country_name(country)
    country = DataJson["country"]
    confirmed = DataJson["confirmed"]
    active = DataJson["active"]
    deaths = DataJson["deaths"]
    recovered = DataJson["recovered"]
    last_update = DataJson["last_update"]
    text.delete('1.0', 'end')
    text.insert(END, f'country: {country}\nactive: {active}\ndeaths: {deaths}\nrecovered: {recovered}\nlast update: {last_update}')
        
def Read_Country():
    if comboExample.get() == 'Selecet Country':
        messagebox.showinfo('No Found','Error Selecet Country',icon = 'warning')
    else:
        MsgBox = messagebox.askquestion ('askquestion',f'Are you sure you want to Search the {comboExample.get()}')
        if MsgBox == 'yes':
            text.delete('1.0', 'end')
            text.insert(END, 'start Search')
            Threads = Thread(target=covids, args=(comboExample.get(),))
            Threads.start()

comboExample = ttk.Combobox(main, 
                            values=[
                                    "Selecet Country",
                                    'Israel',
                                    'US',
                                    'Brazil',
                                    'India',
                                    'Russia',
                                    'South Africa',
                                    'Mexico',
                                    'Peru',
                                    'Colombia',
                                    'Chile',
                                    'Iran',
                                    'Spain',
                                    'United Kingdom',
                                    'Saudi Arabia',
                                    'Pakistan',
                                    'Bangladesh',
                                    'Italy',
                                    'Argentina',
                                    'Turkey',
                                    'France',
                                    'Germany',
                                    'Iraq',
                                    'Philippines',
                                    'Indonesia',
                                    'Canada',
                                    'Qatar',
                                    'Kazakhstan',
                                    'Egypt',
                                    'Ecuador',
                                    'Bolivia',
                                    'China',
                                    'Ukraine',
                                    'Sweden',
                                    'Oman',
                                    'Dominican Republic',
                                    'Panama',
                                    'Belgium',
                                    'Kuwait',
                                    'Belarus',
                                    'United Arab Emirates',
                                    'Romania',
                                    'Netherlands',
                                    'Guatemala',
                                    'Singapore',
                                    'Portugal',
                                    'Poland',
                                    'Japan',
                                    'Honduras',
                                    'Nigeria',
                                    'Bahrain',
                                    'Ghana',
                                    'Armenia',
                                    'Kyrgyzstan',
                                    'Afghanistan',
                                    'Switzerland',
                                    'Algeria',
                                    'Azerbaijan',
                                    'Morocco',
                                    'Uzbekistan',
                                    'Serbia',
                                    'Moldova',
                                    'Ireland',
                                    'Kenya',
                                    'Venezuela',
                                    'Costa Rica',
                                    'Nepal',
                                    'Ethiopia',
                                    'Austria',
                                    'Australia',
                                    'El Salvador',
                                    'Czechia',
                                    'Cameroon',
                                    'Cote d\'Ivoire',
                                    'Denmark',
                                    'Korea, South',
                                    'West Bank and Gaza',
                                    'Bosnia and Herzegovina',
                                    'Bulgaria',
                                    'Madagascar',
                                    'Sudan',
                                    'North Macedonia',
                                    'Senegal',
                                    'Kosovo',
                                    'Norway',
                                    'Congo (Kinshasa)',
                                    'Malaysia',
                                    'Zambia',
                                    'Guinea',
                                    'Gabon',
                                    'Tajikistan',
                                    'Haiti',
                                    'Finland',
                                    'Luxembourg',
                                    'Paraguay',
                                    'Mauritania',
                                    'Lebanon',
                                    'Albania',
                                    'Croatia',
                                    'Greece',
                                    'Djibouti',
                                    'Libya',
                                    'Maldives',
                                    'Equatorial Guinea',
                                    'Hungary',
                                    'Malawi',
                                    'Zimbabwe',
                                    'Central African Republic',
                                    'Nicaragua',
                                    'Congo (Brazzaville)',
                                    'Montenegro',
                                    'Thailand',
                                    'Eswatini',
                                    'Somalia',
                                    'Cuba',
                                    'Namibia',
                                    'Cabo Verde',
                                    'Sri Lanka',
                                    'Slovakia',
                                    'Mali',
                                    'South Sudan',
                                    'Suriname',
                                    'Mozambique',
                                    'Lithuania',
                                    'Slovenia',
                                    'Estonia',
                                    'Rwanda',
                                    'Guinea-Bissau',
                                    'Iceland',
                                    'Benin',
                                    'Sierra Leone',
                                    'Yemen',
                                    'Tunisia',
                                    'Angola',
                                    'New Zealand',
                                    'Uruguay',
                                    'Latvia',
                                    'Uganda',
                                    'Jordan',
                                    'Liberia',
                                    'Gambia',
                                    'Cyprus',
                                    'Georgia',
                                    'Syria',
                                    'Burkina Faso',
                                    'Niger',
                                    'Malta',
                                    'Togo',
                                    'Jamaica',
                                    'Andorra',
                                    'Chad',
                                    'Bahamas',
                                    'Sao Tome and Principe',
                                    'Vietnam',
                                    'Botswana',
                                    'Lesotho',
                                    'Diamond Princess',
                                    'San Marino',
                                    'Guyana',
                                    'Tanzania',
                                    'Taiwan*',
                                    'Burundi',
                                    'Comoros',
                                    'Burma',
                                    'Mauritius',
                                    'Mongolia',
                                    'Eritrea',
                                    'Trinidad and Tobago',
                                    'Cambodia',
                                    'Papua New Guinea',
                                    'Belize',
                                    'Brunei',
                                    'Barbados',
                                    'Monaco',
                                    'Seychelles',
                                    'Bhutan',
                                    'Antigua and Barbuda',
                                    'Liechtenstein',
                                    'Saint Vincent and the Grenadines',
                                    'Fiji',
                                    'Saint Lucia',
                                    'Timor-Leste',
                                    'Grenada',
                                    'Laos',
                                    'Dominica',
                                    'Saint Kitts and Nevis',
                                    'Holy See',
                                    'Western Sahara',
                                    'MS Zaandam'])

search = Button(main, text='Search',width='10', command=Read_Country)
ClickMe = Button(main, text='ClickMe ! ',width='10', command=github)
ClickMe.place(x=5,y=170)
exit_Button = Button(main, text='exit ! ',width='10', command=lambda : main.destroy())
exit_Button.place(x=160,y=170)
text = Text(main)
text.place(x=15, y=50,width='220',height='100')
comboExample.place(x=10, y=20,width='225')
comboExample.current(0)
search.place(x=80,y=170)
#print(comboExample.current(), comboExample.get())
main.mainloop()
