import requests
from bs4 import BeautifulSoup
import sys

class URL():
    def __init__(self, url):
        self.url_name = url
        self.__all_forms_list = self.__get_all_forms()
        self.forms_dict = dict()
        self.__get_form_num(self.__all_forms_list)
        

    def __get_html(self):
        """ returns the html content from webpage """
        try:
            if self.url_name != '':
                raw_html = requests.get(self.url_name).text
                parsed_html = BeautifulSoup(raw_html, "html.parser")
                return parsed_html
        except requests.exceptions.ConnectionError:
            print('Issues connecting to your internet. Check your wifi.')
            sys.exit()

    """ 
    Extracts all taxi form code attributes from html
    input: a url's html code
    ouput: list of every taxi form on url's code attributes
    """
    def __get_all_forms(self):
        total_forms_list = []
        packages = self.__get_html().find_all('div', id='taxi-form-packages') # find all taxi form packages
        
        for item in packages:
            # remove any forms that are hidden within class: default-form-clone and aside tag
            if not item.find_parents("aside", class_= "floating-cta-wrapper--fixed") and \
            not item.find_parents("div", class_= "default-form-clone"):
                total_forms_list.append(item.select("div > code").pop(-1).get('id'))
        return total_forms_list

    """
    Extracts form grouping and number
    input: list of all form id's
    output: list of all program id's
    """
    def __get_form_num(self, all_forms_list):
        for form in all_forms_list:
            # extract program grouping and id
            single_form = form.split("-")[:3]
            form_name = "-".join(single_form)
            if form_name in self.forms_dict:
                self.forms_dict[form_name] += 1
            else:
                self.forms_dict[form_name] = 1
        return self.forms_dict
    
    def __repr__(self):
        return('URL: {}\n'
                'Forms used on page: {}'.format(self.url_name, self.forms_dict))

if __name__ == '__main__':
    # Tests for webpage with forms
    webpage_with_form = 'https://onlinemba.ucdavis.edu/'
    
    # create url instance
    url_with_form = URL(webpage_with_form)
    print(url_with_form)
