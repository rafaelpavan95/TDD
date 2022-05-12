import unittest
from unittest.mock import patch
from application.employees import Employee

class TestEmployees(unittest.TestCase):

    def setUp(self):

        self.emp_1 = Employee('Rafael', 'Pavan', 60000)
        self.emp_2 = Employee('Nicole', 'Leitner', 60000)

    def tearDown(self):

        pass
    
    def TestEmail(self):

        self.assertEqual(self.emp_1.email(),'Rafael.Pavan@email.com')
        self.assertEqual(self.emp_2.email(),'Nicole.Leitner@email.com')
        

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname(), 'Rafael Pavan')
        self.assertEqual(self.emp_2.fullname(), 'Nicole Leitner')

    def test_apply_raise(self):
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 60000*1.05)
        self.assertEqual(self.emp_2.pay, 60000*1.05)

    def test_monthly_schedule(self):
        
        with patch('application.employees.requests.get') as mocked_get:
        
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Pavan/May')
            self.assertEqual(schedule, 'Success')
            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Leitner/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':

    unittest.main()

