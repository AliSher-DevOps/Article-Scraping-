from selenium import webdriver
from csv import reader
import time
import os
from csv import writer
driver=webdriver.Chrome("chromedriver.exe")

print('Enter staring page number:')
starting_index= input()
print('Enter ending page number:')
ending_index= input()


for index2 in range(int(starting_index),int(ending_index)+1):
    url="https://search-beta.abc.net.au/index.html?siteTitle=news#/?query=environment&page="+str(index2)
    try:
        driver.get(url)
        time.sleep(5)
        print("page no:",index2)
        data_list=[]
        for index in range(1,11):
            try:
                title_url ='//*[@id="#content"]/div[1]/section/div/div[2]/div[2]/div[2]/div/ul/li['+str(index)+']/article/div/div[1]/div/a/h2/span'
                desc_url ='//*[@id="#content"]/div[1]/section/div/div[2]/div[2]/div[2]/div/ul/li['+str(index)+']/article/div/div[1]/div/a'
                date_url ='//*[@id="#content"]/div[1]/section/div/div[2]/div[2]/div[2]/div/ul/li['+str(index)+']/article/div/div[1]/div/time[1]'
                aurthor_url ='//*[@id="#content"]/div[1]/section/div/div[2]/div[2]/div[2]/div/ul/li['+str(index)+']/article/div/div[1]/div/span'

                title_row1=driver.find_element_by_xpath(title_url)
                title = title_row1.text
                data_list.append(title)
                aurthor_row1=driver.find_element_by_xpath(aurthor_url)
                aurthor = aurthor_row1.text
                data_list.append(aurthor)
                date_row1=driver.find_element_by_xpath(date_url)
                date = date_row1.text
                data_list.append(date)
                
                driver.find_element_by_xpath(desc_url).click()
                desc = driver.find_element_by_xpath('//*[@id="body"]/div').text
                data_list.append(desc)
                driver.get(url)
                time.sleep(5)
            except:
                pass
            try:
                with open('data.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(data_list)
                    f_object.close()
            except:
                    print("data file is open please close csv file")
            data_list=[]
    except:
        print("invalid starting and ending index please visit website and enter correct index")