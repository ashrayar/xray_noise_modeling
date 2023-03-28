import sys
import os


orig_resol = 0.77

r10s = range(8, 31)

for r10 in r10s:
  print(r10)

  r = r10 * 0.1
  rs = "%.1f" % r

  b_shift = 0
  if r > orig_resol:
    b_shift = 10.0 * (r - orig_resol)

  cmd = "phenix.pdbtools 7kr0.pdb output.file_name=7kr0_shift_bfac_%s.pdb" \
        " convert_to_isotropic=True shift_b_iso=%f" \
        % (rs, b_shift)
  print(cmd)
  os.system(cmd)
