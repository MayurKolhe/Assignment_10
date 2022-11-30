import unittest
import io
import sys
from unittest.mock import patch

import contacts
import sqlite3

database_name = 'mytest99.db'

import os
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)



class Test01_ADD_CONTACT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** FUNCTION CALL: add_contact('Buzz','Lightyear') THEN cur.execute('''SELECT * FROM contacts''') THEN tmp = cur.fetchall() *** EXPECT: tmp = [(1, 'Buzz', 'Lightyear')] ***
        """
        remove_file(database_name)
        c = contacts.Contacts()
        c.set_database_name(database_name)
        c.add_contact('Buzz','Lightyear')
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute('''SELECT * FROM contacts''')
        tmp = cur.fetchall()
        con.commit()
        con.close()
        self.assertEqual(tmp, [(1, 'Buzz', 'Lightyear')])
        print()
        remove_file(database_name)

class Test02_MODIFY_CONTACT(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** FUNCTION CALL: add_contact('Buzz','Lightyear') THEN modify_contact(1, 'Mickey','Mouse') THEN cur.execute('''SELECT * FROM contacts''') THEN tmp = cur.fetchall() *** EXPECT: tmp = [(1, 'Mickey', 'Mouse')] ***
        """
        remove_file(database_name)
        c = contacts.Contacts()
        c.set_database_name(database_name)
        c.add_contact('Buzz','Lightyear')
        c.modify_contact(1, 'Mickey','Mouse')
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute('''SELECT * FROM contacts''')
        tmp = cur.fetchall()
        con.commit()
        con.close()
        self.assertEqual(tmp, [(1, 'Mickey', 'Mouse')])
        print()
        remove_file(database_name)

class Test03_ADD_PHONE(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** FUNCTION CALL: add_phone(99,'Cell','(714)555-1212') THEN cur.execute('''SELECT * FROM phones''') THEN tmp = cur.fetchall() *** EXPECT: tmp = [(1, 99, 'Cell', '(714)555-1212')] ***
        """
        remove_file(database_name)
        c = contacts.Contacts()
        c.set_database_name(database_name)
        c.add_phone(99,'Cell','(714)555-1212')
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute('''SELECT * FROM phones''')
        tmp = cur.fetchall()
        con.commit()
        con.close()
        self.assertEqual(tmp, [(1, 99, 'Cell', '(714)555-1212')])
        print()
        remove_file(database_name)

class Test04_MODIFY_PHONE(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** FUNCTION CALL: add_phone(99,'Cell','(714)555-1212') THEN modify_phone(1, 'Home','(562)666-8855') THEN cur.execute('''SELECT * FROM contacts''') THEN tmp = cur.fetchall() *** EXPECT: tmp = [(1, 99, 'Home', '(562)666-8855')] ***
        """
        remove_file(database_name)
        c = contacts.Contacts()
        c.set_database_name(database_name)
        c.add_phone(99,'Cell','(714)555-1212')
        c.modify_phone(1, 'Home','(562)666-8855')
        con = sqlite3.connect(database_name)
        cur = con.cursor()
        cur.execute('''SELECT * FROM phones''')
        tmp = cur.fetchall()
        con.commit()
        con.close()
        self.assertEqual(tmp, [(1, 99, 'Home', '(562)666-8855')])
        print()
        remove_file(database_name)

class Test05_GET_CONTACT_PHONE_LIST(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** FUNCTION CALL: add_contact('Buzz','Lightyear') THEN add_phone(1,'Cell','(714)555-1212') THEN add_phone(1,'Home','(562)666-8855') THEN tmp = get_contact_phone_list() *** EXPECT: tmp = [(1, 'Buzz', 'Lightyear', 1, 1, 'Cell', '(714)555-1212'),(1, 'Buzz', 'Lightyear', 2, 1, 'Home', '(562)666-8855')] ***
        """
        remove_file(database_name)
        c = contacts.Contacts()
        c.set_database_name(database_name)
        c.add_contact('Buzz','Lightyear')
        c.add_phone(1,'Cell','(714)555-1212')
        c.add_phone(1,'Home','(562)666-8855')
        tmp = c.get_contact_phone_list()
        self.assertEqual(tmp, [(1, 'Buzz', 'Lightyear', 1, 1, 'Cell', '(714)555-1212'),(1, 'Buzz', 'Lightyear', 2, 1, 'Home', '(562)666-8855')])
        print()
        remove_file(database_name)


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
