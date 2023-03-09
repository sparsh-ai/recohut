import re
import json
import os

# definition of some reserved words
reserved_words = [
    "Calle",
]

addresses = [
    "Winterallee 3",
    "Musterstrasse 45",
    "Blaufeldweg 123B",
    "Am Bächle 23",
    "Auf der Vogelwiese 23 b",
    "4, rue de la revolution",
    "200 Broadway Av",
    "Calle Aduana, 29",
    "Calle 39 No 1540",
    "Av Calle 39 No 1540",
    "201 Main st"
]


def check_reserved_word(chunks):
    #This function looks for the reserved words 
    #and takes the next chunk as the street_name
    #all after the reverded_word+1 is housenumber
    for i in range(len(chunks)):
        for j in range(len(reserved_words)):
            if chunks[i] == reserved_words[j]:
                street_name = ' '.join(
                    chunks[0: i + 2])
                del chunks[0: i + 2]
                house_number = ' '.join(chunks[0: len(chunks)])
                complete_address = {'street': street_name, 'housenumber': house_number}
                return complete_address

    return False


def start_with_number(chunks):
    #This function evaluates if the first chunk contains numbers 
    #if yes, it's the house_number and all other chunks
    #correspond to the street_name
    check = bool(re.search(r'\d', chunks[0]))
    if check:
        street_name = ' '.join(chunks[1: len(chunks)])
        house_number = chunks[0]
        complete_address = {'street': street_name, 'housenumber': house_number}
    else:
        return False
    return complete_address


def start_with_name(chunks):
    # This function finds the chunks that contains number
    # to take it as the house_number, all other chunks
    # correspond to the street_name
    for i in range(len(chunks)):
        if bool(re.search(r'\d', chunks[i])):
            street_name = ' '.join(chunks[0: i])
            house_number = ' '.join(chunks[i: len(chunks)])
            complete_address = {'street': street_name, 'housenumber': house_number}
            return complete_address
    return False

if __name__ == '__main__':

    lst_address = []

    for address in addresses:

        address = address.replace(",", "")
        address_in_chunks = address.split(' ')
        complete_address = check_reserved_word(address_in_chunks)

        if complete_address is not False:
            lst_address.append(complete_address)
        else:
            complete_address = start_with_number(address_in_chunks)
            if complete_address is not False:
                lst_address.append(complete_address)
            else:
                complete_address = start_with_name(address_in_chunks)
                lst_address.append(complete_address)

    # Save and print final JSON with addresses
    json_object = json.dumps(lst_address, ensure_ascii=False, indent=4)
   
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    with open(dir_path+'/json_data.json', 'w') as out_file:
        print(json_object, file=out_file)
    print(json_object)
