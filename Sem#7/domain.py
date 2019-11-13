'''
clients
    - unique ID
    - name
    - age 
    - driver license series

cars
    - valid license plate number
    - a meke and models
    - color 


we want fearure driven development
    - we start by implementing a feature and make it work
What we start with:
    add a new client : unique id name and age

1. Write a client class in the domain
    - client has an id (set in constructor, read only otherwise)
    - client has a name of len >= 3 and age _= 18 (properties)



'''

import unittest

class Client:
    def __init__ (self, clientID, clientName, clientAge):
        if clientID == None:
            raise ValueError
        self._ID = clientID
        self._name = clientName
        self._age = clientAge

    @property
    def id (self):
        return self._ID
    
    @property
    def name (self):
        return self._name
    
    @property
    def age (self):
        return self._age
    
    @name.setter
    def name (self, value):
        if value == None or len(value) < 3:
            raise ValueError
        else:
            self._name = value

    @age.setter
    def age (self, value):
        if value == None or value < 18:
            raise ValueError
        else:
            age = value

    def __str__ (self):
        return str(self.ID) + " " + str(self.name) + " " + str(self.age)



'''
 this tells python this is a special test class which contains tests 
 python should find these classes and run tests on its own
 '''
class TestClient (unittest.TestCase):
    def test_client (self):
        # sum interesting
        # python 3.8 introduced walrus operator -> :=
        # if (n:= len(mylist)):

        c = Client(1, "Pop Andreea", 19 )
        self.assertEqual(c.id,1)
        assert c.name == "Pop Andreea"
        assert c.age == 19

        try:
            c.age = 17
            assert False # should not run
        except ValueError:
            assert True # we are okay
        except Exception:
            assert False # a dif exception was raised


    def test_client_again (self):
        c = Client(1, "Pop Mihnea", 20 )
        with self.assertRaises(ValueError) as ve:
            c.age = 17
        if str(ve.exception):
            pass




        
        # self.assertRaises(ValueError, c.age,20)
        '''
        try:
            c.age = 17
            assert False # should not run
        except ValueError:
            assert True # we are okay
        except Exception:
            assert False # a dif exception was raised
        '''
tc = TestClient()
tc.test_client()
tc.test_client_again()

print("hello test")

'''
1. don t forget to call tests
2. first test failure crashes my program
    - what s the status of remaining tests?
    - no reports, no feedback, nada
3. no difference between running the program and testing it

support for running unit tests is spotty in vs code
    - it s ok in pycharn and eclipse
    - probably ok in vs community

'''












#assign len(data) to n and return n
#if (n := len(data) == 3):
#    print(n)