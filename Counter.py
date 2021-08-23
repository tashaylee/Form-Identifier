from Url import URL
import csv
import os.path

class Counter:

    def __init__(self):
        self.__all_urls = set()
        self.all_forms_dict = dict()

    def parse_csv(self, file):
        """ cleans up urls in csv file and returns all urls as strings in a set """
        try:
            with open(file + '.csv', mode = "r", encoding = "utf-8-sig") as csv_file:
                csv_reader = csv_file.readlines()

                for line in csv_reader:
                    line = line.strip(',\n')
                    self.__all_urls.add(line)
        except FileNotFoundError as e:
            print('{}\n\nFile name doesnt exist. Restart program with valid csv file.'.format(e))
            quit()
    
    def get_all_urls(self):
        return self.__all_urls

    def set_all_forms_dict(self):
        """ sets dictionary keys to urls; sets values as a dictionary with the 
        form type as keys and form count as values """
        for url in self.__all_urls:
            # set instance
            url = URL(url)
            self.all_forms_dict[url.url_name] = url.forms_dict
    
    def get_all_forms_dict(self):
        """ returns updated dictionary """
        return self.all_forms_dict

    def write_csv(self):
        """ writes content from dictionary into a csv file """
        column_title = ['URL', 'Form Grouping-ID', '# of Times On Page']

        with open('form_counter_dictionary.csv', 'w', newline='') as dict_csv:
            csvwriter = csv.writer(dict_csv, delimiter=',', lineterminator='\r')
            csvwriter.writerow(column_title)
            for url in self.all_forms_dict:
                grouping = ''
                count = 0
                for k,v in self.all_forms_dict[url].items():
                    grouping = k
                    count = v
                csvwriter.writerow([url, grouping, count])
            return dict_csv

    def __repr__(self):
        return('Dictionary of all # of forms on each url: {}'.format(self.all_forms_dict))


if __name__ == '__main__':

    # create instance of counter
    form_counter = Counter()

    # add lines of csv file into instance attr
    form_counter.parse_csv('sitemap_urls')
    
    # checks if parse_csv adds all urls from csv file into a set object
    file = open('sitemap_urls.csv', mode= 'r')
    row_count = sum(1 for row in file)
    file.close()
   
    # checks if get_all_urls returns an updated set
    form_counter.get_all_urls()
    
    # update form dictionary
    form_counter.set_all_forms_dict()
    form_counter.get_all_forms_dict()
    
    form_counter.write_csv()

    print('Counter tests ran successfully. Hooray!')