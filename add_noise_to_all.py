import sys


r10s = range(8, 31)

for r10 in r10s:
  
  r = r10 * 0.1
  rs = "%.1f" % r
  
  print("""
  echo %s
  sftools << eof
  read 7kr0_resol_%s.mtz
  Y
  calc col cf = ran_g 0.1 col fmodel * *
  calc F col FSIM = col cf col fmodel +
  calc Q col SIGFSIM = 0.1 col fmodel *
  calc F col FWT = col FSIM
  calc P col PHWT = col PHIFMODEL
  DELETE COL FMODEL cf
  write 7kr0_resol_%s_noisy.mtz
  quit
  eof
  """ % (rs, rs, rs))
