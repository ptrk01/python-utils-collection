import unittest
import utils

class TestStringMethodsUtils(unittest.TestCase):

    def test_timestampToDate(self):
        self.assertEqual(utils.timestampToDate(1554807112), '2019-04-09 10:51:52')
    
    def test_fileToList(self):
        self.assertEqual(utils.fileToList('test_resources/names.txt'), ['Linus Thorvalds', 'Bill Gates', 'Steve Jobs'])
        
    def test_listToFile(self):
        utils.listToFile('test_resources/names.txt', ['Linus Thorvalds', 'Bill Gates', 'Steve Jobs'])
        self.assertEqual(utils.fileToList('test_resources/names.txt'), ['Linus Thorvalds', 'Bill Gates', 'Steve Jobs'])

if __name__ == '__main__':
    unittest.main()

