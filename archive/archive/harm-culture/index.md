# Race, Culture, and Harm


## The Construction of Race

In 1950,
South Africa's apartheid government created the Race Classification Board
to assign legal racial categories to people whose status was ambiguous.
The examiners used what they called the pencil test:
if a pencil inserted into someone's hair stayed in place without falling,
the person might be classified as "Coloured" rather than "White."
They listened to accents,
examined fingernails for pigmentation,
and interviewed neighbors.
Families were split:
siblings were classified into different categories because they had inherited different combinations of features,
giving them different legal rights and permitted occupations,
and requiring them to live in different neighborhoods.

The pencil test is an extreme example of something that operates wherever racial classification exists:
a social and political determination dressed as a natural fact.
Race is not a biological category.
This is not a political opinion—it is the settled position of geneticists,
who have found more variation within conventionally defined racial groups than between them.
Race has been defined and redefined by specific people for specific political reasons.
Understanding how these categories are built, and by whom, is necessary for understanding
how algorithmic systems operate in societies organized around race and caste.
A system cannot be race-neutral or caste-neutral if it is trained on data generated
by institutions that were not.

Take the US Census Bureau's changing list of racial categories as an example.
In 1930,
Mexicans were for the first time classified as a separate racial category rather than white.
A decade later they were reclassified as white again
following diplomatic pressure from the Mexican government.
The category "Hispanic" does not appear in census data before 1970;
it was created by the Nixon administration to aggregate Spanish-speaking populations for federal programs.

The sociologists Michael Omi and Howard Winant called this process
[%g racial_formation "racial formation" %].
Irish immigrants in the 1840s appeared in popular cartoons as racially distinct from Anglo-Saxons,
while Italian immigrants in the early twentieth century were subject to legal discrimination
and extrajudicial violence partly justified on racial grounds.
Jewish people were categorized as a distinct race for purposes of immigration restriction
under the Johnson-Reed Act of 1924.
Each of these groups eventually became "white" through political processes
like labor organizing, military service, and suburban home ownership policies
that included them while excluding Black Americans
[%b OmiWinant2015 %].

A structurally identical process operated in colonial India,
where British census-taking hardened a complex system of
jati—locally variable occupational and kinship communities—into
a rigid administrative scheme derived from the four-varna hierarchy of classical Sanskrit texts.
Before the British began conducting censuses in the 1870s,
caste identity in most of India was locally negotiated, overlapping, and context-dependent.
A family might claim a higher jati status in one region than in another.
The colonial census required people to report a single affiliation from a fixed list,
ranked in a hierarchy that was presented as traditional but was
in practice imposed or interpolated by officials unfamiliar with local practice.

The jurist and social reformer B.R. Ambedkar,
who was himself from a Scheduled Caste community and who drafted independent India's constitution,
argued throughout his career that caste is not a natural feature of Hindu society.
He saw the colonial census not as a neutral enumeration of existing facts
but as a hardening of fluid social positions into legal permanence.
His arguments remain politically contested in India today,
which is itself evidence that caste is a political artifact.

The Mandal Commission of 1979 recommended reserving twenty-seven percent of central government jobs for Other Backward Classes.
There were widespread student protests when its recommendations were partially implemented in 1990.
The opposition was not to the existence of caste hierarchy as such;
tt was to the explicit acknowledgment of that hierarchy as the basis for redistribution.
Naming a constructed category in order to redress it is deeply uncomfortable
for the people advantaged by the original construction.
The same pattern has appeared in every country where affirmative action policies have been implemented:
defenders of the status quo claim that *they* are being discriminated against.

Isabel Wilkerson's *Caste* draws an explicit parallel between
the racial hierarchy of the United States, the caste system of India, and Nazi Germany's racial laws.
The three systems share structural features:
birth-based status that cannot be changed by individual achievement,
enforcement of endogamy (i.e., pressure or prohibition against intermarriage across boundaries),
and claims that contact with the lower caste or race will pollute those with higher status.
These systems aren't identical,
but understanding their similarities makes it easier to see features
that are easy to miss if each is treated as unique
[%b Wilkerson2020 %].

Which brings us to the algorithmic systems the tech industry is building.
They operate in a world where race and caste have been encoded into property records,
school funding formulas, arrest databases, and credit histories
through decades of explicitly discriminatory policy.
A hiring model trained on historical promotion decisions learns to prefer candidates
who resemble the people who were previously promoted,
in organizations that excluded people by race and class.
A recidivism prediction tool trained on arrest data learns patterns from policing decisions
that were themselves racially disparate,
and a content moderation system trained on human moderators' judgments
inherits their biases about whose speech is threatening and whose is merely passionate
[%b Kendi2016 %].

