# Who Owns What


## Intellectual Property as Invention

Copyright, patent, and trademark are not natural rights:
they are legal instruments invented at specific times to serve specific interests.
The expansion of intellectual property rights over the past forty years was a deliberate political project,
pursued by specific industries,
over the objection of economists who predicted (correctly) that it would harm innovation.
Understanding this history is essential for evaluating current claims
about AI training data, open source licensing, and platform ownership of content created by users.

The Statute of Anne,
enacted in England in 1710,
is generally identified as the first copyright law.
It was not passed to protect authors,
but to end a monopoly held by the London Stationers' Company,
a guild of printers that had controlled the trade in printed books since the sixteenth century,
and to create a new system of publisher monopolies that would operate for limited terms.
Authors received rights in the statute,
but only to the extent that they assigned those rights to publishers,
who were the real beneficiaries of the act.
The framing of copyright as a natural right of creators,
which dominates popular and political discussion today,
was a later construction that reversed the actual historical origin
[%b Bracha2019 %].

Patent and copyright terms have been extended repeatedly,
almost always to be longer, broader, and allow fewer exceptions.
United States copyright terms have moved from 14 years under the Copyright Act of 1790
to the current life-plus-70 years.
(The 1998 Sonny Bono Copyright Term Extension Act was timed
to prevent the earliest Mickey Mouse films from entering the public domain.)
Patent terms have been less dramatically extended,
but the scope of what is patentable has expanded substantially,
particularly with the rise of software patents.
Each extension was the result of lobbying by specific industries,
over the objections of economists
who consistently argued that the existing terms were already longer than necessary to incentivize creation.

<div class="callout" markdown="1">

Pharmaceutical companies have been extremely effective at shaping intellectual property law globally.
Beginning with the Agreement on Trade-Related Aspects of Intellectual Property Rights (TRIPS) in 1994,
high-income countries required all members of the World Trade Organization
to adopt patent standards that matched or exceeded their own.
Countries that had deliberately excluded pharmaceutical products from patentability
in order to build domestic generic drug industries,
including India, Brazil, and several African countries,
were required to change their laws.
The result was a substantial transfer of rents to pharmaceutical companies operating in rich countries,
and a significant increase in drug prices in countries that could least afford them.

</div>

Software patents are a category of intellectual property right
whose practical operation differs substantially from the stated purpose of the patent system.
The original argument for patents is that they encourage disclosure:
an inventor gets a time-limited monopoly
in exchange for publishing a description of the invention
sufficient to allow others to replicate it after the term expires.
In contrast,
software patents are often written at high levels of abstraction,
covering broad categories of computational method rather than specific implementations.
They are concentrated in the portfolios of large technology companies, financial institutions,
and [%g patent_assertion_entities "patent assertion entities" %]:
organizations that hold patents without producing anything,
but derive revenue entirely from licensing and litigation.
Software patents are used primarily against smaller companies and open source projects,
which lack the resources to defend extended litigation.

Open source licensing emerged in part as
a response to the expansion of intellectual property rights over software.
The [%g gpl "GNU Public License" %] (GPL) and its relatives use copyright law against itself:
the license grants broad permissions
that apply only on the condition that derivative works carry the same license,
making it legally difficult to take open source software and close it.
This kind of [%g copyleft "copyleft" %] has only been a partial success:
big tech companies have learned to extract enormous value from open source software
while contributing relatively little back,
because their primary product is not the software but the service running on it
[%b Doctorow2022 Baldwin2014 Bellos2024 %].

## Setting the Standard

In May 1886,
American railroads completed the largest coordinated industrial operation the country had seen.
Over two days,
work crews across the South pulled up thousands of miles of track
and relaid it three inches closer together,
converting the region's idiosyncratic gauge to match the rest of the country.
The process was planned, organized, and executed in less time than most tech companies take
to schedule a product launch.

The southern railroads had resisted this change for decades
because the incompatibility was not an accident.
Different gauges meant that northern rolling stock could not run on southern track,
so freight crossing a gauge boundary had to be unloaded, transferred, and reloaded.
Every cargo shipment lost time and money at the border,
and that money went to the carriers who controlled the boundary.
The technical choice was a market weapon.

A [%g standards_body "technical standard" %] is an agreement about how things connect.
The value of having a standard usually far exceeds
the value of any particular outcome in the format war that precedes it,
which is exactly why control of the format is worth fighting for.

Thomas Edison understood this in the 1880s,
when he and George Westinghouse fought over whether the United States would run on direct or alternating current.
Edison had bet on DC infrastructure and stood to lose if AC won,
so he electrocuted animals at exhibitions
and lobbied for AC to be used in the first electric chair,
hoping to fix the association of alternating current with execution in the public mind.
None of this changed the underlying physics, though;
AC transmits over longer distances at lower cost,
and Westinghouse won.

