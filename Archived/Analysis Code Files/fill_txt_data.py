# fill_txt_data.py
# Fill the txt file for the days races via web automation.

# Imports.
import datetime
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
import html2text

def extract_html(total_races, i):
    """ Parse the HTML into text. """
    filename = open("Future Race Data/file.html", 'r').read()

    h = html2text.HTML2Text()
    h.ignore_links = True
    soup = BeautifulSoup(filename, 'html.parser')

    main_text = soup.get_text()

    final_text = BeautifulSoup(main_text, 'html.parser')

    with open('Future Race Data/filea' + str(i) + '.txt', 'w') as out_txt_f:
        out_txt_f.write(final_text.get_text())
    
    sec_filename = open("Future Race Data/filea" + str(i) + ".txt", 'r').read()

    with open('Future Race Data/fileb' + str(i) + '.txt', 'w') as out_txt_b:
        out_txt_b.write(h.handle(sec_filename))


def web_extract(meeting, total_races):
    """ Fill text files using web extraction - automating fills. """
    current = datetime.datetime.today()
    year = current.year
    month = current.month

    day = '11'

    if month < 10: 
        month = '0' + str(month)
    #day = current.day
    #if day < 10: 
    #    day = '0' + str(day)

    driver = webdriver.Chrome()

    link_a = "https://new.tab.co.nz/extended-form/"
    date = ("{}-{}-{}".format(year, month, day))

    for i in range(1, total_races + 1):
        url = link_a + date + '-m' + str(meeting) + '-r' + str(i)
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div/div/main/div[2]/div[2]/div[1]/div[1]/span[6]/a').click()
        
        time.sleep(1)

        current_URL = driver.current_url
        print(current_URL)
        data = requests.get(current_URL)

        with open('Future Race Data/file.html', 'w') as out_html_f:
            out_html_f.write(str(data.text.encode('utf-8')))
        
        extract_html(total_races, i)



