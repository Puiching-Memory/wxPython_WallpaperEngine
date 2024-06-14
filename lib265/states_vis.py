import pstats
from pstats import SortKey

#python -m cProfile -o pstats.pypt -m test_cython
#doc:https://docs.python.org/zh-cn/3.12/library/profile.html

p = pstats.Stats('./pstats.pypt')
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(50)   