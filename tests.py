import unittest

from most_active_cookie import main

class CookieTest(unittest.TestCase):
    def test_cookie(self):
        """
        tests for most_active_cookie.py
        """
        self.assertEqual(main([]), "error: parameters not sufficient")
        self.assertEqual(main(["123.csv"]), "error: parameters not sufficient")
        self.assertEqual(main(["blank.csv", "-p"]), "error: parameters not sufficient")
        self.assertEqual(main(["blank.csv", "-d", "2020-1-5"]), "error: incorrect date format")
        self.assertEqual(main(["blank.csv", "-d", "2020-12-09"]), "error: csv file is empty")
        self.assertEqual(main(["cookie_log.csv", "-d", "2020-12-09"]), "error: no data in cvs file that matches input date")
        self.assertEqual(main(["cookie_log.csv", "-d", "2018-12-08"]), "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n")
        self.assertEqual(main(["cookie_log.csv", "-d", "2018-12-09"]), "AtY0laUfhglK3lC7\n")

if __name__ == '__main__':
    unittest.main()


# appropriate tests to run in command line 
# $python3 most_active_cookie.py    error: parameters not sufficient
# $python3 most_active_cookie.py 123.csv    error: parameters not sufficient
# $python3 most_active_cookie.py blank.csv -p   error: parameters not sufficient
# $python3 most_active_cookie.py blank.csv -d 2020-1-5  error: incorrect date format
# $python3 most_active_cookie.py blank.csv -d 2020-12-09    error: csv file is empty
# $python3 most_active_cookie.py cookie_log.csv -d 2020-12-09   error: no data in cvs file that matches input date
# $python3 most_active_cookie.py cookie_log.csv -d 2018-12-08   SAZuXPGUrfbcn5UA
#4sMM2LxV07bPJzwf
#fbcn5UAVanZf6UtG
# $python3 most_active_cookie.py cookie_log.csv -d 2018-12-09   AtY0laUfhglK3lC7