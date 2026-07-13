import unittest
from models.Equipment import Equipment

class TestEquipment(unittest.TestCase):
    def test_valid_equipment(self):
        eq = Equipment("EQ000001", 5.5, 10.0, True)
        self.assertEqual(eq.Id, "EQ000001")
        self.assertEqual(eq.powerRating, 5.5)
        self.assertEqual(eq.hourlyRentalRate, 10.0)
        self.assertEqual(eq.currentStatus, "Available")

    def test_invalid_id_length_short(self):
        with self.assertRaisesRegex(ValueError, "Equipment id need length from 4 to 20"):
            Equipment("SH", 5.5, 10.0, True)

    def test_invalid_id_length_long(self):
        with self.assertRaisesRegex(ValueError, "Equipment id need length from 4 to 20"):
            Equipment("THISIDISWAYTOOLONGTOBEVALID", 5.5, 10.0, True)

    def test_invalid_id_not_alnum(self):
        with self.assertRaisesRegex(ValueError, "Equipment Id only contain character or digit"):
            Equipment("EQ-00001", 5.5, 10.0, True)

    def test_invalid_power_rating(self):
        with self.assertRaisesRegex(ValueError, "Equipment power rating must be a number"):
            Equipment("EQ000001", -5.0, 10.0, True)
            
        with self.assertRaisesRegex(ValueError, "Equipment power rating must be a number"):
            eq = Equipment("EQ000001", 5.5, 10.0, True)
            eq.powerRating = 0.0

    def test_invalid_hourly_rate(self):
        with self.assertRaisesRegex(ValueError, "Equipment hourly rental rate must be a number"):
            Equipment("EQ000001", 5.5, -10.0, True)

    def test_invalid_status_type(self):
        with self.assertRaisesRegex(ValueError, "Equipment current status must be a boolean"):
            Equipment("EQ000001", 5.5, 10.0, "Sold")

if __name__ == '__main__':
    unittest.main()
