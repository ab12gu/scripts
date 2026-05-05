# filename: extract-law-ids.py
# 
# author: Abhay Gupta
# date created: 26-05-03

#
# </tr><tr class="grid-row" onclick="window.location = &#39;LegalDirectory/LegalProfile.aspx?Usr_ID=000000000056&#39;">
#   <td>
#       <ItemTemplate>56</ItemTemplate>
#   </td><td>Robert C.</td><td>Mussehl</td><td>Shoreline</td><td>Emeritus</td><td>(206) 667-8296</td>

# <tr>
#    <td><strong>Email:</strong></td>
#    <td><span id="dnn_ctr2977_DNNWebControlContainer_ctl00_lblEmail"><a href='mailto:monte@hesterlawgroup.com' class='link-copy'><span style='type-decoration:underline;'>monte@hesterlawgroup.com</span></a></span></td>
#   </tr>


from urllib import request 
import requests
from html.parser import HTMLParser
import json

class MyHTMLParser(HTMLParser):
    container = []
    html = ""
    url = ""
    text = ""

    def store_url(self, url):
        self.url = url

    def handle_starttag(self, tag, attrs):
        #print(attrs)
        attrs = dict(attrs)
        if 'onclick' in attrs:
            self.container.append(attrs['onclick'][-13:-1])
        """
        if tag == "a": 
            if len(attrs):
               # print(attrs[0])
                if len(attrs[0]):
                    print(attrs[0][1])
                if attrs[0] == 'href':
                    print(attrs)
        if tag == "tr": 
            if len(attrs):
                self.container.append(attrs[-1][-1][-13:-1])
        """

    def extract_ids(self):
        print(1)
        #print(self.container)

    def getHTML(self):
        self.html = requests.get(url=self.url)
        self.text = self.html.text


# when a python module is imported, __name__ is set to the module's name (by defualt its __main__)
if __name__ == '__main__':

    lawyer_ids = []

    lawyer_pages = 162

    url_lawyer_search = (
        "https://www.mywsba.org/PersonifyEbusiness/LegalDirectory.aspx?"
        "ShowSearchResults=TRUE&"
        "LicenseType=Lawyer&EligibleToPractice=Y&"
        "Status=Activ"
        "e&AreaOfPractice=Personal+Injury"
        "&Page="
    )

    url_lawyer_id = (
        "https://www.mywsba.org/PersonifyEbusiness/LegalDirectory/LegalProfile.aspx?"
        "Usr_ID="
    )

    for page in range(lawyer_pages+1):
        url_lawyer_search = url_lawyer_search + str(page)

        htmlparser = MyHTMLParser()
        htmlparser.store_url(url_lawyer_search)
        htmlparser.getHTML()

        htmlparser.feed(htmlparser.text)
        #print(htmlparser.container)
        #lawyer_ids.extend(htmlparser.container)

    print(len(htmlparser.container))
    #print(len(lawyer_ids))
    #print(lawyer_ids)

    with open('lawyer_ids.json', 'w') as f:
        json.dump(htmlparser.container, f)

    #with open('data.json', 'w', encoding='utf-8') as f:
        #json.dump(htmlparser.container, f)

    # with open('data.json', 'wb') as f:
    #with open('data.json', 'w', encoding='utf-8') as f:
        #json.dump(htmlparser.container, f)

    #for ID in htmlparser.container:
        #url = url_lawyer_id + ID
        #print(url)
        #htmlparser.store_url(url)
        #htmlparser.getHTML()

    #htmlparser.feed(htmlparser.text)


### NOT USED 

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



