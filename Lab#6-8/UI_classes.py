from tests import *
from service import *

class UI:
    def __init__ (self):
        self._service = Service()
        self._repository = self._service._repository
        


    @staticmethod
    def print_books_menu ():
        menu = '''
1. Add book
2. List books
3. Remove book
4. Update book
x. Exit
        '''
        print(menu)

    def add_book_UI (self):
        '''
        Reads and adds a book to the book list
        '''
        bookId = input("Give book ID: ").strip(" ")
        title = input("Give title: ").strip(" ")
        author = input("Give author: ").strip(" ")
        book = Book(bookId, title, author)

        try:
            self._repository.add_book(book)
            print("\nThe book was added succesfully\n")
        except duplicateID:
            print("\nThe book already exists\n")
        except badId:
            print("\nThe id is not a natural number\n")
        except emptyString:
            print("\nThe author or the title is void\n")
        
    def list_books_UI (self):
        books = self._repository.list_books()
        if len(books) == 0:
            print("\nThere are no books\n")
        else:
            for i in books:
                print(i)

    def remove_book_UI (self):
        '''
        Removes a book after a given id
        '''
        ID = input("Give the book ID: ")

        try:
            self._repository.remove_bookID(ID)
            print("\nThe book was removed succesfully\n")
        except IdDoesNotExist:
            print("\nThe required book does not exist\n")
        except badId:
            print("\nThe is not a natural number")
        
    def update_book_UI (self):
        '''
        Updates the author or the title of a given book
        '''
        ID = input("Give ID: ")
        try:
            self._repository.valid_ID(ID)
        except badId:
            print("\nThe id is not a natural number\n")
            return

        choice = '''
1. Update author
2. Update title
        '''
        print(choice)
        choice = input("> ")
        if choice == "1":
            author = input("Give new author: ")
            try:
                self._repository.update_book_author(ID, author)
                print("\nThe book was updated succesfully\n")
            except IdDoesNotExist:
                print("\nThe required book doesn't exist\n")
            except emptyString:
                print("\nThe new name of the author is void\n")
        
        elif choice == "2":
            title = input("Give title: ")
            try:
                self._repository.update_book_title(ID, title)
                print("\nThe book was updated succesfully\n")
            except IdDoesNotExist:
                print("\nThe required book does not exist\n")
            except emptyString:
                print("\nThe new value of the title is void\n")
        else:
            print("\nInvalid command\n")

    def start_book_ui (self):
        commands = {
            "1" : self.add_book_UI,
            "2" : self.list_books_UI,
            "3" : self.remove_book_UI,
            "4" : self.update_book_UI
        }

        while True:
            self.print_books_menu()
            choice = input("> ")
            print("")
            choice = choice.strip(" ")
            if choice in commands:
                commands[choice]()
                if choice in ["1", "3"]:
                    self._repository.sort_book_list()
            elif choice == "x":
                return
            else:
                print("Invalid command")
       

    @staticmethod
    def print_clients_menu():
        menu = '''
1. Add client
2. List clients
3. Remove client
4. Update client
x. Exit
'''
        print (menu)
    def add_client_ui (self):
        '''
        Function reads a client and adds it to the list
        '''
        ID = input("Give ID: ").strip(" ")
        name = input("Give name: ").strip(" ")
        client = Client(ID, name)
        try:
            self._repository.add_client(client)
            print("\nThe client was added succesfully\n")
        except badId:
            print("\nThe id is not a natural number\n")
        except duplicateID:
            print("\nA client with this id already exists\n")

    def list_clients_ui (self):
        '''
        Function lists all clients
        '''
        clients = self._repository.list_clients()
        if len(clients) == 0:
            print("\nThere are no clients\n")
        else:
            for i in clients:
                print(i)
            
    def remove_client_ui (self):
        '''
        Removes a client from the list of clients
        '''
        ID = input("Give the id: ").strip(" ")
        try:
            self._repository.remove_client(ID)
            print("\nThe client was removed succesfully")
        except IdDoesNotExist:
            print("\nThe required id does not exist\n")
        except badId:
            print("\nThe id is not a natural number\n")

    def update_client_ui (self):
        '''
        Updates a client's name
        '''
        ID = input("Give id: ").strip(" ")
        name = input("Give name: ").strip(" ")
        try: 
            self._repository.update_client_name(ID, name)
            print("\nThe client was updated succesfully\n")
        except badId:
            print("\nThe id is not a natural number\n")
        except IdDoesNotExist:
            print("\nThe required client does not exist")


    def start_client_ui (self):
        commands = {
            "1" : self.add_client_ui,
            "2" : self.list_clients_ui,
            "3" : self.remove_client_ui,
            "4" : self.update_client_ui
        }

        while True:
            self.print_clients_menu()
            choice = input("> ")
            print("")
            choice = choice.strip(" ")
            if choice in commands:
                commands[choice]()
                if choice in ["1", "3"]:
                    self._repository.sort_client_list()
            elif choice == "x":
                return
            else:
                print("Invalid command")

ui = UI()
ui.start_book_ui()