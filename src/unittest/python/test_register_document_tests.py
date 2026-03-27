import unittest
import os
import json
from freezegun import freeze_time
from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class MyTestCase(unittest.TestCase):

    # Congelamos el tiempo para que el SHA-256 sea siempre el mismo [cite: 60]
    @freeze_time("2026-03-27 12:00:00")
    def test_01_valid_registration(self):
        """Paso 4: Caso válido - Todos los nodos no terminales presentes [cite: 14, 15]"""

        # 1. Configuración de rutas
        # Asegúrate de que este archivo existe con el JSON válido [cite: 20]
        input_file = "src/unittest/resources/test_01.json"
        store_file = "document_store.json"

        # 2. Limpieza del entorno (Pre-condición) [cite: 72, 73]
        if os.path.exists(store_file):
            os.remove(store_file)

        manager = EnterpriseManager()

        # 3. Ejecución del método [cite: 35]
        try:
            signature = manager.register_document(input_file)

            # 4. Verificación del resultado (O1: SHA-256 esperado) [cite: 42, 70]
            # Nota: Este valor de hash depende de la cadena formateada en ProjectDocument
            expected_hash = "6798059082264906561e14934a4c6806e579787a27d975390979401946894562"
            self.assertEqual(signature, expected_hash)

            # 5. Verificación de persistencia (O2: Se guardó en el almacén) [cite: 41, 71]
            self.assertTrue(os.path.exists(store_file))
            with open(store_file, "r") as f:
                data = json.load(f)
                self.assertEqual(len(data), 1)
                self.assertEqual(data[0]["project_id"], "cda29ebeed77e5fc60b6e4e183a4fa2a")
                self.assertEqual(data[0]["file_signature"], expected_hash)

        except EnterpriseManagementException as e:
            self.fail(f"El registro lanzó una excepción inesperada: {e.message}")

if __name__ == '__main__':
    unittest.main()