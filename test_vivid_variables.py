from vivid_variables import scrape_variables
from collections import Counter

# Scrapes variables from test sources and checks that it found the correct variables (and excluded variables instantiated in for control and parameters)

assert Counter(scrape_variables("test-resources/java/Trie.java")) == Counter(['children', 'leaf', 'cur', 'child', 'root'])
assert Counter(scrape_variables("test-resources/java/DfsNoRecursion.java")) == Counter(['n', 'curEdge', 'stack', 'u', 'v', 'g'])
assert Counter(scrape_variables("test-resources/java/Gauss.java")) == Counter(['n', 'a', 'b', 'best', 'tt', 't', 'z', 'a', 'b', 'x', 'y'])
assert Counter(scrape_variables("test-resources/java/GraphCycleDetection.java")) == Counter(['n', 'color', 'next', 'cycleStart', 'cycle', 'cycleStart', 'graph', 'cycle'])
assert Counter(scrape_variables("test-resources/java/Matrix.java")) == Counter(['n', 'm', 'res', 'n', 'm', 'k', 'res', 'n', 'res', 'a', 'b', 'c', 'x', 'y'])