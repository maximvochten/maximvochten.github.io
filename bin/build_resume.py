"""Build the short public CV linked from the website.

Run from the repository root: python bin/build_resume.py
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/pdf/MaximVochten_resume.pdf"
FONTS = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DejaVu", str(FONTS / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(FONTS / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold")

ink = colors.HexColor("#19212a")
muted = colors.HexColor("#4c5964")
accent = colors.HexColor("#235877")

styles = {
    "name": ParagraphStyle(
        "Name", fontName="DejaVu-Bold", fontSize=19, leading=22,
        textColor=ink, spaceAfter=3,
    ),
    "tagline": ParagraphStyle(
        "Tagline", fontName="DejaVu", fontSize=10.2, leading=13,
        textColor=muted, spaceAfter=6,
    ),
    "contact": ParagraphStyle(
        "Contact", fontName="DejaVu", fontSize=8.5, leading=12,
        textColor=accent, spaceAfter=10,
    ),
    "heading": ParagraphStyle(
        "Heading", fontName="DejaVu-Bold", fontSize=10, leading=13,
        textColor=accent, spaceBefore=11, spaceAfter=5,
    ),
    "body": ParagraphStyle(
        "Body", fontName="DejaVu", fontSize=9.1, leading=12.3,
        textColor=ink, alignment=TA_LEFT, spaceAfter=4,
    ),
    "role": ParagraphStyle(
        "Role", fontName="DejaVu-Bold", fontSize=9.4, leading=12.4,
        textColor=ink, spaceBefore=5, spaceAfter=3,
    ),
    "bullet": ParagraphStyle(
        "Bullet", fontName="DejaVu", fontSize=8.9, leading=11.7,
        leftIndent=11, firstLineIndent=-8, textColor=ink, spaceAfter=3,
    ),
    "reference": ParagraphStyle(
        "Reference", fontName="DejaVu", fontSize=8.6, leading=11.4,
        leftIndent=9, firstLineIndent=-9, textColor=ink, spaceAfter=5,
    ),
}


def p(text, style="body"):
    return Paragraph(text, styles[style])


def section(title):
    return p(title, "heading")


def bullet(text):
    return p("&#8226; " + text, "bullet")


story = [
    p("Maxim Vochten", "name"),
    p("Senior Researcher | Research leadership | Robotics and autonomous systems", "tagline"),
    p(
        '<link href="mailto:maxim.vochten@mil.be">maxim.vochten@mil.be</link>'
        '  |  <link href="https://maximvochten.github.io/">maximvochten.github.io</link>'
        '  |  Brussels, Belgium',
        "contact",
    ),
    HRFlowable(width="100%", thickness=0.65, color=colors.HexColor("#d7dfe5")),
    section("PROFILE"),
    p(
        "Mechanical engineer and researcher who leads collaborative projects and supervises "
        "researchers while contributing to scientific work. Experience spans robot learning, manipulation "
        "and autonomy, from industrial applications to systems used in hazardous environments."
    ),
    section("EXPERIENCE"),
    p("Royal Military Academy, Brussels | Senior Researcher | Jan 2025 - present", "role"),
    bullet(
        "Lead RMA's team in GENIUS, an EDF project on robotic demining, with responsibility "
        "for technical work and collaboration with consortium partners."
    ),
    bullet(
        "Serve as promotor alongside colleagues on ATTENTION (DEFRA) and eUGS (EDA), "
        "supporting research direction, researcher supervision and project delivery."
    ),
    bullet(
        "Supervise researchers across robotics and autonomous systems activities and "
        "contribute to collaborative research proposals and publications."
    ),
    p("KU Leuven | Postdoctoral Researcher | Oct 2018 - Dec 2024", "role"),
    bullet(
        "Developed methods for representing and generalising skills from human demonstrations "
        "in Prof. Joris De Schutter's ERC Advanced Grant ROBOTGENSKILL."
    ),
    bullet(
        "Led the four-person KU Leuven team in PROROB, a Flanders Make ICON project on "
        "virtual-reality approaches to industrial robot programming."
    ),
    bullet(
        "Co-promotor of two PhD researchers; supervised master's theses; coordinated "
        "teaching-assistant duties in the Automation division."
    ),
    p("KU Leuven | Doctoral Researcher | Aug 2013 - Sep 2018", "role"),
    bullet(
        "Studied invariant representations of rigid-body motion for motion recognition "
        "and robot learning from demonstration; assisted with engineering teaching."
    ),
    section("EDUCATION"),
    p("PhD in Mechanical Engineering, KU Leuven (2018) | MSc in Mechanical Engineering, KU Leuven (2013)"),
    section("SUPERVISION AND TEACHING"),
    p(
        "Co-promotor of two doctoral researchers and mentor or co-supervisor of more than "
        "15 master's thesis students at KU Leuven. Teaching assistant for Applied Mechanics 3 "
        "and Mechanisms and Vibration; organiser of student robotics workshops."
    ),
    section("SELECTED PUBLICATIONS"),
    p(
        'T.-T. Nguyen, <b>M. Vochten</b> et al., '
        '<link href="https://researchportal.rma.ac.be/en/publications/predictive-and-inertia-aware-motion-planning-for-usv-navigation-i/">'
        'Predictive and Inertia-Aware Motion Planning for USV Navigation in Cluttered Harbors</link>. '
        'IFAC World Congress, 2026.', "reference"
    ),
    p(
        'T. T. Nguyen, <b>M. Vochten</b> et al., '
        '<link href="https://doi.org/10.1007/978-3-032-29469-2_27">'
        'Deep Long-Term Ship Motion Prediction with Anomaly Detection for Autonomous Maritime UAV Landing</link>. '
        'ISRM, 2026.', "reference"
    ),
    p(
        '<b>M. Vochten</b> et al., '
        '<link href="https://doi.org/10.1109/TRO.2023.3309230">'
        'Invariant Descriptors of Motion and Force Trajectories for Interpreting Object Manipulation Tasks in Contact</link>. '
        'IEEE Transactions on Robotics, 2023.', "reference"
    ),
    p(
        '<b>M. Vochten</b> et al., '
        '<link href="https://doi.org/10.1109/LRA.2020.3048674">'
        'Shape-preserving and reactive adaptation of robot end-effector trajectories</link>. '
        'IEEE Robotics and Automation Letters, 2021.', "reference"
    ),
    p(
        'Fuller records: <link href="https://scholar.google.com/citations?user=d1hglOMAAAAJ">'
        'Google Scholar</link> and <link href="https://researchportal.rma.ac.be/en/persons/maxim-vochten/">'
        'RMA research profile</link>.', "body"
    ),
    section("RESEARCH TOOLS AND RECOGNITION"),
    p(
        'Open-source packages: '
        '<link href="https://github.com/maximvochten/invariants_py">invariants_py</link> and '
        '<link href="https://github.com/maximvochten/invariants_mat">invariants_mat</link>. '
        'Best paper, Human-Friendly Robotics (2021); KUKA Innovation Award finalist (2016).'
    ),
]


def footer(canvas, doc):
    canvas.setFont("DejaVu", 8)
    canvas.setFillColor(muted)
    canvas.drawString(18 * mm, 13 * mm, "Maxim Vochten | September 2026")
    canvas.drawRightString(A4[0] - 18 * mm, 13 * mm, str(doc.page))


OUTPUT.parent.mkdir(parents=True, exist_ok=True)
pdf = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
    topMargin=16 * mm, bottomMargin=20 * mm,
    title="Maxim Vochten - CV", author="Maxim Vochten",
)
pdf.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
