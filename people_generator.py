import random, json, os
from customer import Customer

errLoc = []

def nameLength():
    '''
    nameLength

    Randomly generates a number between 0 and 99. Uses this to produce a name length.
    Probabilities are weighted, with medium lengths (4-7 letters) being most likely.
    Minimum length is 3, maximum is 10.

    Returns an int.

    '''
    rand = round(random.random() * 99)
    if rand < 10:
        return 3
    elif rand < 25:
        return 4
    elif rand < 45:
        return 5
    elif rand < 62:
        return 6
    elif rand < 75:
        return 7
    elif rand < 85:
        return 8
    elif rand < 94:
        return 9
    elif rand < 100:
        return 10

def allConsonants(string):
    '''
    allConsonants
    
    Checks a given string for vowel characters.

    Returns False if a vowel is found. Returns True otherwise.

    '''
    vowels = ['a','e','i','o','u']
    for char in string:
        if char in vowels:
            # loop ends because something is being returned
            return False
    return True

def nameGenerator():
    '''
    nameGenerator

    Randomly generates a string of characters. Probabilities are weighted based on
    analysis of the frequency of the occurrence of letters of the English alphabet.
    The function imports json object as a reference for this data.

    Returns a string consisting of English letters and exactly one space ("Firstname Lastname").

    '''
    # create json object from file
    with open("letters.json", "r") as f:
        json_obj = json.load(f)
    alphabet = []
    startfreq = []

    # place data into lists to be read by random.choices() function later
    for elem in json_obj["letter frequencies"]:
        alphabet.append(elem["letter"])
        startfreq.append(elem["frequency"])
    
    # generate first name
    fcount = 0
    while True:
        # generate length
        flength = nameLength()
        # choose starting letter based on known frequency
        fname = random.choices(alphabet, weights=startfreq, k=1)[0]
        i = 1
        while i < flength:
            # produce lists for bigram frequency
            idx = alphabet.index(fname[i-1])
            alph = []
            freq = []
            for elem in json_obj["letter frequencies"][idx]["bigram frequency"]:
                alph.append(elem['letter'])
                freq.append(elem['frequency'])
            fname += random.choices(alph, weights=freq, k=1)[0]
            i += 1
        
        # Check for pronounceability:
            # This is done in a very restrained manner--all substrings of length 5
            # of the name string are checked for vowels. If there is a substring of
            # length 5 with no vowels, the name is rejected.
        cond = False
        for m in range(flength):
            idx = m+4
            if flength - m < 5:
                idx = -1
            if allConsonants(fname[m:idx].lower()):
                cond = True
                break
            if flength - m <= 5:
                break
        if cond:
            fcount += 1
            if fcount == 0:
                print("Unpronounceable name rejected...")
            else:
                # print number of times a name was rejected
                print(f"Unpronounceable name rejected (x{fcount})...")
            continue
        break
    
    # generate last name
    lcount = 0
    while True:
        # generate length 
        llength = nameLength()
        # choose starting letter based on known frequency
        lname = random.choices(alphabet, weights=startfreq, k=1)[0]
        j = 1
        while j < llength:
            # produce lists for bigram frequency
            idx = alphabet.index(lname[j-1])
            alph = []
            freq = []
            for elem in json_obj["letter frequencies"][idx]["bigram frequency"]:
                alph.append(elem['letter'])
                freq.append(elem['frequency'])
            lname += random.choices(alph, weights=freq, k=1)[0]
            j += 1
        
        # Check for pronounceability:
            # This is done in a very restrained manner--all substrings of length 5
            # of the name string are checked for vowels. If there is a substring of
            # length 5 with no vowels, the name is rejected.
        cond = False
        for l in range(flength):
            idx = l+4
            if flength-l < 5:
                idx = -1
            if allConsonants(fname[l:idx].lower()):
                cond = True
                break
            if flength-l <= 5:
                break
        if cond:
            lcount += 1
            if lcount == 0:
                print("Unpronounceable name rejected...")
            else:
                # print number of times a name was rejected
                print(f"Unpronounceable name rejected (x{lcount})...")
            continue
        break
    # format name strings, combine them to be returned
    name = fname.capitalize() + " " + lname.capitalize()
    return name

