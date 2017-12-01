#/usr/bin/env python3
import feedparser
from bs4 import BeautifulSoup
import html
import requests
import os, sys
import re
# json
github_api = "https://jobs.github.com/positions.json"
# rss
stackoverflow_api="https://stackoverflow.com/jobs/feed"

class Job():
	id=""
	title=""
	url=""
	company=""
	date=""
	requirements=""
	technologies=""
	number_years_minima=""
	diplome_required=""

def determine_technos(text):
	b = BeautifulSoup(text)
	m = b.find(text=re.compile(r"require.*:"))
	print(m)
	if m is None:
		return
	item = m.findNext('ul')

	print(item)


def determine_requirements(text):
	pass

def determine_diplome(text):
	pass

def parse_rss(url):
	parsed = feedparser.parse(url)
	for item in parsed.entries:
		job = Job()
		job.url = item.link
		#determine job title
		regex = r"(.*)\s{0,}at\s{0,}(.*)"
		m = re.search(regex, item.title)
		job.title = m.group(1)
		job.company = m.group(2)


		job.date = item.published_parsed
		job.id = item.id
		job.requirements = item.tags if hasattr(item,"tags") else []

		data = html.unescape(item.description).replace("<br>","").replace("<br />","").replace("<br/>","") # remove all rubish
		determine_technos(data)
		print()

def main():
	parse_rss(stackoverflow_api)

if __name__ == '__main__':
	main()
"""
<item><
guid isPermaLink="false">135916</guid>
<link>https://stackoverflow.com/jobs/135916/senior-software-developer-online-systems-carmax?a=JA5fwdGgzPq</link>
<a10:author><a10:name>CarMax</a10:name></a10:author>
<category>asp.net</category>
<category>reactjs</category>
<category>azure</category>
<category>c#</category>
<category>sitecore</category>
<title>Senior Software Developer - Online Systems at CarMax (Richmond, VA)</title>
<description>
	<p>What we do:</p><br /><p>Do you want to make car buying easier? Hate sitting in a dealership for hours? We have a challenge for you then&hellip;help us figure out a way to make the car buying process short, sweet and to the point!</p><br /><p>Who we are looking for:</p><br /><p>We are looking for a senior developer to drive innovation in our digital photography and merchandising space. You get to work with your own product manager and UX guru to design and develop tools for associates to capture, manipulate, and store images, as well as innovate new ways to display and manipulate our product images that will enhance our customers&rsquo; online experience.</p><br /><p><strong>Skills &amp; Requirements</strong></p><br /><p>Let&rsquo;s get under the hood! Here is the techie part:</p><br /><ul><br /><li>Microsoft .NET</li><br /><li>Azure (To the cloud!)</li><br /><li>React.js</li><br /><li>JavaScripting/Front End Technologies</li><br /><li>HTML/CSS and other web design components</li><br /><li>Microsoft SQL Server&nbsp;</li><br /><li>Continuous integration, continuous deployment, and automated testing</li><br /></ul><br /><p>What we REALLY would like:</p><br /><ul><br /><li>Android</li><br /><li>Endeca technologies</li><br /><li>Sitecore Content Management</li><br /><li>MongoDB/No SQL Technologies</li><br /><li>Deep understanding of HTTP, HTML, and current web development frameworks, patterns, and practices</li><br /><li>Experience with high-volume web architecture at both a software and infrastructure level</li><br /><li>Passion for software quality and experience with continuous integration and delivery practices</li><br /><li>Experience with automated testing</li><br /><li>Familiarity with common software design patterns</li><br /><li>Ability to mentor junior developers and help them weigh trade offs in design decisions</li><br /></ul><br /><p>What you need to have:</p><br /><ul><br /><li>5 + years of application development experience required</li><br /><li>4 year degree required; IT Course of Study preferred.&nbsp;</li><br /><li>Preferred experience in appropriate development&nbsp;language (see Specialty section)</li><br /><li>Certifications, etc.&nbsp;</li><br /><li>Appropriate Certification Preferred (see Specialty section)</li><br /><li>RDBMS experience&nbsp;</li><br /><li>Typically 6+ years of database development experience (see Specialty section)</li><br /></ul><br /><p>If think this is you, let us know and apply! What are you waiting for?</p><br /><p>See for yourself on why you should come work here:</p><br /><p><a href="https://www.themuse.com/companies/carmax" rel="nofollow">https://www.themuse.com/companies/carmax</a></p><br /><p>Sponsorship Note:</p><br /><p>Candidates must be legally authorized to work for any U.S. employer on a full-time basis. Sponsorship will be considered for this specific role.</p>
</description>
<pubDate>Fri, 17 Nov 2017 18:17:19 Z</pubDate>
<a10:updated>2017-11-17T18:17:19Z</a10:updated>
<location xmlns="http://stackoverflow.com/jobs/">Richmond, VA</location>
</item>
"""
