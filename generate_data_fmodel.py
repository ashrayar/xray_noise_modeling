import sys
import os


orig_resol = 0.77

r10s = range(8, 31)

for r10 in r10s:
  print(r10)

  r = r10 * 0.1
  rs = "%.1f" % r

  cmd = "phenix.fmodel 7kr0_shift_bfac_%s_p1.pdb k_sol=0.4 b_sol=45 high_resolution=%f real r_free=0.05 file_name=7kr0_resol_%s.mtz" \
        % (rs, r, rs)
  print(cmd)
  os.system(cmd)