A century later,
Microsoft repeatedly used [%g standards_capture "standards capture" %] as a business strategy.
The company would adopt an open standard like HTML, Java, or Kerberos authentication,
and then add proprietary extensions that were convenient but tied developers to Microsoft's version.
Once enough code was written against the extensions,
[%g interoperability "interoperability" %] with non-Microsoft systems degraded.
The strategy had a name inside the company: embrace, extend, extinguish.
(The "extinguish" referred to both the open standard and Microsoft's competitors.)
[%b Russell2014 %]

Google's Accelerated Mobile Pages, launched in 2015,
was presented as an open standard for fast-loading mobile web pages.
To receive preferential treatment in Google's mobile search results,
however,
pages had to be hosted on Google's own servers and delivered through Google's infrastructure.
Publishers who adopted AMP handed Google control over their content delivery
in exchange for a favorable page rank.
Google eventually backed away from the hosting requirement,
but only under regulatory pressure.

Apple took a different approach.
Rather than capturing an open standard, it simply refused to implement one.
RCS is a modern successor to SMS that supports end-to-end encryption,
read receipts,
high-resolution media,
and group chat.
For years after Android phones had adopted it,
Apple kept cross-platform messaging on unencrypted SMS,
so messages between iPhones and Android phones appeared as green bubbles.
Internal documents revealed in US antitrust litigation showed Apple executives explicitly acknowledging
that adopting RCS would reduce the social cost of switching from iPhone to Android,
particularly for teenagers for whom the green-bubble distinction had become a social marker.
The EU's Digital Markets Act eventually compelled Apple to support RCS in 2024.

When a technology becomes embedded in a formal standard,
the patent holder typically commits to license it on [%g frand "FRAND" %] terms:
fair, reasonable, and non-discriminatory.
This sounds reassuring,
but the word "reasonable" has funded decades of litigation.
Qualcomm's licensing practices for mobile baseband patents
(the technology that connects a phone to a cellular network)
were subject to antitrust proceedings simultaneously in the United States, Europe, South Korea, China,
and Taiwan in the late 2010s.
The core allegation was consistent across jurisdictions:
Qualcomm was using its position as the patent holder
o charge fees that bore no relationship to any recognizable interpretation of "reasonable."
The legal outcomes varied by country;
Qualcomm remained profitable throughout.

<div class="callout" markdown="1">

During the browser wars of the late 1990s,
Microsoft bundled Internet Explorer with Windows,
deliberately undercutting Netscape's business model.
IE's market dominance then allowed Microsoft to implement proprietary HTML extensions
that worked only in its browser.
What finally broke this cycle was not antitrust action—which produced a consent decree
and little structural change—but the arrival of Firefox and then Chrome,
backed by organizations with different incentives.

</div>

If you are a developer building a product,
every choice between an open standard and a proprietary API is
a bet on the future behavior of the platform that owns the API.
History suggests the bet is a bad one.
From Instagram's third-party API and Twitter/X's developer API
to Google Reader and Firebase's original pricing structure,
platforms have repeatedly changed terms after developers are so invested that they can't walk away.
Each time,
the platform points to its terms of service,
which always reserves the right to change.

The structural remedy for this is interoperability mandates:
legal requirements that platforms accept connections from competing services
on terms that do not depend on the platform's goodwill.
Phone number portability,
which required carriers to let customers keep their numbers when switching providers,
eliminated one of the most effective lock-in mechanisms in telecoms.
Messaging interoperability requirements in the EU's Digital Markets Act
are attempting to do the same thing for social platforms.
Whether they succeed depends on implementation details that are actively contested,
and on enforcement that companies have historically resisted every way they can
[%b Shapiro1999 Wu2010 %].

## Public Subsidy, Private Profit

When Steve Jobs unveiled the iPhone in January 2007,
the crowd responded as if Apple had conjured something from nothing.
What neither Jobs nor the press mentioned was that
every technology in that device had been developed with government money.
The internet it connected to had been built by the Defense Advanced Research Projects Agency.
The GPS it used had been developed and maintained by the US Air Force,
which had turned off the deliberate signal degradation for civilian users only seven years earlier.
Its touchscreen came from research supported by the National Science Foundation,
which Apple had acquired by buying a small company called FingerWorks in 2005.
Siri, added to the iPhone 4S in 2011, had started as a DARPA-funded project at SRI International.
The government took the risk;
the investors who held Apple stock reaped the benefits.

This pattern is not unique to Apple.
The internet began as ARPANET, a network funded by the Department of Defense from 1969
to connect university research computers.
The initial packet-switching protocols,
the domain name system,
and the basic architecture of what became the web
were all developed in publicly funded laboratories and universities.
The commercial internet of the 1990s built on this foundation without paying for it.
The browser itself emerged from the National Center for Supercomputing Applications,
funded by the National Science Foundation.
Mosaic was not a startup product:
It was a research project paid for by American taxpayers.

The drug industry runs the same arrangement at enormous scale.
The National Institutes of Health spends roughly $47 billion annually on biomedical research.
Much of this money funds the basic science
that pharmaceutical companies would not fund themselves because the returns are too distant and uncertain.
When that basic science produces a promising compound,
private companies license it, conduct clinical trials, and patent the result.
The public paid for the underlying knowledge.
The private company captures the patent and sets the price.
Unlike every other wealthy country.
the United States has no legal mechanism to negotiate that price.
As a result,
insulin costs American patients ten times what Canadians pay.

<div class="callout" markdown="1">

The mRNA vaccine platform that produced the Pfizer-BioNTech and Moderna COVID-19 vaccines
illustrates this dynamic precisely.
The fundamental science of mRNA delivery
was developed over decades by Katalin Karikó and Drew Weissman at the University of Pennsylvania,
supported by the National Institutes of Health.
When COVID-19 hit,
the US government funded the clinical trials and pre-purchased hundreds of millions of doses
before any vaccine had received authorization.
The government provided the science, the capital, and the guaranteed market.
Moderna became a $200 billion company,
and its executives became very rich.
The NIH's claim to a share of the intellectual property—which
would have given the government some leverage over pricing—was
disputed by Moderna and ultimately not enforced.

</div>

The economist Mariana Mazzucato has called this arrangement
the privatization of gains and the socialization of losses.
Her argument is not that private companies add no value:
they obviously do, in manufacturing, distribution, and application.
Her argument is that
the standard story of heroic private entrepreneurs taking risks that timid governments would never accept
inverts the actual history.
Governments took the foundational risks
by funding research that might produce nothing,
maintaining infrastructure that would not attract private capital,
and training the scientists and engineers that firms would later hire.
Technology transfer moves the results into private hands,
almost always at prices that dramatically undervalue the public's investment
[%b Mazzucato2013 %].

The tech companies that have benefited most from publicly funded research
are also among the most sophisticated users of international tax structures
designed to minimize what they pay back into the public systems that enabled them.
Apple's arrangements in Ireland,
described in a 2016 European Commission ruling,
allowed the company to pay an effective tax rate of 0.005% on European profits.
Over and over,
public investment creates the technology,
private firms capture the profits,
and international tax structures ensure that
only a tiny fraction of those profits flow back into the public budget.
The cycle is effectively a permanent subsidy.

The arrangement looks different in Europe,
partly because European governments built in mechanisms that Americans left out.
Germany's Fraunhofer-Gesellschaft,
a network of applied research institutes funded jointly by the federal government,
state governments,
and industry,
licenses its discoveries under terms that return revenue to the institutes themselves
rather than transferring intellectual property to private buyers at knockdown prices.
The European Medicines Agency negotiates drug prices on behalf of member states,
which is why the same cancer drugs that cost American patients six figures a year
cost Germans and French patients a fraction of that.
When Moderna tried to sell COVID-19 vaccines to the European Union,
EU negotiators paid roughly half the per-dose price that American buyers paid,
for the same product developed with the same publicly funded science.
The European model still lets private firms profit substantially from public investment.
What it does not do is treat the transfer as a gift.

China has taken a third path that makes the American arrangement look like an oversight rather than a design.
Programs like Made in China 2025, announced in 2015,
identify strategic industries like semiconductors, electric vehicles, robotics, and artificial intelligence,
and pour in state capital with the explicit goal of domestic ownership of the results,
not just the benefits.
Companies like CATL,
which now supplies roughly a third of the world's electric vehicle batteries,
grew to global scale with protected home markets and state-backed financing before competing internationally.
The distinction between public and private in this system is deliberately blurry:
the government can require access to technology developed with state support,
block the international transfer of profits,
and redirect corporate strategy in ways that American or European regulators legally cannot.
This does solve the problem Mazzucato describes,
since the state that takes the foundational risk never fully loses its claim on the result.
It creates a different problem, though:
accountability runs upward to the Communist Party rather than outward to citizens,
and the line between a national champion and an instrument of state policy disappears entirely
[%b Chang2012 Acemoglu2023 Webber2011 %].

## International Tax Avoidance

In August 2016,
the European Commission ordered Apple to repay thirteen billion euros in back taxes to Ireland.
The commission had investigated Apple's tax arrangements in Ireland
and concluded that they amounted to illegal state aid:
Ireland had given Apple a selective advantage unavailable to other companies,
allowing the company to pay an effective tax rate of 0.005% on European profits
of sixteen billion euros in 2014.

The Irish government was ordered to collect the money,
and promptly announced it would appeal the ruling.
Ireland did not want the thirteen billion euros;
its government argued in court,
alongside Apple,
that the commission had made an error.
This only baffled the cynical:
Ireland's unusually favorable tax treatment of multinationals was a deliberate policy
to attract foreign companies.

The mechanism Apple used was a variant of a structure known as the Double Irish,
which Irish tax law had made available through a combination of
specific provisions and deliberate regulatory tolerance.
Ireland taxes companies that are managed and controlled from Ireland.
The United States taxes companies incorporated in the United States.
Apple's Irish subsidiaries
were incorporated in Ireland but had their management and control located outside Ireland,
so Ireland did not tax them.
They were also not incorporated in the United States, so the US did not tax them either.
At its peak, this arrangement sheltered tens of billions of dollars annually.

The intellectual property component made the structure self-sustaining.
Apple's valuable patents were licensed from a subsidiary in a low-tax jurisdiction.
European sales flowed through Apple Sales International,
which paid royalties back to the IP-holding entity.
The royalties reduced taxable profit in the high-tax jurisdictions where the sales occurred.
[%g transfer_pricing "Transfer pricing" %]
(the setting of prices for transactions between subsidiaries of the same company)
is supposed to follow the arm's length principle:
the price should be what unrelated parties would charge each other.
In practice, there is no market price for a license to Apple's entire product ecosystem,
so whatever number Apple's accountants put in the contract became the price.
Tax authorities in each country then had to prove the price was wrong,
which requires the kind of information that companies are not generally eager to provide.

Apple was not alone, and Ireland was not the only country involved.
The Dutch Sandwich added a Netherlands entity to the structure,
exploiting a Dutch tax provision that exempted certain royalty payments from withholding tax.
Royalties would flow from Ireland to the Netherlands,
then onward to the zero-tax jurisdiction,
each step reducing the amount captured by any jurisdiction that might want to tax it.
Luxembourg served a similar function for Amazon;
by putting its European headquarters there,
the company could book sales across the continent while keeping profits in a jurisdiction
that had negotiated unusually favorable rulings with dozens of major multinationals.
Google's arrangement was so elaborate to have its own nickname:
the Double Irish with a Dutch Sandwich.

<div class="callout" markdown="1">

The offshore financial system that made these structures possible has deeper roots than tech.
The Cayman Islands established themselves as a financial center in the 1960s
through legislation specifically designed to attract capital seeking freedom from tax and regulation.
By 2016,
the Cayman Islands hosted more than 100,000 registered companies despite a population of 60,000 people.
Switzerland's banking secrecy,
formalized in 1934,
protected foreign depositors from the tax authorities of their home countries for decades.
Luxembourg,
the Netherlands,
Ireland,
and Singapore all competed to attract corporate headquarters and intellectual property holdings
through combinations of favorable rulings and light regulation.
None of this was invented by tech companies,
but they used it on a larger scale than almost anyone before them.

</div>
[%b Shaxson2011 %]

The OECD's BEPS project,
launched in 2013,
produced a fifteen-point action plan to close these loopholes.
Countries that adopted its recommendations
were supposed to require substance in the jurisdictions where companies claimed tax residence,
limit the deductibility of interest payments used to shift profits,
and require country-by-country reporting to  make the overall structure visible.
Ireland amended its tax law in 2015 to prevent new companies from using the Double Irish structure,
but gave companies already using it a five-year phase-out period.

The 2021 agreement among 136 countries on a global minimum corporate tax rate of 15%,
negotiated under OECD auspices,
went further than any previous multilateral effort.
It established the principle that no matter where a multinational's profits were booked,
at least 15% would be paid somewhere.
The agreement was called historic,
which was accurate,
and transformative,
which was not,
since implementation depended on each country passing domestic legislation.

Gabriel Zucman's estimates suggest that
roughly 40% of multinational profits are shifted to [%g tax_haven "tax havens" %] annually,
costing governments approximately $200 billion per year in corporate tax revenue.
This is money that does not fund schools,
infrastructure,
or healthcare in the countries where the economic activity actually occurred.
The companies that benefit from this system defend it as legal, which it is.
They also describe it as responsible tax planning,
which is a creative use of the word responsible
[%b Zucman2015 Schneier2023 %].
