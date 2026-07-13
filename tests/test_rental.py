import unittest
from datetime import datetime, timedelta
from models.Rental import Rental

class TestRental(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now()
        self.later = self.now + timedelta(hours=2)

    def test_valid_rental(self):
        rt = Rental("RT001", "John Doe", self.now, self.later, "EQ000001")
        self.assertEqual(rt.Id, "RT001")
        self.assertEqual(rt.clientName, "John Doe")
        self.assertEqual(rt.equipmentId, "EQ000001")
        self.assertEqual(rt.startTime, self.now)
        self.assertEqual(rt.expectedReturnTime, self.later)

    def test_invalid_id_length(self):
        with self.assertRaisesRegex(ValueError, "Rental id need length from 4 to 20"):
            Rental("RT1", "John Doe", self.now, self.later, "EQ000001")

    def test_invalid_equipment_id_length(self):
        with self.assertRaisesRegex(ValueError, "Equipment id need length from 4 to 20"):
            Rental("RT001", "John Doe", self.now, self.later, "EQ1")



    def test_invalid_return_time_logic(self):
        with self.assertRaisesRegex(ValueError, "Expected return time must be later than start time."):
            Rental("RT001", "John Doe", self.later, self.now, "EQ000001")

    def test_string_time_parsing(self):
        rt = Rental("RT001", "John Doe", "15/07/2026 10:00", "15/07/2026 12:00", "EQ000001")
        self.assertEqual(rt.startTime.strftime("%d/%m/%Y %H:%M"), "15/07/2026 10:00")
        self.assertEqual(rt.expectedReturnTime.strftime("%d/%m/%Y %H:%M"), "15/07/2026 12:00")

    def test_invalid_string_time_format(self):
        with self.assertRaisesRegex(ValueError, "Invalid start time format"):
            Rental("RT001", "John Doe", "InvalidTime", self.later, "EQ000001")

if __name__ == '__main__':
    unittest.main()