India's Aadhaar biometric identification system links fingerprints and iris scans
to a twelve-digit identifier for every resident.
It was presented as a race- and caste-blind system that would reduce discrimination
by making identity verification universal and objective.
In practice,
manual laborers whose fingerprints have worn smooth from physical work
cannot authenticate,
and rural residents without internet access cannot use online verification portals.
A system described as category-neutral still produces unequal outcomes
when the world it operates in is not
[%b Khera2019 %].

## The Taboos of Professional Culture

Every professional culture places certain topics outside the scope of legitimate concern,
and those who choose to discuss them publicly anyway
run the risk of being ostracized as radicals.
For example,
medicine was slow to discuss error and malpractice,
while law was slow to discuss access and cost.
A similar pattern is visible in the literature written for software engineers:
thousands of pages on management, leadership, and technical decision-making,
but almost nothing on workers' rights, collective action, or alternative ownership structures.
As with medicine and law,
the topics excluded are ones that threatened the interests of
the profession's most powerful practitioners.

[%b Douglas2002 %] argued that that what a group treats as taboo is not random.
Taboos cluster around the boundaries of the group itself:
what is forbidden defines who belongs and who does not,
what counts as legitimate thought,
and what marks the thinker as dangerous or confused.
The things placed out of bounds are therefore not those that threaten the group's members.
They are frequently the things that,
if examined,
would reveal tensions in the group's self-understanding or power structure.
The placement of a boundary is a form of power,
exercised by those with enough standing to enforce it.

Medicine's encounter with its own error rate is a case study in professional taboo and its eventual failure.
For most of the twentieth century,
the dominant framework for medical error was individual blame:
a bad outcome was the fault of a bad physician,
and the appropriate response was to identify and punish the individual.
This framework served the profession's interest in self-regulation and resisted external oversight.
The work of researchers like Lucian Leape,
and later the publication of [%b Kohn1999 %] by the Institute of Medicine in 1999,
reframed medical error as a systems problem.
The finding that between 44,000 and 98,000 Americans died annually from preventable medical errors
was not new to researchers,
but was taboo because it endangered the profession as a whole.

[%b Gawande2009 %] documents how aviation-style checklists,
which treat error as a predictable product of complex systems rather than individual failure,
were resisted for decades by physicians who experienced them as an affront to professional judgment.
The evidence that checklists reduced deaths in surgical settings was not in dispute.
The resistance was to the implication that a physician's individual competence and experience were insufficient,
and that standardized protocols designed by committees should constrain clinical practice.

The legal profession's relationship with access to justice follows a similar pattern.
Legal ethics in the United States has historically focused on conflicts of interest,
attorney-client confidentiality, and competence, but not on cost.
The profession's code of conduct treats affordability as a matter of individual attorney discretion
rather than a structural obligation.
This is not because access to legal representation is unimportant;
it is because the profession's wealthiest members *like* the current pricing structure,
and because defining access as a professional ethics problem
would require the profession to regulate itself
in ways that would reduce their incomes.
The explosion in legal costs over recent decades
has made the civil court system effectively inaccessible to most people in most disputes,
a situation that the profession has addressed primarily by wringing its hands.

I own over a dozen books on software engineering.
They covers project management,
software architecture,
team dynamics,
technical leadership,
career development,
and the business of startups.
What they do *not* cover is workers' rights in the tech industry,
the legal framework governing noncompete agreements and ownership of employee inventions,
alternative ownership structures like cooperatives and worker-owned firms,
or the systematic harassment and exclusion of women.
While it's common to hear people in Silicon Valley say that
we should keep politics out of programming,
these decisions about what to write (and read) are political:
it puts the interests of one set of stakeholders over another.

## The Moral Psychology of Building Harmful Things

In September and October 2021,
the Wall Street Journal published a series of articles
based on tens of thousands of internal Facebook documents provided by a former employee named Frances Haugen.
Among other things,
the documents showed that Facebook's own researchers had found that
Instagram worsened body image issues and increased suicidal ideation in teenage girls,
and that the company had known this for years while publicly denying that its platforms caused harm.
The documents also showed that Facebook's algorithms systematically promoted outrage and divisive content
because it generated more engagement,
and that internal teams had identified this as a serious problem without being able to change it.

None of this is surprising in retrospect.
What *is* surprising is how ordinary the behavior looks when you read the documents:
working groups, slide decks, and recommendations sent to committees.
The harm was not produced by villains.
It was produced by an organization operating in ways
that feel completely familiar.

The psychologist Stanley Milgram ran his obedience experiments at Yale in 1961 and 1962.
In the most famous version, subjects were told they were participating in a study of learning,
and were instructed by an authority figure to administer electric shocks
to another person whenever that person gave a wrong answer.
That "other person" was a confederate;
the shocks were fake,
and the screams were recorded.

