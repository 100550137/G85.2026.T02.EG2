"""
codigo para calcular el balance de los cantidades inflows y cantidades outlfows

"""
import json
import re
from datetime import datetime
from .enterprise_management_exception import EnterpriseManagementException

class ProjectBudget:
    'class ProjectBudget:'
    def __init__(self):
        self._flow_file="flows.json"
        self._output_file="project_balance.json"
        self._id_pattern=r"^[0-9a-fA-F]{32}$"

    def check_project_budget(self,project_id:str)->bool:
        """Calcular la diferencia del inflow - outflow """
        #CM-FR-03-P1
        if not isinstance(project_id, str) or not re.match(self._id_pattern, project_id):
            raise EnterpriseManagementException
        try:
            #CM-FR-03-P2
            with open(self._flow_file,"r",encoding="utf-8") as file:
                movements = json.load(file)
            total_balance=0.0
            id_found=False
            for entry in movements:
                if entry.get("PROJECT_ID") == project_id:
                    id_found=True
                    inflow=float(entry.get("inflow",0.0))
                    outflow=float(entry.get("outflow",0.0))
                    total_balance+=(inflow-outflow)
            #CM-FR-03-O3
            if not id_found:
                raise EnterpriseManagementException("PROJECT_ID not found in movements")

            #CM-FR-03-O1
            return True

        #CM-FR-03-O3
        except FileNotFoundError as exc:
            raise EnterpriseManagementException("Internal error, flows.json not found") from exc
        except json.decoder.JSONDecodeError as exc:
            raise EnterpriseManagementException("Internal error, invalid json format") from exc

    def save_project_budget(self,project_id:str, balance:float):
        'save project budget'
        # CM-FR-03-P3
        result_data = {
            "project_id": project_id,
            "timestamp": datetime.utcnow().timestamp(),
            "balance": balance
        }

        with open(self._output_file, "a", encoding="utf-8") as out_file:
            out_file.write(json.dumps(result_data) + "\n")
