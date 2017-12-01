# json
github_api = "https://jobs.github.com/positions.json"
# rss
stackoverflow_api="https://stackoverflow.com/jobs/feed"

class Job():
	id=""
	title=""
	url=""
	entreprise=""
	date=""
	requirements=""
	technologies=""
	number_years_minima=""
	diplome=""

def parse_rss(url):
	pass

def main():
	parse_rss(stackoverflow_api)

