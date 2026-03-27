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

    @freeze_time("2026-03-27 12:00:00")
    def test_34_document(self):
        input_file = "src/unittest/resources/test_34.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "0bfd9d91abc1d6a6cebcfd07410d3032ce0f4a5c2333c9c99088c2e94135325b"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_35_document(self):
        input_file = "src/unittest/resources/test_35.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "c53fd6b412f37ef5bc7fbe3d0af15e95b6c5354a1643601adc016641d0cf3c0f"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_36_document(self):
        input_file = "src/unittest/resources/test_36.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "3327b1851567da0ccce2051aa24249d078a4e67ce0e978e4de0a05de2246be15"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_37_document(self):
        input_file = "src/unittest/resources/test_37.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "c53fd6b412f37ef5bc7fbe3d0af15e95b6c5354a1643601adc016641d0cf3c0f"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_38_document(self):
        input_file = "src/unittest/resources/test_38.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "16b377d55e5886dfcb0ee92515df27b7a8b8d68c548e647ecdd2dda37f15f0f0"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_39_document(self):
        input_file = "src/unittest/resources/test_39.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "069306385294f1780651257743d3385d91f8384f7c2195191b74b8fe802defd2"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_40_document(self):
        input_file = "src/unittest/resources/test_40.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "97b3125a583f5e055635a8b01e9b3b0f16b99535fe0889ffc31ce0e335065f93"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_41_document(self):
        input_file = "src/unittest/resources/test_41.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "d21fe6d667e3a64e761ae66092c10fccf462e3a56f12eae8b8c67ac42f612a38"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_42_document(self):
        input_file = "src/unittest/resources/test_42.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "f7ae323e89f69c3ccdd10aae8ef13055ba89458d27d8e64296e36e0f02073b82"

        self.assertEqual(signature, expected_hash)

    @freeze_time("2026-03-27 12:00:00")
    def test_43_document(self):
        input_file = "src/unittest/resources/test_43.json"
        manager = EnterpriseManager()

        signature = manager.register_document(input_file)

        expected_hash = "c7605a6e5d7c4cdad456c49dac6991af8e8576e5f68676524bb68065a75e1e38"

        self.assertEqual(signature, expected_hash)

if __name__ == '__main__':
    unittest.main()