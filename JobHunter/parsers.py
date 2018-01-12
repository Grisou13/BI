import os, html, sys
from bs4 import BeautifulSoup, BeautifulStoneSoup

class Job():
    id = ""
    title = ""
    url = ""
    company = ""
    date = ""
    misc_skills = []
    technologies = []
    years_of_experience = ""
    diploma_required = ""
    location = ""

    parsed_xml_entity = None
    content = None
    bs = None


class Parser:
    parsers = []

    def parse(self, data):
        for p in self.parsers:
            p.build(data)

    def add(self, parser):
        self.parsers.append(parser)


class StackoverflowParser:
    def build(item):
        job = Job()
        data = html.unescape(item.description).replace("<br>", "").replace("<br />", "").replace("<br/>",
                                                                                                 "")  # remove all rubish
        bs = BeautifulSoup(data, "html.parser")
        job.bs = bs
        job.content = data
        job.parsed_xml_entity = item

        job.url = item.link
        # determine job title
        job.title = job.determine_title(item.title)
        job.company = job.determine_company(item.title)

        locationInTitle = job.guess_location_in_title(job.title)

        job.location = item.get("location", locationInTitle)
        isRemote = job.guess_job_is_remote(job)
        if isRemote and job.location == "":
            job.location = "remote"
        job.date = item.published
        job.id = item.id

        job.technologies = [x.term for x in item.tags] if hasattr(item, "tags") else []
        technos = job.determine_technos(bs)
        if not len(technos):
            job.scrap_page_for_info(job.url)
        job.technologies = job.technologies + technos

        job.diplome_required = job.determine_diploma(item.title + "\n" + bs.get_text() + "\n")
        job.number_years_minima = job.determine_years_of_experience(bs.get_text())

        return job

    def scrap_page_for_info(self, url):
        print(url)
        return
        res = requests.get(url)
        bs = BeautifulSoup(res.text, "html.parser")
        technos = bs.find("")
        requirements = bs.find()

    def get_content(self):
        return html.unescape(self.parsed_xml_entity.description).replace("<br>", "").replace("<br />", "").replace(
            "<br/>", "")  # remove all rubish

    def __str__(self):
        return json.dumps(self.__dict__)

    def determine_technos(self, bs):
        wantedWords = ['language',
                       'experience',
                       'knowledge',
                       'expert',
                       'skill',
                       'proficient',
                       'programming',
                       'technologies',
                       'technology']

        b = bs
        m = b.find(text=re.compile(r"require.*:"))
        technos = []
        # print(m)
        if m is None:
            return technos
        item = m.findNext('ul')

        if item is None:
            return technos
        for li in item.findAll('li'):
            line = li.get_text()
            if (not line.endswith('?') and any(word in line.lower() for word in wantedWords)):
                # print(line)
                techno1 = re.findall(r'\(([^)]+)\)', line)
                if techno1:
                    techno1 = list(filter(None, re.split(r', |\/',
                                                         techno1[0].replace('eg: ', '').replace('e.g. ', '').replace(
                                                             'etc.', ''))))
                    technos = technos + techno1
                techno2 = line.replace('eg: ', '').replace('e.g. ', '').split(':')
                if len(techno2) == 2:
                    techno2 = techno2[1]
                    techno2 = list(filter(None, re.split(r', |\/', techno2.replace('etc.', ''))))
                    technos = technos + techno2

        return technos

    def determine_years_of_experience(self, text):
        regs = [
            r"(\d.?) years\s(?:of\s)?\s?experience"
        ]
        for r in regs:
            m = re.search(r, text)
            if m is None:
                return ""
            else:
                return m.group(1)

    def determine_requirements(self, text):
        pass

    def determine_diploma(self, text):
        # ((Bachelor|Master)\s?(?:degree\s)?\s?(in (.+?))?)[,\.\!](?:or|and|\W)
        # ((Bachelors?|Master)\s?(?:degree\s)?\s?(in (.+?)))(?=,|\.|!|\/|or|and|[A-])
        regs = {
            "Bachelor - Master": r"((bachelors? or masters?|bachelors?|masters?)\s((?:(?!or|,|\.|!).)*))",
            "Apprenticeship": r"(apprenticeship)",
            "CFC": r"(CFC)"
        }
        for k, v in regs.items():
            m = re.search(v, text, re.IGNORECASE)
            if m:
                return m.group(1)
        return ""

    def determine_title(self, text):
        regex = r"(.*)\s{0,}at\s{0,}(.*)"
        m = re.search(regex, text)
        return m.group(1)

    def determine_company(self, text):
        ret = ""
        regex = r"(.*)\s{0,}at\s{0,}(.*)"
        m = re.search(regex, text)
        title = m.group(2)

        reg = r"(.*)(\(.*\)$)"
        m = re.search(reg, title)
        if m is not None:
            ret = m.group(1)
        else:
            ret = title
        return ret

    def guess_location_in_title(self, text):
        regex = r"(\(.*\)$)"
        m = re.search(regex, text)
        return m.group() if m is not None else ""

    def guess_job_is_remote(self, job):
        regex = r"remote"

        return job.location == "" and re.search(regex, job.title)


class GithubParser(Parser):
    pass
