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
        """Caso no válido: Acronym incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Acronym incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Acronym incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Acronym incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Description incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Description incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Description incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Department incorrecto"""
        cif = "A58818501"
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
        """Caso no válido: Department incorrecto"""
        cif = "A58818501"
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

    @freeze_time("2024-12-31 23:59:59")
    def test_19(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = 420,69
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_20(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "String"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_21(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "5/01/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_22(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "100/01/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_23(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "00/01/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_24(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "32/01/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_25(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/1/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_26(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/100/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_27(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/00/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_28(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/13/2027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_29(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/202"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_30(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/02027"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_31(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "1/1/2024"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_32(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "1/1/2028"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_33_a(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "1/1/2029"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_33_b(self):
        """Caso no válido: Date incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "31/12/2024"
        budget = 999999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_34(self):
        """Caso no válido: Budget incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/2025"
        budget = "50k€"

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_35(self):
        """Caso no válido: Budget incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/2025"
        budget = 49999.99

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_36(self):
        """Caso no válido: Budget incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/2025"
        budget = 1000000.01

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_37(self):
        """Caso no válido: Budget incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/2025"
        budget = 50000.1

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

    @freeze_time("2024-12-31 23:59:59")
    def test_38(self):
        """Caso no válido: Budget incorrecto"""
        cif = "A58818501"
        acronym = "GLogicEmp"
        description = "Sistema Logistica Empresarial"
        department = "HR"
        starting_date = "01/01/2025"
        budget = 50000.001

        manager = EnterpriseManager()

        try:
            res = manager.register_project(cif, acronym, description,
                                           department, starting_date, budget)
            self.assertEqual(len(res), 32)

        except EnterpriseManagementException as e:
            self.fail(f"El registro de proyecto lanzó una excepción inesperada: {e.message}")

if __name__ == '__main__':
    unittest.main()
