"""class for testing the regsiter_order method"""
import unittest
from freezegun import freeze_time
from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    @freeze_time("2024-12-31 23:59:59")
    def test_01(self):
        """Caso válido: todos los datos cumplen las restricciones del enunciado"""
        cif = "A58818501"
        acronym = "ProyA"
        description = "Proyecto A"
        department = "LEGAL"
        starting_date = "01/01/2025"
        budget = 50000.01

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_02(self):
        """Caso válido: todos los datos cumplen las restricciones del enunciado"""
        cif = "A58818501"
        acronym = "ProyAB"
        description = "Proyecto AB"
        department = "FINANCE"
        starting_date = "02/02/2026"
        budget = 50000.00

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_03(self):
        """Caso válido: todos los datos cumplen las restricciones del enunciado"""
        cif = "A58818501"
        acronym = "GRedes2028"
        description = "Gestion de Redes Empresariales"
        department = "LOGISTICS"
        starting_date = "31/12/2027"
        budget = 1000000.00

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_04(self):
        """Caso válido: todos los datos cumplen las restricciones del enunciado"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_05(self):
        """Caso no válido: Cif incorrecto"""
        cif = "123"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_06(self):
        """Caso no válido: Cif incorrecto"""
        cif = "ABCDEFGHI"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_07(self):
        """Caso no válido: Cif incorrecto"""
        cif = "1234567890"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_08(self):
        """Caso no válido: Cif incorrecto"""
        cif = "1ABCDEFGH"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_09(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_10(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = 12345
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_11(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "1234"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_12(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "12345678901"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_13(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "äöüß"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_14(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "GLogicEmp"
        description = 1234567890
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_15(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "GLogicEmp"
        description = "Gestiones"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_16(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "GLogicEmp"
        description = "Gestion de Redes Empresariales1"
        department = "HR"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_17(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = 1
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_18(self):
        """Caso no válido: Cif incorrecto"""
        cif = "A5881850"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "string"
        starting_date = "30/11/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

if __name__ == '__main__':
    unittest.main()
