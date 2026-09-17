
from kipy import KiCad
from kipy.util import from_mm
from ../constraints import CONSTRAINTS_MM

 
 
def apply():
    board = KiCad().get_board()
    rules = board.get_design_rules().rules
 
    for key, value_mm in CONSTRAINTS_MM.items():
        if not hasattr(rules.constraints, key):
            print(f"[plugin_ipc_version] Attribut absent sur rules.constraints : {key}")
            continue
        setattr(rules.constraints, key, from_mm(value_mm))
 
    board.set_design_rules(rules)
 
 
if __name__ == "__main__":
    apply()