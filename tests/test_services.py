import unittest
from datetime import datetime, timedelta
from models.Rental import Rental
from models.Equipment import Equipment
from services.RentalServices import RentalServices
from services.EquipmentServices import EquipmentServices
import os

class TestServices(unittest.TestCase):
    def setUp(self):
        self.eq_service = EquipmentServices()
        self.rt_service = RentalServices(self.eq_service)

        if os.path.exists('data/equipmentData.txt'):
            open('data/equipmentData.txt', 'w').close()
        if os.path.exists('data/rentalData.txt'):
            open('data/rentalData.txt', 'w').close()

        self.eq_service._EquipmentServices__repositories._EquipmentRepositories__equipmentList.clear()
        self.rt_service._RentalServices__repositories._RentalRepositories__rentalList.clear()

    def test_equipment_append_and_status(self):
        eq = Equipment("EQ000001", 5.5, 10.0, True)
        self.eq_service.append(eq)
        retrieved = self.eq_service.getEquipmentById("EQ000001")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.currentStatus, "Available")

    def test_rental_fee_calculation_no_penalty(self):
        eq = Equipment("EQ000001", 5.5, 10.0, True)
        self.eq_service.append(eq)

        now = datetime.now()
        later = now + timedelta(hours=2)

        rt = Rental("RT001", "John Doe", now, later, "EQ000001")
        self.rt_service.append(rt)

        base, penalty, total = self.rt_service.calculateFeesAndLatePenalties("RT001")

        self.assertAlmostEqual(base, 20.0)
        self.assertEqual(penalty, 0.0)
        self.assertAlmostEqual(total, 20.0)

    def test_rental_fee_calculation_with_penalty(self):
        eq = Equipment("EQ000001", 5.5, 10.0, True)
        self.eq_service.append(eq)

        now = datetime.now()
        start = now - timedelta(hours=4)
        expected = now - timedelta(hours=2)

        rt = Rental("RT001", "John Doe", start, expected, "EQ000001")
        self.rt_service._RentalServices__repositories.append(rt)

        base, penalty, total = self.rt_service.calculateFeesAndLatePenalties("RT001")

        self.assertAlmostEqual(base, 20.0)
        self.assertAlmostEqual(penalty, 20.2)
        self.assertAlmostEqual(total, 40.2)

    def test_rental_updates_equipment_status(self):
        eq = Equipment("EQ000001", 5.5, 10.0, True)
        self.eq_service.append(eq)

        rt = Rental("RT001", "John Doe", datetime.now(), datetime.now() + timedelta(hours=1), "EQ000001")
        self.rt_service.append(rt)

        retrieved = self.eq_service.getEquipmentById("EQ000001")
        self.assertEqual(retrieved.currentStatus, "Rented")

if __name__ == '__main__':
    unittest.main()
