# ══════════════════════════════════════════════════════════════════════════════
# OUO Intelligence — config.py
# ══════════════════════════════════════════════════════════════════════════════
# This file contains org URLs and settings.
# Keywords are in keywords.py — edit that file to add/change search terms.
# ══════════════════════════════════════════════════════════════════════════════

EMAIL_TO = "armaghan.eslami@gmail.com"


# ── EUROPE: THINK TANKS & INSTITUTES ──────────────────────────────────────────

EUROPE_ORGS = {
    "CEPS":                    "https://www.ceps.eu/who-we-are/join-ceps/",
    "ETUI":                    "https://www.etui.org/about-etui/jobs-at-etui",
    "Bruegel":                 "https://www.bruegel.org/careers",
    "TNO":                     "https://www.tno.nl/en/careers/vacancies/",
    "Rathenau":                "https://www.rathenau.nl/en/careers",
    "AIAS-HSI (UvA)":          "https://www.uva.nl/en/about-the-uva/working-at-the-uva/vacancies/vacancies.html",
    "IHS Vienna":              "https://www.ihs.ac.at/en/about/vacancies/",
    "WIFO":                    "https://www.wifo.ac.at/en/about_wifo/career_opportunities",
    "Bertelsmann Stiftung":    "https://www.bertelsmann-stiftung.de/en/careers",
    "NESTA":                   "https://www.nesta.org.uk/jobs",
    "AlgorithmWatch":          "https://algorithmwatch.org/en/jobs",
    "Fraunhofer IAO":          "https://www.iao.fraunhofer.de/en/jobs-and-careers.html",
    "Fraunhofer ISI":          "https://www.isi.fraunhofer.de/en/karriere.html",
    "SINTEF":                  "https://www.sintef.no/en/about-sintef/career/",
    "VTT":                     "https://www.vttresearch.com/en/careers",
    "JRC (European Commission)": "https://joint-research-centre.ec.europa.eu/work-us_en",
    "EUROFOUND":               "https://www.eurofound.europa.eu/en/pages/vacancies",
    "CEDEFOP":                 "https://www.cedefop.europa.eu/en/about-cedefop/job-opportunities/vacancies",
    "EU-OSHA":                 "https://osha.europa.eu/en/careers/vacancies-open",
}


# ── EUROPE: UNIVERSITIES ───────────────────────────────────────────────────────

EUROPE_UNIVERSITIES = {
    "KU Leuven":                  "https://www.kuleuven.be/personeel/jobsite/jobs/staff",
    "Ghent University":           "https://jobs.ugent.be/go/Professorial-staff/8808902/",
    "Vrije Universiteit Brussel": "https://jobs.vub.be/go/EN_ACADEMIC-PERSONNEL-&-RESEARCHERS/3775501/",
    "Radboud University":         "https://www.ru.nl/en/working-at/job-opportunities/vacancy-type/postdoc-5015",
    "University of Amsterdam":    "https://werkenbij.uva.nl/",
    "Tilburg University":         "https://career5.successfactors.eu/portalcareer?_s.crb=VHaBjWoLx2EGbehUlohGe2i63ik6Ivtfw8FyudzfbG4%253d",
    "Erasmus University Rotterdam": "https://www.eur.nl/werken-bij-eur",
    "Delft University of Technology": "https://careers.tudelft.nl/search",
    "TU Munich":                  "https://www.tum.de/en/about-tum/careers-and-jobs/postdocs",
    "LMU Munich":                 "https://www.lmu.de/en/about-lmu/working-at-lmu/job-portal/academic-staff/",
    "University of Cologne":      "https://jobportal.uni-koeln.de/",
    "Humboldt University Berlin": "https://www.hu-berlin.de/en/university/working-at-the-hu/jobs",
    "University of Vienna":       "https://jobs.univie.ac.at/search",
    "WU Vienna":                  "https://www.wu.ac.at/en/hr/open-positions/",
    "University of Graz":         "https://jobs.uni-graz.at/en/jobs",
    "TU Graz":                    "https://jobs.tugraz.at/en/jobs",
}


# ── EUROPE: EXPANDED (labor institutes, intl orgs, stats agencies, survey firms) ──

