import unittest
from freezegun import freeze_time
from uc3m_consulting.enterprise_manager import EnterpriseManager


class MyTestCase(unittest.TestCase):

    @freeze_time("2026-03-27 12:00:00")
    def test_01_document(self):
        input_file = "src/unittest/resources/test_01.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "28a20416b453507cda2ffceda801c379569cdd1d0f97662e0592a35cc7f87293"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_02_document(self):
        input_file = "src/unittest/resources/test_02.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "44544801463487bcc272f3dc0f01344ddec749d82c7e469bdb1bf5a93f73030b"

        self.assertEqual(signature, expected_hash)


    @freeze_time("2026-03-27 12:00:00")
    def test_03_document(self):
        input_file = "src/unittest/resources/test_03.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_04_document(self):
        input_file = "src/unittest/resources/test_04.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_05_document(self):
        input_file = "src/unittest/resources/test_05.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_06_document(self):
        input_file = "src/unittest/resources/test_06.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_07_document(self):
        input_file = "src/unittest/resources/test_07.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_08_document(self):
        input_file = "src/unittest/resources/test_08.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_09_document(self):
        input_file = "src/unittest/resources/test_09.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_10_document(self):
        input_file = "src/unittest/resources/test_10.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_11_document(self):
        input_file = "src/unittest/resources/test_11.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_12_document(self):
        input_file = "src/unittest/resources/test_12.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_13_document(self):
        input_file = "src/unittest/resources/test_13.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_14_document(self):
        input_file = "src/unittest/resources/test_14.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_15_document(self):
        input_file = "src/unittest/resources/test_15.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_16_document(self):
        input_file = "src/unittest/resources/test_16.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_17_document(self):
        input_file = "src/unittest/resources/test_17.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_18_document(self):
        input_file = "src/unittest/resources/test_18.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_19_document(self):
        input_file = "src/unittest/resources/test_19.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_20_document(self):
        input_file = "src/unittest/resources/test_20.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_21_document(self):
        input_file = "src/unittest/resources/test_21.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_22_document(self):
        input_file = "src/unittest/resources/test_22.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_23_document(self):
        input_file = "src/unittest/resources/test_23.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_24_document(self):
        input_file = "src/unittest/resources/test_24.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_25_document(self):
        input_file = "src/unittest/resources/test_25.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_26_document(self):
        input_file = "src/unittest/resources/test_26.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_27_document(self):
        input_file = "src/unittest/resources/test_27.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_28_document(self):
        input_file = "src/unittest/resources/test_28.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_29_document(self):
        input_file = "src/unittest/resources/test_29.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_30_document(self):
        input_file = "src/unittest/resources/test_30.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_31_document(self):
        input_file = "src/unittest/resources/test_31.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_32_document(self):
        input_file = "src/unittest/resources/test_32.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_33_document(self):
        input_file = "src/unittest/resources/test_33.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f48ff8bc76a427e69f19a3ebe63b27d8aa2a55e6cf0596e927cbe27d25c67735"

        self.assertEqual(signature, expected_hash)

if __name__ == '__main__':
    unittest.main()