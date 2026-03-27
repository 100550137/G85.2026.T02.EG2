import unittest
import os
import json
from freezegun import freeze_time
from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class MyTestCase(unittest.TestCase):

    @freeze_time("2026-03-27 12:00:00")
    def test_01_valid_registration(self):
        input_file = "src/unittest/resources/test_01.json"  # El JSON que me has pasado
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        # Este es el hash que corresponde a:
        # {alg:SHA-256, typ:DOCUMENT, project_id:a1b2c3d4e5f678901234567890abcdef, file_name:ABC12345.pdf}
        expected_hash = "ed2883d8c2b8d42127a2c01df2bbdebdf0b5af4951d67b6b9e1e43881432c064"

        self.assertEqual(signature, expected_hash)

if __name__ == '__main__':
    unittest.main()