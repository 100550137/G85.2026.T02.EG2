import unittest
import os
import json
from freezegun import freeze_time
from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Limpiar el almacén antes de cada test para evitar basura"""
        if os.path.exists("document_store.json"):
            os.remove("document_store.json")

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

if __name__ == '__main__':
    unittest.main()