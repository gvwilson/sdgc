# Why Discrimination Persists

Becker's 1957 work on discrimination in labor markets generated an optimistic prediction.
Firms that discriminate pay a cost because
they forgo productive workers that non-discriminating competitors will hire instead.
Over time,
competitive pressure should therefore eliminate discrimination [%b Becker1971 %].

History has thoroughly falsified this prediction.
Discrimination has not been competed away in any labor market where economists have looked carefully.
The gap between Becker's prediction and the observed reality reveals that
rational economics misidentifies what discrimination is and how it works.

Economists distinguish [%g taste_discrimination "taste-based discrimination" %],
in which employers simply prefer not to hire members of certain groups regardless of productivity,
from [%g statistical_discrimination "statistical discrimination" %],
in which employers use group membership as a proxy for characteristics they cannot directly observe.
An employer who uses race or gender as a proxy for something like reliability
is drawing inferences from population-level patterns
that are themselves often the product of prior discrimination,
which creates a vicious circle.

The psychological research on [%g implicit_bias "implicit bias" %] complicates the picture further.
Studies using the Implicit Association Test and its successors show that most people,
including those who explicitly reject prejudice,
harbor automatic associations between social groups and evaluative attributes.
These associations operate below the conscious level,
and lead to well-intentioned people evaluating resumes differently
depending on the apparent race or gender of the applicant.

[%g audit_studies "Audit studies" %] provide the cleanest evidence.
Researchers send pairs of fictitious resumes to real job postings,
holding everything constant except for names that signal racial identity.
The results are consistent across many countries and many decades:
resumes with names coded as white receive significantly more callbacks
than identical resumes with names coded as Black.
The same pattern appears when resumes signal class background, gender, or disability.

But understanding why discrimination persists also requires recognizing that some workers benefit from it.
Workers who belong to favored groups face less competition for jobs, promotions, and wages
when members of excluded groups are kept out.
This gives them an incentive to back political groups that will maintain discriminatory arrangements,
even if they object adamantly to being accused of discrimination.
Such groups merely need people to believe that not actively being bad
is the same as being good.

India's caste system and South Africa's apartheid
both persisted long after any plausible economic case for them had dissolved.
They persisted because they served social and psychological functions
that economic analysis does not capture:
in particular,
they guaranteed those near the bottom of otherwise low-status hierarchies that
they were not at the very bottom.

> If you can convince the lowest white man he's better than the best colored man,
> he won't notice you're picking his pocket.
> Hell, give him somebody to look down on, and he'll empty his pockets for you.
>
> – Lyndon B. Johnson

The history of how discrimination gets built into professional structures
is worth understanding before applying it to computing.
The [%g flexner_report "Flexner Report" %] of 1910 recommended consolidating medical education
around a small number of university-based schools modeled on Johns Hopkins.
What is less often noted is what this consolidation closed:
the eclectic and homeopathic schools that had trained a significant proportion of women physicians,
and the historically Black medical colleges that were the primary pathway into medicine for Black practitioners.
The reorganization of medicine around a single credentialing model
was also a reorganization of medicine around a single demographic profile.
The American Medical Association's subsequent decades of opposition
to women's participation in medical societies
and to Black physicians' hospital admitting privileges
extended and consolidated what the Flexner Report had begun.

The legal profession followed the same pattern.
Bar associations across Britain, the United States, and continental Europe
formally prohibited women from practice until courts or legislatures intervened.
In the UK, women were not admitted to the legal profession until the Sex Disqualification (Removal) Act of 1919.
In the US, the Supreme Court upheld Illinois's exclusion of women from the bar in 1872,
with a concurrence that stated women's domestic roles were divinely ordained.
The formal barriers were eventually removed.
The informal barriers persisted:
partnerships that did not hire women,
chambers that did not take women as pupils,
and professional associations that did not see women as natural members.
These required decades more of pressure to dislodge,
and have not been fully dislodged.

The undercounting of women's scientific contributions is documented across many countries and disciplines.
The pattern includes attribution of women's work to male collaborators or supervisors,
systematic exclusion from authorship norms that credited the laboratory head
rather than the person who performed the experiments,
and deliberate suppression documented in specific cases
such as Rosalind Franklin's role in the determination of DNA's structure.
Studies of citation patterns, grant success rates, and peer review outcomes
continue to find systematic disadvantages for women researchers in many scientific fields,
controlling for measurable differences in output.

Mary Beard's analysis of women's exclusion from public speech
draws the pattern to its full historical length.
From the moment in the Odyssey where Telemachus tells Penelope to go back inside
and let men deal with public affairs,
through Roman rhetoric's treatment of women's public speech as inherently disgraceful,
through centuries of legal and customary prohibition on women speaking in court and in public assemblies,
the mechanisms of exclusion are remarkably consistent.
They include treating women's speech as categorically out of place in authoritative contexts,
dismissing or ridiculing women who do speak in those contexts rather than engaging with what they say,
and redefining the terms of authority in response to women's gains
so that what women achieve is always reclassified as less important than what they have not yet achieved.

In contemporary computing,
the primary mechanism of exclusion operates under the label of [%g culture_fit "culture fit" %].
Hiring decisions made on the basis of cultural fit are rarely experienced as discriminatory
by those who make them.
The judgment is framed as a question of whether a candidate seems like one of us,
whether they would enjoy working with the existing team,
whether they share the team's values and habits.
But when the existing team is demographically homogeneous,
hiring for cultural fit reproduces that homogeneity.
The criterion functions as a demographic filter while providing its users with a clean conscience.

The automation of hiring decisions does not solve this problem.
It replicates it at scale.
Algorithmic hiring tools trained on historical hiring data
learn to identify candidates who resemble those previously hired and promoted.
If the historical data reflects discriminatory patterns,
the algorithm encodes those patterns into a system that is harder to scrutinize and challenge
than a human decision-maker.
Amazon's internal recruiting tool, abandoned in 2018,
penalized resumes that included the word "women's"
and downgraded graduates of all-women's colleges,
because it had learned from a decade of prior hiring decisions that were heavily male.

The standard response to demographic imbalance in tech is to point to the pipeline:
not enough women or underrepresented minorities in computer science programs,
and the problem will correct itself when universities produce more qualified candidates.
This explanation is flatly contradicted by the evidence.
Women's participation in computing was substantially higher in the 1980s than it is today.
The decline in women's representation occurred
while women's representation in law, medicine, and other professions was increasing.
The pipeline analogy locates the problem in the wrong place.
Demographic problems that originate in hiring practices, retention conditions, and professional culture
cannot be solved by changing who enters the pipeline.
They require changing the conditions that determine who stays in,
who is promoted,
and who leaves.

[%b Becker1971 Banaji2013 Cassidy2025 McGhee2021 Wilkinson2011 Starr1982 Beard2017 %]
