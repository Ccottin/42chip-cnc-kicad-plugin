import pcbnew
from ../constraints import CONSTRAINTS_MM
 
 
# Correspondance entre les clés de constraints.py et les attributs SWIG
# de BOARD_DESIGN_SETTINGS. Toutes les valeurs SWIG sont en unités internes
# (nanomètres) -> conversion via pcbnew.FromMM().
_SWIG_FIELD_MAP = {
    "min_clearance": "m_MinClearance",
    "min_track_width": "m_TrackMinWidth",
    "min_connection_width": "m_MinConn",
    "min_via_annular_width": "m_ViasMinAnnularWidth",
    "min_via_size": "m_ViasMinSize",
    "min_through_drill": "m_MinThroughDrill",
    "min_microvia_size": "m_MicroViasMinSize",
    "min_microvia_drill": "m_MicroViasMinDrill",
    "copper_edge_clearance": "m_CopperEdgeClearance",
    "hole_clearance": "m_HoleClearance",
    "hole_to_hole_min": "m_HoleToHoleMin",
}
 
 
def apply(board=None):
    """Applique CONSTRAINTS_MM au board donné (ou au board actif si None)."""
    board = board or pcbnew.GetBoard()
    if board is None:
        raise RuntimeError("Aucun board actif (lance ceci comme Action Plugin dans KiCad).")
 
    settings = board.GetDesignSettings()
 
    for key, value_mm in CONSTRAINTS_MM.items():
        attr_name = _SWIG_FIELD_MAP.get(key)
        if attr_name is None:
            print(f"[plugin_swig_version] Pas d'équivalent SWIG connu pour '{key}', ignoré.")
            continue
        if not hasattr(settings, attr_name):
            print(f"[plugin_swig_version] Attribut absent sur cette version de KiCad : {attr_name}")
            continue
        setattr(settings, attr_name, pcbnew.FromMM(value_mm))
 
    pcbnew.Refresh()
 
 
class ModifierConstraints(pcbnew.ActionPlugin):
    """Action Plugin : applique les contraintes de constraints.py en un clic."""
 
    def defaults(self):
        self.name = "Modifier Constraints"
        self.category = "Design Rules"
        self.description = "Applique les contraintes définies dans constraints.py au board actif"
        self.show_toolbar_button = True
 
    def Run(self):
        apply()
 
 
if __name__ == "__main__":
    apply()