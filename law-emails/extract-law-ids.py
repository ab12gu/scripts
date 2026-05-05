# filename: extract-law-ids.py
# 
# author: Abhay Gupta
# date created: 26-05-03


#
# </tr><tr class="grid-row" onclick="window.location = &#39;LegalDirectory/LegalProfile.aspx?Usr_ID=000000000056&#39;">
#   <td>
#       <ItemTemplate>56</ItemTemplate>
#   </td><td>Robert C.</td><td>Mussehl</td><td>Shoreline</td><td>Emeritus</td><td>(206) 667-8296</td>

from urllib import request 
import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    container = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr": 
            if len(attrs):
                self.container.append(attrs[-1][-1][-13:-1])

    def extract_ids(self):
        print(1)
        #print(self.container)


def extract_ids_alt(url_lawyer_search, url_lawyer_id):
    print(url_lawyer_search)
    print(url_lawyer_id)

    lawyer_search = request.Request(url_lawyer_search)
    lawyer_id = request.Request(url_lawyer_id)

    with request.urlopen(lawyer_search) as f:
        lawyer_search.data = f.read().decode('utf-8')
        print(f.read().decode('utf-8'))

    print(lawyer_search.full_url)
    print(lawyer_search.data)

def extract_ids(url_lawyer_search, url_lawyer_id):
    r = requests.get(url=url_lawyer_search)

    htmlparser = MyHTMLParser()
    htmlparser.add_directory(
    htmlparser.feed(r.text)
    htmlparser.extract_ids()


# when a python module is imported, __name__ is set to the module's name (by defualt its __main__)
if __name__ == '__main__':
    url_lawyer_search = (
        "https://www.mywsba.org/PersonifyEbusiness/LegalDirectory.aspx?"
        "ShowSearchResults=TRUE&"
        "LicenseType=Lawyer&EligibleToPractice=Y&"
        "Status=Activ"
        "e&AreaOfPractice=Personal+Injury"
    )

    url_lawyer_id = (
        "https://www.mywsba.org/PersonifyEbusiness/LegalDirectory/LegalProfile.aspx?"
        "Usr_ID="
    )

    extract_ids(url_lawyer_search, url_lawyer_id)