Sixty-five percent of them administered
what they had been told was the maximum voltage—labeled "Danger: Severe Shock"—because
a person in a lab coat told them to.
Milgram's explanation was that people in hierarchical situations shift into an agentic state:
they stop regulating their own behavior against their personal moral standards
and start executing instructions from whoever they perceive as legitimate authority,
locating responsibility in the authority rather than in themselves
[%b Arendt2006 %].

The psychologist Albert Bandura identified eight mechanisms
by which people disengage their moral standards
to engage in or tolerate harmful behavior without feeling responsible for it.
[%g moral_disengagement "Moral disengagement" %] does not require cruelty or indifference.
It operates through cognitive reframing
that is available to people
who consider themselves good.
Moral justification frames the harm as serving a higher purpose,
while euphemistic labeling describes content moderation failures as "trust and safety challenges".
Advantageous comparison measures the harm against something worse
("At least we're not as bad as authoritarian governments"),
and displacement of responsibility points to someone else:
the advertisers demanded this, the users clicked on it.
[%g diffuse_decision_making "Diffusion of responsibility" %] distributes it across so many people
that no single one feels it:
the engineers wrote the algorithm, the product managers set the metrics, the executives approved the strategy.
Dehumanization of those harmed is rarely explicit,
but treating teenage users primarily as engagement statistics
accomplishes much of the same work
[%b Bandura1999 Palazzo2025 %].

<div class="callout" markdown="1">

The sociologist Diane Vaughan's analysis of the Challenger disaster identified a related mechanism
she called [%g normalization_of_deviance "normalization of deviance" %]:
the gradual process by which organizations come to accept risk thresholds
that would initially have been unacceptable,
through repeated exposure to near-misses
that did not immediately produce catastrophe.
NASA engineers had known for years that O-rings on solid rocket boosters failed in cold temperatures.
Each launch
that succeeded despite the problem
was treated as evidence that the problem was manageable.
The risk was not hidden:
it was documented, discussed, and progressively normalized.
The night before the Challenger launch,
engineers who understood the risk recommended against launching in cold weather.
Their recommendation was overruled by managers
who reframed the decision as requiring proof of danger rather than proof of safety.
No one decided to kill the seven astronauts who died the next day.
NASA had simply accumulated a set of practices that made the outcome possible
[%b Vaughan1996 %].

</div>

The Facebook documents are interesting partly
because they show several mechanisms working together.
Individual researchers and developers knew about specific harms and documented them.
Their documentation traveled upward through an organization
where each level had reasons like competitive pressure,
advertising revenue,
or political sensitivity to treat the problem as manageable
rather than as a reason to change the product.
By the time decisions were made at the level that could change the product,
the people making those decisions were insulated from the specific harms
by many layers of summary and abstraction.
They were also,
not coincidentally,
the people whose personal wealth was most directly tied to the metrics the product optimized.

The phrase "we just build hammers" is the most common form of moral disengagement in technology work.
It frames engineers as neutral suppliers of capability,
placing all responsibility for consequences on whoever chooses to use the tools
and however they choose to use them.
This framing collapses when you look at what the tools actually do.
A recommendation algorithm that is trained to maximize engagement
and deployed on a platform used by teenagers
is not neutral the way that a hammer is.
It is a system specifically designed to capture attention,
running on knowledge about how human psychology responds to certain kinds of content,
at a scale that no individual user can resist or comprehend.
The programmers who built it made choices about what to optimize,
and their bosses approved those choices.

The economist Albert Hirschman distinguished three responses available to people inside failing institutions:
exit (leaving), voice (speaking up), and loyalty (staying and tolerating).
The Facebook documents are a record of people choosing voice—writing memos,
flagging concerns,
recommending changes—and being answered with loyalty:
the problem is noted,
continue executing,
the strategy will not change.
Most of them stayed.
Their alternatives were limited:
mandatory arbitration clauses meant they could not easily sue,
non-disclosure agreements meant they could not easily speak,
and other large platforms were no better than Facebook.
Haugen's choice to leave and bring documents with her was unusual
precisely because the structural incentives pointed the other way.

None of this means that people inside organizations that cause harm are helpless.
It means that the conditions that produce harmful outcomes are predictable,
that they operate through ordinary human psychology rather than through exceptional malice,
and that understanding them is prerequisite to changing them.
Big tech's ethics boards
and principled statements about responsible AI
are no more meaningful than the diversity commitments they have spent the last couple of years ditching.
They are meant to soothe while leaving the incentive structures unchanged.
When the metrics that determine whether a career succeeds
are the same metrics that produce harm,
most people will find ways to make peace with the harm
[%b Ehmke2025 %].
