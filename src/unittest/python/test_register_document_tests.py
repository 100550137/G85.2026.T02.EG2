import unittest
import os
import json
from freezegun import freeze_time
from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


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

if __name__ == '__main__':
    unittest.main()