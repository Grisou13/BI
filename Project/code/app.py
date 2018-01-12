import config

for proc in config.PROCESSING:
    print("Processing ", proc.name)
    proc.process()