EUROPE_ORGS_EXPANDED = {

    # Labor economics and policy research institutes
    "IZA Institute of Labor Economics (Bonn)":        "https://www.iza.org/en/jobs",
    "CPB Netherlands Bureau for Economic Policy Analysis": "https://www.cpb.nl/en/vacancies",
    "DIW Berlin (German Institute for Economic Research)": "https://www.diw.de/en/diw_01.c.100406.en/jobs.html",
    "IFAU Sweden (labour market policy evaluation)":   "https://www.ifau.se/en/About-IFAU/Vacancies/",
    "IAB Germany (Institute for Employment Research)": "https://www.iab.de/en/iab/jobs.aspx",
    "WZB Berlin Social Science Center":               "https://www.wzb.eu/en/jobs",
    "ZEW Mannheim (Centre for European Economic Research)": "https://www.zew.de/en/about-zew/careers",
    "LISER Luxembourg (work, health, labour market)": "https://www.liser.lu/jobs.cfm",

    # International organizations
    "OECD careers":              "https://www.oecd.org/careers/",
    "ILO Geneva careers":        "https://www.ilo.org/global/about-the-ilo/employment/lang--en/index.htm",
    "World Bank jobs":           "https://jobs.worldbank.org/",
    "Eurofound":                 "https://www.eurofound.europa.eu/en/about-eurofound/recruitment",

    # National statistics and government labor research
    "CBS Statistics Netherlands": "https://www.werkenbijhetcbs.nl/",
    "ONS UK Office for National Statistics": "https://www.ons.gov.uk/aboutus/careers",
    "Destatis Germany Federal Statistical Office": "https://www.destatis.de/EN/About-Us/Careers/_node.html",
    "Statistik Austria":         "https://www.statistik.at/en/about-us/careers",

    # Survey and market research firms
    "Ipsos careers":             "https://www.ipsos.com/en/careers",
    "Kantar careers":            "https://kantar.com/careers",
    "GfK careers":               "https://www.gfk.com/careers",
    "Gallup careers":            "https://www.gallup.com/careers/home.aspx",

    # Consulting research arms
    "BCG Henderson Institute careers": "https://www.bcg.com/careers",
    "Deloitte Human Capital research careers": "https://www2.deloitte.com/global/en/pages/careers/articles/join-deloitte.html",

    # People analytics in large companies
    "Philips careers":           "https://www.philips.com/a-w/careers.html",
    "Unilever careers":          "https://careers.unilever.com/",
    "ING Group careers":         "https://www.ing.jobs/global/careers.htm",
    "Spotify jobs":              "https://www.lifeatspotify.com/jobs",
    "Booking.com careers":       "https://careers.booking.com/",

    # Program evaluation and impact research
    "3ie International Initiative for Impact Evaluation": "https://www.3ieimpact.org/about-3ie/work-3ie",
    "J-PAL Europe":              "https://www.povertyactionlab.org/careers",
    "Mathematica careers":       "https://www.mathematica.org/career-opportunities",
    "ICF International Europe":  "https://www.icf.com/careers",

    # HR research and workforce consulting
    "Mercer careers":            "https://careers.mercer.com/",
    "Willis Towers Watson careers": "https://careers.wtwco.com/",
    "Korn Ferry careers":        "https://www.kornferry.com/careers",
}


# ── JAPAN: ORGS & THINK TANKS ─────────────────────────────────────────────────

JAPAN_ORGS = {
    "ILO Tokyo":              "https://www.ilo.org/tokyo/lang--en/index.htm",
    "UN University":          "https://careers.unu.edu/o/researcher",
    "OECD Tokyo":             "https://www.oecd.org/careers/",
    "GRIPS":                  "https://www.grips.ac.jp/en/about/jobs/",
    "RIETI":                  "https://www.rieti.go.jp/en/about/recruitment.html",
    "Recruit Works Institute": "https://www.works-i.com/english",
    "UTokyo PARI":            "https://pari.u-tokyo.ac.jp/eng/",
    "Asia Pacific Initiative": "https://apinitiative.org/en/",
    "Mercari R4D":            "https://apply.workable.com/mercari/",
    "JILPT":                  "https://www.jil.go.jp/english/about/recruit.html",
}


# ── JAPAN: UNIVERSITIES ────────────────────────────────────────────────────────

JAPAN_UNIVERSITIES = {
    # University of Tokyo
    "UTokyo - main jobs page":                      "https://www.u-tokyo.ac.jp/focus/en/jobs/index.php",
    "UTokyo Tokyo College (interdisciplinary, English)": "https://www.tc.u-tokyo.ac.jp/en/recruit/",
    "UTokyo Institute for Future Initiatives":      "https://ifi.u-tokyo.ac.jp/en/",

    # Hitotsubashi University (social sciences -- posts individual PDFs)
    "Hitotsubashi University jobs":                 "https://www.hit-u.ac.jp/jinji-saiyo/",

    # Waseda University
    "Waseda University jobs":                       "https://www.waseda.jp/top/en/about/work/job-openings",
    "Waseda Institute for Advanced Study (WIAS)":   "https://www.waseda.jp/inst/wias/en/recruitment/",

    # Keio University
    "Keio University jobs":                         "https://www.keio.ac.jp/en/jobs/",

    # Sophia University (posts via piloti.sophia.ac.jp)
    "Sophia University jobs":                       "https://piloti.sophia.ac.jp/eng/",

    # ICU
    "ICU jobs":                                     "https://www.icu.ac.jp/en/recruit/",

    # Meiji University
    "Meiji University jobs":                        "https://www.meiji.ac.jp/seikei/koubo/",

    # Ritsumeikan APU
    "Ritsumeikan APU jobs":                         "https://en.apu.ac.jp/home/faculty/content1399/",

    # Rikkyo University
    "Rikkyo University jobs":                       "https://english.rikkyo.ac.jp/news/",

    # Temple University Japan
    "Temple University Japan jobs":                 "https://www.tuj.ac.jp/joblistings",

    # Tokyo Tech (now Institute of Science Tokyo)
    "Tokyo Tech / Institute of Science Tokyo jobs": "https://www.isct.ac.jp/en/about/careers",

    # Chuo University
    "Chuo University jobs":                         "https://www.chuo-u.ac.jp/aboutus/recruit/",
}


