from cctbx.maptbx.box import shift_and_box_model
from iotbx.data_manager import DataManager


r10s = range(8, 31)

for r10 in r10s:
	print(r10)

	r = r10 * 0.1
	rs = "%.1f" % r

	dm = DataManager()
	filename_pdb="7kr0_shift_bfac_"+rs+".pdb"
	model = dm.get_model(filename=filename_pdb)
	model_p1 = shift_and_box_model(model)
	new_filename="7kr0_shift_bfac_"+rs+"_p1.pdb"
	dm.write_model_file(model_p1,new_filename)