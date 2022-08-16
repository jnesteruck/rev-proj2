import random, numpy, json, os
from shutil import rmtree
from faker import Faker
from customer import Customer
from markov import MarkovChain

errLoc = []

def nameLength():
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

def nameFaker():
    fake = Faker()
    name = fake.name()
    return name

def findIndex(val, lst):
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    print("Item not in list.")


def allConsonants(string):
    vowels = ['a','e','i','o','u']
    for char in string:
        if char in vowels:
            return False
    return True

def nameGenerator():
    with open("letters.json", "r") as f:
        json_obj = json.load(f)
    # prob = MarkovChain(json_obj)
    alphabet = []
    startfreq = []
    for elem in json_obj["letter frequencies"]:
        alphabet.append(elem["letter"])
        startfreq.append(elem["frequency"])
    fcount = 0
    while True:
        flength = nameLength()
        fname = random.choices(alphabet, weights=startfreq, k=1)[0]
        i = 1
        while i < flength:
            idx = findIndex(fname[i-1], alphabet)
            alph = []
            freq = []
            for elem in json_obj["letter frequencies"][idx]["bigram frequency"]:
                alph.append(elem['letter'])
                freq.append(elem['frequency'])
            fname += random.choices(alph, weights=freq, k=1)[0]
            i += 1
        
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
                
                print(f"Unpronounceable name rejected (x{fcount})...")
            continue
        break
    
    lcount = 0
    while True:
        llength = nameLength()
        lname = random.choices(alphabet, weights=startfreq, k=1)[0]
        j = 1
        while j < llength:
            idx = findIndex(lname[j-1], alphabet)
            alph = []
            freq = []
            for elem in json_obj["letter frequencies"][idx]["bigram frequency"]:
                alph.append(elem['letter'])
                freq.append(elem['frequency'])
            lname += random.choices(alph, weights=freq, k=1)[0]
            j += 1
        
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
                
                print(f"Unpronounceable name rejected (x{lcount})...")
            continue
        break
    name = fname.capitalize() + " " + lname.capitalize()
    return name

def nameGen():
    # if random.random() < 0.3:
    #     return nameFaker()
    vowels = []
    vf = []
    consonants = []
    cf = []
    starts = []
    sf = []
    ends = []
    ef = []
    with open("english_freq.csv", 'r') as f:
        for line in f:
            line = line.strip()
            data = line.split(",")
            if data[2] == 'vowel':
                vowels.append(data[0])
                vf.append(float(data[1]))
            elif data[2] == 'consonant':
                consonants.append(data[0])
                cf.append(float(data[1]))
            elif data[2] == 'start':
                starts.append(data[0])
                sf.append(float(data[1]))
            elif data[2] == 'end':
                ends.append(data[0])
                ef.append(float(data[1]))
    
    # firstname
    flength = nameLength()
    fname = random.choices(starts,weights=sf,k=1)[0]
    i = len(fname)
    while i < flength:
        if fname[i-1] in vowels:
            chars = consonants
            freq = cf
        else:
            chars = vowels
            freq = vf
        while True:
            char = random.choices(chars,weights=freq,k=1)[0]
            if char == fname[i-1]:
                continue
            else:
                break
        fname += char
        i += len(char)
    fname += random.choices(ends,weights=ef,k=1)[0]
    
    # last name
    llength = nameLength() + 1
    lname = random.choices(starts,weights=sf,k=1)[0]
    j = len(lname)
    while j < llength:
        if lname[j-1] in vowels:
            chars = consonants
            freq = cf
        else:
            chars = vowels
            freq = vf
        while True:
            char = random.choices(chars,weights=freq,k=1)[0]
            if char == lname[j-1]:
                continue
            else:
                break
        lname += char
        j += len(char)
    lname += random.choices(ends,weights=ef,k=1)[0]
    name = fname.capitalize() + " " + lname.capitalize()
    return name
    

def locationGenerator():
    err = False
    locs = []
    cities = []
    countries = []
    vals = []
    with open("bigcities.csv",'r',encoding="utf8") as f:
        for line in f:
            line = line.strip()
            data = line.split(", ")
            if data[1] == 'United States':
                weight = 10 * (int(data[2]) ** 2)
            else:
                weight = int(data[2]) ** 2
            cities.append(data[0])
            countries.append(data[1])
            locs.append((data[0], data[1]))
            vals.append(weight)
    if random.random() < 0.01:
        city = random.choices(cities, weights=vals,k=1)[0]
        country = random.choice(countries)
        loc = (city, country)
        err = True
    else:
        loc = random.choices(locs, weights=vals,k=1)[0]
    rand = random.random()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if rand < 0.01:
        err = True
        c = random.randint(0,1)
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
    if err:
        errLoc.append(loc)
    return loc

def main():
    os.system("cls")
    customers = []
    i = 0
    rmSpace = []
    errChar = []
    semicol = []
    while i < 1000:
        rand = random.random()
        name = nameGenerator()
        loc = locationGenerator()
        if rand < 0.01:
            fname = name.split(" ")[0].strip(" ")
            lname = name.split(" ")[1].strip(" ")
            rmSpace.append(i+1)
            name = fname + lname
        elif rand < 0.02:
            invalid_chars = ['0','1','2','3','4','5','6','7','8','9','!','@','$','%','^','&','*','(',')','~','`','"',"'",'?','|','/',',','.','-','_','+',':',';','<','>']
            new_name = ""
            val = False
            for char in name:
                new_name += char
                if random.random() < 0.1:
                    val = True
                    new_name += random.choices(invalid_chars, k=1)[0]
            if val:
                errChar.append(i+1)
            name = new_name
        cust = Customer(i+1, name, loc[1], loc[0])
        customers.append(cust)
        i += 1
        print(f'{i} customers created')
    with open("random_names.csv", 'w', encoding="utf8") as f:
        for elem in customers:
            f.write(f"{elem.getID()}, {elem.getName()}, {elem.getCity()}, {elem.getCountry()}\n")
    print()
    print(errLoc)
    print(rmSpace)
    print(errChar)

if __name__ == "__main__":
    main()