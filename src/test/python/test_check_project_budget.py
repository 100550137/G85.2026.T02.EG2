"""Test de project budget"""
import unittest
import json
import os
from src.main.python.uc3m_consulting.check_project_budget import ProjectBudget
from src.main.python.uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class MyTestCase(unittest.TestCase):
    """test class"""
    def setUp(self):
        """usado para iniciar pruebas limpiamente"""
        self.project_budget=ProjectBudget()
        self.flow_file="flows.json"
        self.output_file="project_balance.json"
        if os.path.exists(self.flow_file):
            os.remove(self.flow_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
    def tearDown(self):
        """usado para limpiar después de pruebas"""
        if os.path.exists(self.flow_file):
            os.remove(self.flow_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_tc_rf3_01_exito_1it(self):
        """ruta 1_2_4_5_6_7_8_9_11_15_16_17_12"""
        data=[{"PROJECT_ID":"ff341ef03100429eacdfea777d6bdd56","inflow":"2424.42",
               "outflow":"1280.06"}]
        with open(self.flow_file, "w",encoding="utf-8") as f:
            json.dump(data,f)
        result=self.project_budget.check_project_budget("ff341ef03100429eacdfea777d6bdd56")
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.output_file))

    def test_tc_rf3_02_exito_n_it(self):
        """ruta 1_2_4_5_(6_7_8)xN_9_11_15_16_17_12"""
        data = [
            {"PROJECT_ID": "ff341ef03100429eacdfea777d6bdd56", "inflow": "100.0", "outflow": "0.0"},
            {"PROJECT_ID": "ff341ef03100429eacdfea777d6bdd56", "inflow": "0.0", "outflow": "30.0"}
        ]
        with open(self.flow_file, "w",encoding="utf-8") as f:
            json.dump(data,f)
        self.project_budget.check_project_budget("ff341ef03100429eacdfea777d6bdd56")
        with open(self.output_file, "r", encoding="utf-8") as f:
            result_json = json.loads(f.readline())
            self.assertEqual(result_json["balance"], 70.0) #comprueba si la acumulación ha pasado

    def test_tc_rf3_03_id_invalido(self):
        """ruta 1_2_3"""
        with self.assertRaises(EnterpriseManagementException):
            self.project_budget.check_project_budget("invalid_id_format")

    def test_tc_rf3_04_falta_json(self):
        """ruta 1_2_4_13"""
        if os.path.exists(self.flow_file):
            os.remove(self.flow_file)
        with self.assertRaises(EnterpriseManagementException) as cm:
            self.project_budget.check_project_budget("ff341ef03100429eacdfea777d6bdd56")
        self.assertIn("not found",str(cm.exception).lower())

    def test_tc_rf3_05_json_corrupt(self):
        """ruta 1_2_4_14"""
        with open(self.flow_file, "w",encoding="utf-8") as f:
            f.write("This is corrupt")
        with self.assertRaises(EnterpriseManagementException) as cm:
            self.project_budget.check_project_budget("ff341ef03100429eacdfea777d6bdd56")
        self.assertIn("format",str(cm.exception).lower())

    def test_tc_rf3_06_falta_id(self):
        """ruta 1_2_4_5_6_9_10"""
        data = [{"PROJECT_ID": "otherid0000000000000000000000000", "inflow": "10.0"}]
        with open(self.flow_file, "w", encoding="utf-8") as f:
            json.dump(data, f)
        with self.assertRaises(EnterpriseManagementException) as cm:
            self.project_budget.check_project_budget("ff341ef03100429eacdfea777d6bdd56")
        self.assertIn("not found", str(cm.exception).lower())

if __name__ == '__main__':
    unittest.main()
