import os
processedPath = lambda x : os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/processed/",x))
rawPath = lambda x : os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/raw/",x))
tidyPath = lambda x : os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../data/tidy/",x))
