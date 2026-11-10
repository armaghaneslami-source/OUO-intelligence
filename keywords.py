# ══════════════════════════════════════════════════════════════════════════════
# OUO Intelligence — keywords.py
# ══════════════════════════════════════════════════════════════════════════════
#
# HOW THIS FILE WORKS
# ───────────────────
# There are three lists. The scanner uses them differently depending on
# whether it is scanning an academic org or an industry/think tank org.
#
# ACADEMIC orgs (universities, postdoc boards):
#   A posting is flagged RELEVANT only if it contains:
#     - at least one word from ACADEMIA_TITLES  (a job title word)
#     - AND at least one word from ACADEMIA_FIELDS  (a field/topic word)
#   This prevents false positives like MBA programs or IT roles that
#   happen to contain words like "management" or "researcher".
#
# INDUSTRY orgs (think tanks, institutes, survey firms, consultancies):
#   A posting is flagged RELEVANT if it contains:
#     - at least one phrase from INDUSTRY_STRONG
#   These phrases are specific enough that a single match is sufficient.
#   e.g. "people analytics" or "labor policy" is unlikely to appear in
#   an unrelated posting.
#
# HOW TO ADD A KEYWORD
# ────────────────────
# Just add a new string to the relevant list below.
# Use lowercase. The scanner automatically handles uppercase/mixed case.
# Use the exact phrase as it would appear in a job posting.
# Put it on its own line with a comma at the end.
#
# EXAMPLE — adding "employee relations" to academia fields:
#   "employee relations",        # <-- add it here
#
# ══════════════════════════════════════════════════════════════════════════════


# ── LIST 1: ACADEMIA TITLE TERMS ──────────────────────────────────────────────
# A posting must contain at least ONE of these to be considered relevant
# for academic orgs. These are job title / role type words.
# Add new job titles here as you encounter them in real postings.

ACADEMIA_TITLES = [

    # Postdoctoral
    "postdoctoral",
    "postdoc",
    "post-doctoral",
    "post doctoral",
    "post-doc",

    # Research positions
    "research fellow",
    "research associate",
    "research assistant",
    "research officer",
    "research scientist",
    "junior researcher",
    "early career researcher",
    "visiting researcher",
    "visiting scholar",
    "research position",

    # Faculty
    "assistant professor",
    "associate professor",
    "junior faculty",
    "lecturer",
    "tenure-track",
    "tenure track",

    # Other academic roles
    "phd position",
    "phd candidate",
    "doctoral researcher",
    "research grant",
    "fellowship",
]


# ── LIST 2: ACADEMIA FIELD TERMS ──────────────────────────────────────────────
# A posting must contain at least ONE of these to be considered relevant
# for academic orgs. These are field, topic, and method words.
# A posting that has a title term but none of these is probably unrelated
# (e.g. a research position in chemistry or software engineering).

ACADEMIA_FIELDS = [

    # Core field names
    "psychology",
    "psychological",
    "industrial psychology",
    "industrial-organizational psychology",
    "industrial/organizational psychology",
    "industrial organizational psychology",
    "i/o psychology",
    "i-o psychology",
    "io psychology",
    "occupational psychology",
    "occupational health psychology",
    "work psychology",
    "organizational psychology",
    "organisational psychology",
    "social psychology",
    "behavioral science",
    "behavioural science",
    "human factors",
    "ergonomics",

    # Organizational behavior / management
    "organizational behavior",
    "organizational behaviour",
    "organisational behavior",
    "organisational behaviour",
    "organizational studies",
    "management",
    "human resource management",
    "hrm",
    "human resources",

    # Sociology and social science
    "sociology",
    "sociological",
    "social science",
    "social sciences",
    "social research",

    # Workplace and work topics
    "workplace",
    "work environment",
    "working conditions",
    "future of work",
    "work futures",
    "new ways of working",
    "digital work",
    "platform work",
    "gig work",
    "remote work",
    "telework",
    "hybrid work",
    "workaholism",
    "overwork",
    "work hours",
    "working time",
    "precarious work",
    "precarious employment",
    "non-standard work",

    # Technology and work
    "algorithmic management",
    "algorithmic control",
    "automation",
    "ai at work",
    "artificial intelligence and work",
    "technology and work",
    "human-computer interaction",
    "hci",
    "elsi",

    # Employee outcomes
    "job satisfaction",
    "job performance",
    "job quality",
    "job demands",
    "wellbeing",
    "well-being",
    "employee wellbeing",
    "burnout",
    "work stress",
    "occupational stress",
    "motivation",
    "engagement",
    "employee engagement",

    # Diversity and inequality
    "diversity",
    "equity",
    "inclusion",
    "dei",
    "gender at work",
    "gender equality",
    "equal opportunity",
    "workplace inequality",
    "social inequality",

    # Labor market and employment
    "labor market",
    "labour market",
    "employment",
    "employability",
    "unemployment",
    "job insecurity",

    # Leadership and groups
    "leadership",
    "team dynamics",
    "group dynamics",
    "cooperation",
    "conflict",
    "trust",

    # Culture and identity
    "organizational culture",
    "organisational culture",
    "cross-cultural",
    "work identity",
    "professional identity",

    # Power and control
    "surveillance",
    "monitoring",
    "power",

    # Methods (useful for postdoc calls that specify methods)
    "structural equation",
    "sem",
    "multilevel",
    "longitudinal",
    "mixed methods",
    "qualitative research",
    "quantitative research",
    "survey research",
    "scale development",
    "field experiment",
    "intervention study",

    # Policy link
    "labor policy",
    "labour policy",
    "evidence-based policy",
    "policy research",
]


# ── LIST 3: INDUSTRY STRONG PHRASES ───────────────────────────────────────────
# For think tanks, institutes, survey firms, consultancies.
# A posting is flagged RELEVANT if it contains at least ONE of these phrases.
# These are specific enough that a single match is sufficient.
# Do NOT add generic words here (like "analyst" or "researcher" alone)
# because those will match everything. Keep these as multi-word phrases
# or very specific single terms.

INDUSTRY_STRONG = [

    # People / workforce analytics
    "people analytics",
    "workforce analytics",
    "hr analytics",
    "talent analytics",
    "organizational analytics",
    "people science",
    "people data",

    # Labor / employment research and policy
    "labor policy",
    "labour policy",
    "employment policy",
    "workforce research",
    "workforce development",
    "workforce planning",
    "labor economics",
    "labour economics",
    "labor market research",
    "labour market research",
    "future of work",
    "work futures",

    # Evaluation and development research
    "program evaluation",
    "programme evaluation",
    "impact evaluation",
    "policy evaluation",
    "monitoring and evaluation",
    "randomized controlled trial",
    "rct",
    "international development research",

    # Applied social research
    "applied social science",
    "social research",
    "behavioral research",
    "behavioural research",
    "survey research",
    "organizational research",
    "organisational research",

    # HR and organizational development
    "organizational development",
    "organisational development",
    "change management research",
    "talent management research",
    "employee experience research",
    "human capital research",

    # Field-specific roles
    "organizational psychologist",
    "organisational psychologist",
    "behavioral scientist",
    "behavioural scientist",
    "i/o psychologist",
    "people researcher",
    "workforce researcher",
    "labor researcher",
    "labour researcher",

    # Specific topics likely in relevant postings
    "algorithmic management",
    "platform work",
    "gig economy",
    "digital work",
    "ai governance",
    "responsible ai",
    "elsi",
    "diversity and inclusion research",
    "gender equality research",
    "skills development",
    "skills gap",
    "occupational health",
    "work-life balance",
    "employee wellbeing",
    "workaholism",
]
