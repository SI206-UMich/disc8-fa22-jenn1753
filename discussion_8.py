from bs4 import BeautifulSoup
import requests
import unittest



# Task 2: Look at the Get the URL that links to webpage of universities with Olympic medal wins
# search for the url in the University of Michgian wikipedia page (in the third pargraph of the intro)
# HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
def getLink(soup):
    
    li_list = soup.find_all('a', class_="mw-redirect")
    for li in li_list:
        if "Olympic_medals" in li.get("href", None):
            return "https://en.wikipedia.org" + li.get("href", None)  


# Task 3: Get the details from the box titled "College/school founding". Get all the college/school names and the year they were
# founded and organize the same into key-value pairs.
def getAdmissionsInfo2019(soup):
    d = {}

    table = soup.find('table', class_="toccolours")
    td_list = table.find_all('td')


    td_years_list = table.find_all('td', style="text-align:center;")[1:]
    years = []
    for year in td_years_list:
        year = year.text.strip()
        years.append(year)

    schools = []
    for td in td_list:
        if td not in td_years_list and td != None:
            schools.append(td.text)
    schools = schools[2:]
    
    d = {}
    for index in range(len(schools)):
        d[schools[index]] = years[index]
    
    sorted_d = {}
    for key in sorted(list(d.keys())[2:]):
        sorted_d[key] = d[key]
    return sorted_d


def main():
    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this

    #### YOUR CODE HERE####
    url = 'https://en.wikipedia.org/wiki/University_of_Michigan'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #Call the functions getLink(soup) and getAdmissionsInfo2019(soup) on your soup object.
    getLink(soup)
    getAdmissionsInfo2019(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_link_nobel_laureates(self):
        self.assertEqual(getLink(self.soup), 'https://en.wikipedia.org/wiki/List_of_American_universities_with_Olympic_medals')

    def test_admissions_info(self):
        self.assertEqual(getAdmissionsInfo2019(self.soup), {'Engineering': '1854', 
                                                            'Law': '1859',
                                                            'Dentistry': '1875', 
                                                            'Pharmacy': '1876', 
                                                            'Music, Theatre &Dance': '1880', 
                                                            'Nursing': '1893', 
                                                            'Architecture &Urban Planning': '1906', 
                                                            'Graduate Studies': '1912', 
                                                            'Government': '1914', 'Education': 
                                                            '1921', 'Business': '1924', 
                                                            'Environment andSustainability': '1927', 
                                                            'Public Health': '1941', 
                                                            'Social Work': '1951', 
                                                            'Information': '1969', 
                                                            'Art & Design': '1974', 
                                                            'Kinesiology': '1984'})

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)