# filename: extract-law-ids.py
# 
# author: Abhay Gupta
# date created: 26-05-03


def extract_ids(url):
    print(url)


# when a python module is imported, __name__ is set to the module's name (by defualt its __main__)
if __name__ == '__main__':
    url = "https://www.mywsba.org/PersonifyEbusiness/LegalDirectory.aspx?"
        "ShowSearchResults=TRUE&"
        "LicenseType=Lawyer&EligibleToPractice=Y"
        "&Status=Activ"
        "e&AreaOfPractice=Personal+Injury""
    extract_ids(url)