# ── JAPAN: EXPANDED (labor research, intl orgs, HR firms, consulting) ──────────
# Note: JILPT, RIETI, OECD Tokyo, Recruit Works, Asia Pacific Initiative
# are already in JAPAN_ORGS above. Not repeated here to avoid double-scanning.

JAPAN_ORGS_EXPANDED = {

    # Labor and workforce research
    "NLI Research Institute":                      "https://www.nli-research.co.jp/en/",
    "Japan Productivity Center":                   "https://www.jpc-net.jp/",

    # International organizations with Tokyo offices
    "World Bank Tokyo office":                     "https://www.worldbank.org/en/country/japan",
    "UNDP Japan":                                  "https://www.undp.org/japan",
    "UNICEF Japan":                                "https://www.unicef.or.jp/about_unicef/about_job.html",

    # People analytics and HR research
    "Persol Research and Consulting":              "https://rc.persol-group.co.jp/",
    "Pasona Group":                                "https://www.pasonagroup.co.jp/english/",

    # Consulting firms with Japan offices
    "McKinsey Japan careers":                      "https://www.mckinsey.com/jp/careers",
    "Deloitte Japan careers":                      "https://www2.deloitte.com/jp/en/pages/careers/articles/careers-home.html",
    "Accenture Japan careers":                     "https://www.accenture.com/jp-en/careers",

    # Survey and social research
    "Intage Research":                             "https://www.intage.co.jp/english/",
    "Macromill":                                   "https://www.macromill.com/en/",

    # Policy and government-adjacent research
    "NISTEP National Institute of Science and Technology Policy": "https://www.nistep.go.jp/en",
    "National Institute of Population and Social Security Research": "https://www.ipss.go.jp/s-info/e/Employ/Employ.asp",

    # NGO and nonprofit research
    "Nippon Foundation":                           "https://www.nippon-foundation.or.jp/en/who/jobs",
    "Sasakawa Peace Foundation":                   "https://www.spf.org/en/about/jobs.html",
}


# ── JAPAN: ACADEMIC JOB BOARDS ────────────────────────────────────────────────

JAPAN_ACADEMIC_BOARDS = {
    "JREC-IN Portal (main Japan academic jobs board)": "https://jrecin.jst.go.jp/seek/SeekTop?ln=1",
    "JREC-IN Social Science filter": "https://jrecin.jst.go.jp/seek/SeekTop?ln=1&bgCode1=02&bgCode2=0200",
    "Daigaku Jobs (Japanese board)": "https://jobs.daigaku.net/",
    "Times Higher Education Japan":  "https://www.timeshighereducation.com/unijobs/listings/japan/",
}


# ── POSTDOC AND RESEARCH JOB BOARDS ───────────────────────────────────────────

POSTDOC_BOARDS = {
    "Euraxess":               "https://euraxess.ec.europa.eu/jobs/search",
    "Academic Positions":     "https://academicpositions.com",
    "Nature Careers":         "https://www.nature.com/naturecareers",
    "ResearchGate Jobs":      "https://www.researchgate.net/jobs",
    "Times Higher Education": "https://www.timeshighereducation.com/unijobs/",
    "Academic Transfer (NL)": "https://www.academictransfer.com/en/",
    "Find a Postdoc":         "https://www.findapostdoc.com/",
    "Jobs.ac.uk":             "https://www.jobs.ac.uk/",
    "EuroBrussels":           "https://www.eurobrussels.com",
    "CORDIS (Horizon Europe projects)": "https://cordis.europa.eu/search/en?q=future+of+work",
    "JREC-IN":                "https://jrecin.jst.go.jp/seek/SeekTop?ln=1",
}

POSTDOC_BOARDS_EXPANDED = {
    "Devex (international development jobs)": "https://www.devex.com/jobs/search#",
    "ReliefWeb (UN/NGO jobs)":               "https://reliefweb.int/jobs",
    "EuroBrussels (EU policy jobs)":         "https://www.eurbrussels.com/jobs_list.html",
    "Euractiv Jobs":                         "https://jobs.euractiv.com/",
    "GaijinPot Jobs (English jobs in Japan)": "https://jobs.gaijinpot.com/",
}


# ── NEWS SEARCH QUERIES ────────────────────────────────────────────────────────

NEWS_SOURCES = [
    "ELSI artificial intelligence",
    "future of work AI Europe",
    "AI governance Japan",
    "algorithmic management research",
    "CEPS future of work",
    "ETUI digital work",
    "Mercari R4D ELSI",
    "AlgorithmWatch research",
    "Bertelsmann Stiftung digitalization",
    "ILO future of work AI",
    "postdoc organizational psychology AI",
    "researcher vacancy ELSI ethics",
]
