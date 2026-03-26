import json
import os
from datetime import datetime
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException
"""Module """

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""

    # Ruta del fichero según enunciado
    DATA_FILE = "corporate_operations.json"

    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_acronym: str,
                         project_description: str, department: str,
                         date: str, budget: float):
        """RF1: Registro de proyecto con validaciones y persistencia JSON"""

        # 1. Validación de CIF (CM-FR-01-I1)
        if not self.validate_cif(company_cif):
            raise EnterpriseManagementException("CIF no válido")

        # 2. Validación de Acrónimo (CM-FR-01-I2): 5-10 chars, Alfanumérico
        if not (5 <= len(project_acronym) <= 10):
            raise EnterpriseManagementException("Acrónimo no válido: longitud incorrecta")
        if not project_acronym.isalnum():
            raise EnterpriseManagementException("Acrónimo no válido: solo A-Z y 0-9")

        # 3. Validación de Descripción (CM-FR-01-I3): 10-30 chars
        if not (10 <= len(project_description) <= 30):
            raise EnterpriseManagementException("Descripción no válida: longitud incorrecta")

        # 4. Validación de Departamento (CM-FR-01-I4)
        allowed_depts = ["HR", "FINANCE", "LEGAL", "LOGISTICS"]
        if department not in allowed_depts:
            raise EnterpriseManagementException("Departamento no válido")

        # 5. Validación de Presupuesto (CM-FR-01-I6): Rango y 2 decimales
        if not isinstance(budget, (float, int)) or not (50000.00 <= budget <= 1000000.00):
            raise EnterpriseManagementException("Presupuesto fuera de rango")

        # Verificar que tiene exactamente 2 decimales (comparando con su redondeo)
        if round(budget, 2) != budget:
            raise EnterpriseManagementException("El presupuesto debe tener 2 decimales")

        # 6. Validación de Fecha (CM-FR-01-I5)
        try:
            date_obj = datetime.strptime(date, "%d/%m/%Y")
            # Rango de años 2025-2027
            if not (2025 <= date_obj.year <= 2027):
                raise EnterpriseManagementException("Fecha fuera de rango (2025-2027)")
            # Fecha igual o posterior a hoy (fecha de solicitud)
            if date_obj.date() < datetime.now().date():
                raise EnterpriseManagementException("La fecha debe ser igual o posterior a hoy")
        except ValueError:
            raise EnterpriseManagementException("Formato de fecha incorrecto")

        # 7. Crear objeto para generar el Project ID (MD5)
        new_project = EnterpriseProject(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget
        )
        project_id = new_project.project_id

        # 8. Gestión del fichero JSON y Duplicados (CM-FR-01-P3 / O3)
        data = []
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []

        # Comprobar si ya existe el mismo acrónimo para el mismo CIF
        for item in data:
            if item["company_cif"] == company_cif and \
                    item["project_acronym"] == project_acronym:
                raise EnterpriseManagementException("El proyecto ya existe para este CIF")

        # 9. Guardar y retornar
        data.append(new_project.to_json())
        try:
            with open(self.DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise EnterpriseManagementException(f"Error al escribir en el fichero: {str(e)}")

        return project_id

    @staticmethod
    def validate_cif(cif: str):
        """Validate CIF code."""
        letter = cif[0]
        control_caracter = ["J","A","B","C","D","E","F","G","H","I"]
        number = cif[1:8]
        add_even = int(number[1]) + int(number[3]) + int(number[5])
        add_odd = 0
        i = 0
        while i <= 6:
            odd = str(int(number[i]) * 2)
            if len(odd) == 2:
                odd = int(odd[0]) + int(odd[1])
            add_odd += int(odd)
            i += 2
        total_sum = str(add_even + add_odd)
        if total_sum[1] == "0":
            digit = 0
        else:
            digit = str(10 - int(total_sum[1]))
        if letter in ("A", "B", "E", "H") and (cif[8] != digit):
            return False
        if letter in ("K", "P", "Q", "S"):
            digit = control_caracter[int(digit)]
            if cif[8] != digit:
                return False
        return True
