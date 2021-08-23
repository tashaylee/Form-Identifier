from Counter import Counter

if __name__ == '__main__':
    # create global file name 
    user_input = input('Enter csv file name without .csv at the end: ')
    file = user_input

    print('Extracting data from file.... Please Wait...')

    # create instance of Counter
    form_counter = Counter()
    form_counter.parse_csv(file)
    form_counter.set_all_forms_dict()
    form_counter.write_csv()
    print(form_counter)
    print('Program complete! Open the CSV file "form_counter_dictionary.csv" '
    'to view all urls and the # of leadforms on each url.)')