def locationGenerator():
    '''
    locationGenerator

    Reads from a csv file and selects an entry at random. The data is
    loaded into lists from the file, then an index integer is randomly
    generated. The record at that index is then selected. The record is
    then seperated into a tuple. There is a small random chance that
    components of the tuple may be intentionally (minorly) corrupted.

    Returns a tuple containing 2 strings (city, country)

    '''
    # set err variable to false by default
    err = False
    # initialize lists for random selection
    locs = []
    cities = []
    countries = []
    vals = []
    # read from file to populate lists
    with open("bigcities.csv",'r',encoding="utf8") as f:
        for line in f:
            line = line.strip()
            data = line.split(", ")
            # weigh cities heavily by population by squaring
            if data[1] == 'United States':
                # give extra weight to US cities (for more familiarity)
                weight = 10 * (int(data[2]) ** 2)
            else:
                weight = int(data[2]) ** 2
            cities.append(data[0])
            countries.append(data[1])
            locs.append((data[0], data[1]))
            vals.append(weight)
    if random.random() < 0.01:
        # create ~1% random chance that the country name will be inaccurate
        city = random.choices(cities, weights=vals,k=1)[0]
        country = random.choice(countries)
        loc = (city, country)
        err = True
    else:
        # otherwise, city/country chosen as pair at random
        loc = random.choices(locs, weights=vals,k=1)[0]
    rand = random.random()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if rand < 0.01:
        # Create 1% chance that location will be misspelled
        err = True
        # randomly choose city or country
        c = random.randint(0,1)
        # randomly choose which character to change
        idx = random.randint(0, len(loc[c]) - 1)
        name_new = ""
        for i in range(len(loc[c])):
            if i == idx:
                while True:
                    new_char = random.choice(alphabet)
                    if loc[c][i] == new_char:
                        continue
                    break
                name_new += new_char
            else:
                name_new += loc[c][i]
        if c == 0:
            loc = (name_new, loc[1])
        elif c == 1:
            loc = (loc[0], name_new)
    # if location has a mistake, add to list
    if err:
        errLoc.append(loc)
    return loc

def main():
    # initialize lists
    customers = []
    rmSpace = []
    errChar = []
    # initialize index
    i = 0
    while i < 1000:
        rand = random.random()
        # generate name
        name = nameGenerator()
        # Create ~1% chance that firstname and lastname are not separated by space
        if rand < 0.01:
            fname = name.split(" ")[0].strip(" ")
            lname = name.split(" ")[1].strip(" ")
            rmSpace.append(i+1)
            name = fname + lname
        # Create ~1% chance that an erroneous character exists in the name string
        elif rand < 0.02:
            invalid_chars = ['0','1','2','3','4','5','6','7','8','9','!','@','$','%','^','&','*','(',')','~','`','"',"'",'?','|','/','.','-','_','+',':',';','<','>']
            new_name = ""
            val = False
            for char in name:
                new_name += char
                # Create 10% chance that a character will be preceded by an erroneous character
                if random.random() < 0.1:
                    val = True
                    new_name += random.choices(invalid_chars, k=1)[0]
                    new_name += char
            if val:
                # append to list if erroneous for later verification
                errChar.append(i+1)
            name = new_name
        # generate location
        loc = locationGenerator()
        # create customer object
        cust = Customer(i+1, name, loc[1], loc[0])
        customers.append(cust)
        i += 1
        print(f'{i} customers created')
    # write to csv
    with open("random_names.csv", 'w', encoding="utf8") as f:
        for elem in customers:
            f.write(f"{elem.nameIDString()},{elem.locationString()}\n")
    print()
    # print typos/errors
    print(errLoc)
    print(rmSpace)
    print(errChar)

if __name__ == "__main__":
    main()