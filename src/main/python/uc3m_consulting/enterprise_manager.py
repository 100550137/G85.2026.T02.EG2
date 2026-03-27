import json
import os
import re
from datetime import datetime
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:
    """Clase para la gestión de operaciones corporativas"""

    # Ruta del fichero según enunciado
    DATA_FILE = "corporate_operations.json"

    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_acronym: str,
                         project_description: str, department: str,
                         date: str, budget: float):
        """RF1: Registro de proyecto con validaciones CEV/CENV y VLV/VLNV"""

        # --- 1. VALIDACIÓN company_cif ---
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("CENV1: El CIF debe ser string")
        if len(company_cif) != 9:
            raise EnterpriseManagementException("CENV3/4: El CIF debe tener 9 caracteres")
        if not company_cif[0].isalpha():
            raise EnterpriseManagementException("CENV5: El primer carácter debe ser una letra")
        if not self.validate_cif(company_cif):
            raise EnterpriseManagementException("CENV2: El CIF no es válido")

        # --- 2. VALIDACIÓN project_acronym ---
        if not isinstance(project_acronym, str):
            raise EnterpriseManagementException("CENV6: El acrónimo debe ser string")
        if not (5 <= len(project_acronym) <= 10):
            raise EnterpriseManagementException("CENV7/8: Longitud de acrónimo inválida (5-10)")
        if not project_acronym.isalnum():
            raise EnterpriseManagementException("CENV9: Caracteres no permitidos en el acrónimo")

        # --- 3. VALIDACIÓN project_description ---
        if not isinstance(project_description, str):
            raise EnterpriseManagementException("CENV10: La descripción debe ser string")
        if not (10 <= len(project_description) <= 30):
            raise EnterpriseManagementException("CENV11/12: Longitud de descripción inválida (10-30)")

        # --- 4. VALIDACIÓN department ---
        if not isinstance(department, str):
            raise EnterpriseManagementException("CENV13: El departamento debe ser string")
        if department not in ["HR", "FINANCE", "LEGAL", "LOGISTICS"]:
            raise EnterpriseManagementException("CENV14: Departamento no permitido")

        # --- 5. VALIDACIÓN budget ---
        if not isinstance(budget, (float, int)):
            raise EnterpriseManagementException("CENV27: El presupuesto debe ser numérico")

        # Rango según enunciado (50k - 1M)
        if not (50000.00 <= budget <= 1000000.00):
            raise EnterpriseManagementException("CENV28/29: Presupuesto fuera de rango")

        # Máximo 2 decimales significativos
        if round(budget, 2) != budget:
            raise EnterpriseManagementException("CENV30: El presupuesto debe tener máximo 2 decimales")

        # --- 6. VALIDACIÓN date (REVISADA Y ROBUSTA) ---
        if not isinstance(date, str):
            raise EnterpriseManagementException("CENV15: La fecha debe ser string")

        # Formato estricto DD/MM/YYYY (ej: 02/02/2026)
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", date):
            raise EnterpriseManagementException("CENV16: Formato de fecha inválido. Use DD/MM/YYYY")

        try:
            date_obj = datetime.strptime(date, "%d/%m/%Y")

            # Rango de años 2025-2027
            if not (2025 <= date_obj.year <= 2027):
                raise EnterpriseManagementException("CENV24/25: Año fuera de rango (2025-2027)")

            # Comparación con la fecha actual (respeta freeze_time)
            today = datetime.now().date()
            project_date = date_obj.date()

            if project_date < today:
                raise EnterpriseManagementException("CENV26: La fecha es anterior al registro")

        except ValueError:
            raise EnterpriseManagementException("CENV16: Fecha cronológicamente imposible")

        # --- 7. PROCESO Y PERSISTENCIA ---
        new_project = EnterpriseProject(company_cif, project_acronym, project_description,
                                        department, date, budget)

        # Carga del JSON con manejo de errores de fichero vacío o corrupto
        data = []
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content.strip():
                        data = json.loads(content)
            except (json.JSONDecodeError, IOError):
                data = []

        # Comprobar si ya existe el proyecto para ese CIF (O3)
        for entry in data:
            if entry.get("company_cif") == company_cif and \
                    entry.get("project_acronym") == project_acronym:
                raise EnterpriseManagementException("El proyecto ya existe para este CIF")

        # Guardar datos actualizados
        data.append(new_project.to_json())
        with open(self.DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return new_project.project_id

    @staticmethod
    def validate_cif(cif: str):
        """Algoritmo de validación de CIF blindado contra caracteres no numéricos"""
        try:
            cif = cif.upper()
            if len(cif) != 9:
                return False

            letter = cif[0]
            number = cif[1:8]
            control = cif[8]

            # Comprobar que la parte central son TODO números
            if not number.isdigit():
                return False

            # Suma posiciones pares
            add_even = int(number[1]) + int(number[3]) + int(number[5])

            # Suma posiciones impares
            add_odd = 0
            for i in range(0, 7, 2):
                res = int(number[i]) * 2
                add_odd += (res // 10) + (res % 10)

            total_sum = add_even + add_odd
            last_digit = int(str(total_sum)[-1])
            digit_control = (10 - last_digit) % 10

            letter_control = "JABCDEFGHI"[digit_control]

            if letter in "ABEH":
                return control == str(digit_control)
            elif letter in "KPQS":
                return control == letter_control
            else:
                return control == str(digit_control) or control == letter_control
        except Exception:
            # Cualquier error inesperado (letras donde no deben, etc.) devuelve False
            return False
