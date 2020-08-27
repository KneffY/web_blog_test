# names book
import csv

def add(name,book):
    book.append(name)
    save(book)

def erace(name,book):
    for idx,nm in enumerate(book):
        if nm == name:
            del book[idx]
    save(book)

def show(book):
    for nm in book:
        deploy ="""
        #############################
        ## - - {}
        #############################
        """.format(nm.title())
        print (deploy)

def save(book):
    with open('people.csv','w') as p_obj:
        writer = csv.writer(p_obj)
        writer.writerow('name')
        for nm in book:
            writer.writerow(nm)

def run():
    book = []
    with open('people.csv','r') as p_obj:
        reader = csv.reader(p_obj)
        for idx,row in enumerate(reader):
            if idx == 0:
                continue
            if row == []:
                continue
            add(''.join(row),book)
    while True:
        print ('a to add, d to delet, s to show, q to Quit')
        action = input('>>>: ').lower()
        if action == 'q':
            break
        elif action == 'a':
            name = input('Enter a name: ').lower()
            add(name,book)
        elif action == 'd':
            name = input('Enter a name: ').lower()
            erace(name,book)
        elif action == 's':
            show(book)

if __name__ == '__main__':
    run()
