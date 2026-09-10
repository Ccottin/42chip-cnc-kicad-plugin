from kipy import KiCad
from kipy.util import from_mm


if __name__ == "__main__" :
    
    board = KiCad().get_board()
    rules = board.get_design_rules().rules

    rules.constraints.min_clearance = from_mm(0.25)
    rules.constraints.min_track_width = from_mm(0.5)
    rules.constraints.min_connection_width = from_mm(0)
    rules.constraints.min_via_annular_width = from_mm(0.)
    rules.constraints.min_via_size = from_mm(1.6)
    rules.constraints.min_through_drill = from_mm(0.4)
    rules.constraints.min_microvia_size = from_mm(0)
    rules.constraints.min_microvia_drill = from_mm(0)
    rules.constraints.copper_edge_clearance = from_mm(1)
    rules.constraints.hole_clearance = from_mm(0.25)
    rules.constraints.hole_to_hole_min = from_mm(1)

    board.set_design_rules(rules)