# filename: extract-law-ids.py
# 
# author: Abhay Gupta
# date created: 26-05-03

############### HTML section for ID
#
# </tr><tr class="grid-row" onclick="window.location = &#39;LegalDirectory/LegalProfile.aspx?Usr_ID=000000000056&#39;">
#   <td>
#       <ItemTemplate>56</ItemTemplate>
#   </td><td>Robert C.</td><td>Mussehl</td><td>Shoreline</td><td>Emeritus</td><td>(206) 667-8296</td>

############### HTML section for Email
# <tr>
#    <td><strong>Email:</strong></td>
#    <td><span id="dnn_ctr2977_DNNWebControlContainer_ctl00_lblEmail"><a href='mailto:monte@hesterlawgroup.com' class='link-copy'><span style='type-decoration:underline;'>monte@hesterlawgroup.com</span></a></span></td>
#   </tr>


from urllib import request 
import requests
from html.parser import HTMLParser
import json


class HTMLParserNames(HTMLParser):
    container = []
    tagfound = False
    emailfound = True
    name = ""
    
    def handle_starttag(self, tag, attrs):
        temp = 'dnn_ctr2977_DNNWebControlContainer_ctl00_lblMemberName'
    
        # Extract NAME tag
        attrs = dict(attrs)
        if 'id' in attrs:
            if temp == attrs['id']:
                self.tagfound = True
        
        # Store name if email exists
        if 'href' in attrs:
            email = attrs['href'].split(":")
            if email[0] == "mailto":
                print(self.name)
                self.container.append(self.name)
    
    # Extract Name
    def handle_data(self, data):
        if self.tagfound == True:
            #print(data)
            self.name = data
            self.tagfound = False

class HTMLParserEmails(HTMLParser):
    container = []
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'href' in attrs:
            email = attrs['href'].split(":")
            if email[0] == "mailto":
                print(email[1])
                self.container.append(email[1])

class HTMLParserIDs(HTMLParser):
    container = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'onclick' in attrs:
            self.container.append(attrs['onclick'][-13:-1])

class Lawyers():
    def parseIDs(self, url, pages):

        for page in range(pages+1):
            urlpage = url + str(page)
            html = requests.get(url=urlpage)
            #print(urlpage)
            htmlparser = HTMLParserIDs()
            htmlparser.feed(html.text)

        print(len(htmlparser.container))

        with open('lawyer_ids.json', 'w') as f:
            json.dump(htmlparser.container, f)

    def parseEmailsNames(self, url, isEmail):

        with open('lawyer_ids.json', 'r') as f:
            lawyer_ids = json.load(f)

        for i, ID in enumerate(lawyer_ids):
            #if i > 4:
                #continue
            url = url_lawyer_id + ID
            html = requests.get(url=url)
            if isEmail:
                htmlparser = HTMLParserEmails()
                outfile = 'lawyer_emails.json'
            else:
                htmlparser = HTMLParserNames()
                outfile = 'lawyer_names.json'
            htmlparser.feed(html.text)
            print(i)

        with open(outfile, 'w') as f:
            json.dump(htmlparser.container, f)


# when a python module is imported, __name__ is set to the module's name (by defualt its __main__)
if __name__ == '__main__':

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

    lawyers = Lawyers()

    #lawyers.parseIDs(url_lawyer_search, lawyer_pages)
    #lawyers.parseEmailsNames(url_lawyer_id, True)
    lawyers.parseEmailsNames(url_lawyer_id, False)
    
"""
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
"""

