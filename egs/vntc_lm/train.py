from os.path import abspath, dirname, join

from language_model import SRILanguageModel

sri_bin = "/usr/share/srilm/bin/i686-m64"
lm_tt = SRILanguageModel(sri_bin, "tmp/lm_tt.bin")
# lm_tt.fit("data/train/The thao.txt")
lm_vt = SRILanguageModel(sri_bin, "tmp/lm_vt.bin")
# lm_vt.fit("data/train/Vi tinh.txt")

CWD = dirname(__file__)
filepath = "data/test/The thao/TT_NLD_T_ (8488).txt"
filepath = "data/test/Vi tinh/VT_TT_T_ (5460).txt"
filepath = "data/test/Vi tinh/VT_VNE_T_ (1635).txt"
file = abspath(join(CWD, filepath))
print(lm_tt.predict(file))
print(lm_vt.predict(file))

