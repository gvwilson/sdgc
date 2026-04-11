# Money, Monopoly, and Bubbles


## The Creation of Money

In the 1660s,
London merchants who needed somewhere safe to store their gold and silver
began using the vaults of goldsmiths,
who already had the locks and the reputation.
The goldsmith would issue a paper receipt;
merchants quickly discovered that it was easier to pay each other with receipts
than to cart metal through the streets.
The receipts circulated as currency.

The goldsmiths making these transactions noticed that
at any given time,
only a fraction of depositors came to claim their metal.
The rest left it in the vault, trusting the paper.
A goldsmith willing to issue *more* receipts than he actually had gold in the vault
could lend out the extras and collect interest,
as long as depositors never all came at once.
This is the origin of fractional reserve banking,
a name that makes it sound more principled than it is.

This matters for understanding the modern financial system
because the same basic mechanism is still operating,
at much larger scale,
with slightly more oversight,
in digital form.
The story is also the origin of the periodic bank run:
when depositors suspect the receipts exceed the gold,
everyone tries to claim their metal at once,
which confirms the suspicion,
which guarantees the collapse.
In September 2007,
people queued outside branches of Northern Rock, a British mortgage lender,
for three days—the first run on a British bank in 150 years.
The queues were orderly and very British,
but the mechanism was identical to panics that had destroyed banks in Amsterdam in 1763,
in the United States repeatedly between 1873 and 1907,
and in Argentina in 2001.

In 2014,
the Bank of England published a paper with the dry title
"Money Creation in the Modern Economy."
Its core claim was not subtle:
when a commercial bank makes a loan,
it does not lend out money that was previously deposited.
It creates the deposit simultaneously with the loan.
The loan and the deposit appear on the bank's books at the same moment.
Money that did not previously exist comes into existence through the act of lending.

This is just as ridiculous as it sounds, but very useful.
When you repay a loan,
the deposit disappears from your account and the corresponding debt disappears from the bank's books.
Money is destroyed.
The money supply—the total amount of deposits in the economy—expands when banks are lending
and contracts when loans are being repaid or written off.

The 2008 financial crisis makes more sense through this lens.
When house prices fell, mortgage-backed securities lost value.
Banks had to recognize losses on assets they held.
To maintain their required capital ratios,
they had to stop making new loans and call in existing ones.
This made the money supply contract,
which meant less money available for businesses to borrow,
workers to spend,
and consumers to use to repay their debts.
The financial crisis became an economic crisis not through some mysterious contagion
but through the straightforward mechanism of money destruction.
Governments and central banks responded with quantitative easing:
central banks created new money by purchasing assets from banks,
replacing the money that bad loans were destroying.
This is why central banks can "create money" without necessarily causing inflation
when the money supply is contracting—they are filling a hole
[%b McLeay2014 %].

The anthropologist David Graeber spent years studying debt across cultures and centuries.
In *Debt: The First 5,000 Years*,
he showed that the story economists tell about money—that barter came first,
that money was invented to make barter easier,
and that credit developed on top of money—has
almost no support in the historical or anthropological record.
The fish-for-axes economy that appears in introductory economics textbooks
has never actually existed anywhere.
What appears in the record instead are systems of mutual obligation and accounting:
I owe you,
you owe me,
the village keeps track.
Credit relationships,
Graeber argued,
are older than markets and older than money.
Money emerged not to simplify barter but to settle and record debts
[%b Graeber2011 %].

Graeber's insight matters here because it reframes what a bank actually is.
A bank is not a warehouse that stores your money and lends it out.
It is an institution with the power to create new obligations—to say "I owe you this"
in a form that the recipient can treat as equivalent to goods or labor.
That power is not derived from having gold in a vault.
It is derived from legal recognition,
regulatory framework,
and the collective social agreement
that a bank's promises are worth treating as money.

Who gets to issue these promises,
and under what constraints,
are political questions.
Andrew Jackson ran his 1832 presidential campaign substantially on the question
of whether a private institution (the Second Bank of the United States) should have the power
to create the country's money.
He won,
and the financial panics that followed
eventually produced the Federal Reserve Act of 1913,
which as passed in the aftermath of the 1907 panic
to give the money-creation system a lender of last resort.

Contemporary fintech companies are participating in this long argument
without usually acknowledging it.
Klarna, Afterpay, and Affirm extend credit to consumers at the point of purchase.
In doing this they are creating money,
but they are doing it without the deposit insurance,
capital requirements,
or regulatory oversight that apply to licensed banks.
PayPal holds tens of billions of dollars in customer balances that do not carry deposit insurance,
and Stripe extends credit to merchants.
These companies are, in each case, capturing the profit of money creation
while avoiding the obligations that historically came with it—the same maneuver
that London goldsmiths discovered in the 1660s.

Cryptocurrency takes this further.
Bitcoin and its successors are explicit attempts to create parallel monetary systems outside state control,
with the money-creation mechanism determined by algorithm rather than central bank policy.
The technical design is genuinely novel.
The social question it raises is not:
who gets to create money and who bears the losses when it goes wrong.
If the past is any guide,
the answer to the latter question is, "Not the bankers."
[%b Kindleberger2005 Chang2012 %]

## Big Tech is Like Standard Oil

Venture-funded platform competition is a [%g tontine "tontine" %].
In European finance from the seventeenth through the nineteenth centuries,
a tontine was a pooled investment in which,
as each subscriber died,
the remaining subscribers' shares increased,
with the last survivor inheriting the entire fund.
Most governments eventually banned tontines because they created obvious incentives
to hasten the death of other participants.

In platform competition,
the explicit goal from the first investment round
is to be the one platform that achieves dominance while all competitors fail.
Operating below cost to build market share,
sometimes for years,
makes financial sense
if it eliminates alternatives and enables the extraction of monopoly rents afterward.
Investors who hold positions in multiple competing platforms profit regardless of which one wins;
the workers, users, and communities that depended on those platforms do not.

The life cycle of a dominant firm in a network industry follows a pattern:
enter the market with a genuinely useful product,
use that position to acquire or drive out competitors,
then extract maximum value from the resulting captive market.
Standard Oil, railway companies, the Bell telephone system, cable television,
and major record labels all followed this playbook.
The constraints that eventually constrained them
were the result of political struggles that the industries fought at length.

At its peak,
Standard Oil controlled roughly ninety percent of US oil refining capacity.
It didn't achieve this through superior efficiency
but through secret railroad rebates,
[%g predatory_pricing "predatory pricing" %] against competitors,
and strategic acquisitions of rivals.
The Sherman Antitrust Act of 1890 was written in direct response,
and the landmark 1911 Supreme Court decision that broke Standard Oil into thirty-four separate companies
is often cited as the definitive antitrust remedy.
What is less often noted is that several successor companies immediately reconsolidated,
and that John D. Rockefeller's personal fortune *increased* after the breakup
as the stock prices of the subsidiaries rose.
The remedy addressed the legal structure of the monopoly
without fundamentally altering the underlying concentration of wealth or market power
[%b Stoller2019 %].

The Standard Oil breakup points toward a limit that antitrust has not resolved:
separating a company into parts does not eliminate coordination between those parts.
Japan's prewar zaibatsu were family-controlled conglomerates
combining a bank, a trading company, and manufacturing enterprises across multiple industries.
The bank provided capital to affiliated companies on terms unavailable to competitors;
the trading company controlled export markets;
profitable units cross-subsidized struggling ones during competitive battles.

The American occupation dissolved the zaibatsu after 1945.
Within a decade, the keiretsu emerged:
networks of former zaibatsu firms coordinated through mutual shareholding,
preferential supply relationships, and regular executive meetings.
The legal structure of centralized control had been dismantled,
but the practical coordination continued in a different form.

The Bell network evolved along slightly different lines than Standard Oil.
AT&T's control over telephone infrastructure from the 1910s until its breakup in 1984
was maintained by a [%g regulatory_compact "regulatory compact" %]
in which AT&T accepted rate regulation in exchange for a protected monopoly position.
That compact produced genuine achievements:
Bell Labs generated an extraordinary concentration of fundamental research,
including the transistor, the laser, information theory, and Unix.
It also suppressed the development of competitive long-distance service
and technologies that threatened the core telephone business
[%b Wu2010 %].

The British railway mania of the 1840s followed the same cycle earlier and more visibly,
as the [Fads and Bubbles](@/fads/) chapter describes.
The consolidation that followed produced a small number of large regional monopolies.
Parliament responded with rate controls and mandated third-party access to track,
which the railway companies contested for decades,
making the same arguments that social media and AI companies make today:
the industry was too complex to regulate effectively,
regulation would destroy investment incentives,
and the market would eventually take care of things anyway.

[%g network_effects "Network effects" %] and [%g switching_costs "switching costs" %]
are what make monopolies in network industries self-reinforcing.
A telephone network becomes more valuable as more people join it,
giving the dominant network an advantage separate from the quality or price of the underlying service.
Switching costs compound this:
users who have built workflows and contact lists around a platform
can't afford to move to a competitor even when the competitor offers a better product.

The resulting cycle—subsidize users, lock them in, then extract value by degrading service—
is the subject of the [Enshittification](@/enshittification/) chapter.

Antitrust law in the United States was supposed to prevent this.
Beginning in the 1970s,
however,
it was weakened by a legal school associated with the University of Chicago
that argued courts should evaluate mergers solely on whether they reduced consumer welfare in the short run.
Under this standard,
acquisitions of nascent competitors were not anticompetitive
if the acquired company had not yet raised prices.
Platform companies used this framework to acquire dozens of potential competitors
before they could grow large enough to threaten market share.
The current debate over platform regulation is therefore partly a debate about
whether antitrust law should return to its original concern with concentration of power.

<div class="callout" markdown="1">

China's market regulator fined Alibaba ¥18.2 billion in 2021 for its "either-or" practice
of requiring merchants to sell exclusively on Alibaba platforms on penalty of losing favorable placement—
identical in structure to Standard Oil's railroad rebate agreements,
which penalized shippers who used competing lines.

</div>

[%b Doctorow2025 %]

## Enshittification

In 2005, a Dutch startup called Booking.com offered hotels a deal:
list your rooms on our platform for a 12% commission,
and we will send you customers you would not otherwise reach.
Hotels signed up;
travelers followed, because the inventory was there,
and by the early 2010s,
Booking.com was the dominant hotel search platform across Europe and much of Asia.

Then the commissions started climbing.
By 2019, many hotels were paying 25-30% per booking,
plus additional fees for "preferred placement" near the top of search results.
Hotels that declined to pay for placement found themselves buried behind those that did.
The traveler experience degraded too:
search results increasingly reflected who had paid for prominence,
not which hotel best matched the search.

Hotels understood what had happened,
but they were locked in.
Their repeat customers now booked through Booking.com rather than directly,
because that was where travelers looked.
A hotel that left the platform did not take its customers with it—those
relationships belonged to the platform.
Leaving meant losing access to a market the platform now controlled.

Cory Doctorow named this pattern [%g enshittification "enshittification" %].
A platform enters a market by offering a service below cost to build a user base.
Once users are locked in,
it begins subsidizing business customers,
using the captive user base as leverage.
Once business customers are also locked in,
it harvests both by
degrading service quality,
raising prices,
and extracting the maximum value from a market it now controls.
The platform can do this because the switching costs that lock users in
also protect it from competitive consequences
[%b Doctorow2022 %].

Enshittification depends on two things:
network effects and [%g structural_lock_in "structural lock-in" %].
Neither is not specific to digital platforms.
The record club Columbia House ran the same play in a different era.
Launched in the 1950s in the United States and Canada
and later extended to the United Kingdom, Australia, and Brazil,
it offered new members twelve records or cassettes for a penny.
The first transaction was a real deal.
The extraction came later:
members committed to purchasing eight more titles at "regular club prices,"
which were two to three times the retail price of the same albums in a shop.
If a member forgot to decline the monthly selection,
it arrived automatically and the cost appeared on their bill.
The penny offer built the membership;
the commitment structure extracted the value.
Columbia House recruited around sixteen million members in the United States alone
before the model collapsed when digital music eliminated the inventory advantage.

<div class="callout" markdown="1">

In 1986, a corporation better known for making women's underwear
acquired JanSport and, over the following decades,
bought nearly every backpack brand with a reputation for durability.
Controlling more than half the US backpack market,
it had no competitive pressure to maintain quality.
Fabric thickness dropped, cheaper zippers replaced better ones, and stitching density fell.
The products looked identical on the shelf;
customers discovered what they had actually bought when the stitching pulled apart at the stress points.

JanSport continued to advertise a lifetime warranty,
and the suggestion "just use the warranty" sounds entirely reasonable.
In practice, using it required paying $12 to $25 in return shipping,
waiting three to six weeks,
and arguing that a failure qualified as a "defect in materials and workmanship"
rather than "normal wear and tear."
(The warranty language was not incidental;
it was written to exclude precisely the kind of failure
that was now designed into the product.)
One customer,
when told their zipper failure was wear and tear,
got quotes of $50 to $100 from local tailors,
then bought a used bag at a thrift store for four dollars rather than a new one.

</div>

Grab, the ride-hailing and delivery platform dominant across eight countries in Southeast Asia,
followed the same trajectory at scale.
It entered markets including Malaysia, Indonesia, Vietnam, Thailand, and the Philippines
with driver incentives and passenger subsidies
that made rides cheaper than local alternatives.
It acquired Uber's Southeast Asian operations in 2018,
eliminating its main competitor outright.
With competition gone,
driver commissions rose and passenger fees increased.
The platform began requiring restaurants and drivers to pay for placement
in its food-delivery and services listings.
The pattern was identical to Booking.com's,
conducted in markets where regulatory capacity to respond was considerably thinner.

Investor dynamics accelerate enshittification.
Platforms in their subsidy phase operate at significant losses,
funded by venture capital in expectation of eventual monopoly returns.
Once the platform achieves dominance,
those investors demand extraction.
Losses during the subsidy phase are booked as investment;
extraction during the harvest phase is booked as profit.
The users who benefited from below-cost service in year one
fund those returns in year ten.

Antitrust enforcement has provided limited relief.
Because acquisitions of potential competitors are evaluated on
whether they raised consumer prices immediately—not
whether they reduced competition structurally—dominant platforms can acquire dozens of rivals
before those rivals threaten their market share.
The result is that enshittification faces no real competitive check:
alternatives are acquired or driven out during the subsidy phase.

Two structural interventions *have* produced results.
The European Union's Digital Markets Act,
which took effect in 2024,
requires platforms designated as "gatekeepers"
(those with market capitalizations above €75 billion
or monthly user bases above 45 million in Europe)
to allow interoperability with competing services,
to refrain from self-preferencing their own products in search results,
and to allow users to uninstall pre-installed software.
Fines for non-compliance reach 20% of global revenue.
The act is the first regulatory framework
designed specifically around the leverage that platform dominance creates,
rather than around the consumer prices those platforms charge.

India's Unified Payments Interface uses a different model:
intervene before dominance rather than after.
Instead of regulating private platforms that have already achieved lock-in,
India built public payment infrastructure
that any platform can connect to on equal terms.
Google Pay, PhonePe, and Paytm compete on the same rails;
none owns the customer relationship—that belongs to the user's bank account.
No single platform can raise fees on the underlying infrastructure
because the infrastructure is public.
Brazil's Pix system follows similar principles,
as do comparable approaches adopted by central banks in Ghana and Sri Lanka.
The question today is not whether enshittification can be stopped,
but why regulators in Canada, the US, and elsewhere choose not to stop it
[%b Shapiro1999 Sapp2026 %].

## Fads, Bubbles, and the People Who Should Have Known Better

In February 1637, a single bulb of the Semper Augustus tulip sold in Amsterdam
for the price of a house on a canal.
If you had bought one of those bulbs in November 1636 and sold it in January 1637,
you would have tripled your money.
If you held it until March, you were ruined.

Tulip mania is the most entertaining entry in the catalog of financial bubbles
because it involves flowers.
But the mechanics are identical to what happened in 1720 with South Sea Company shares,
in the 1840s with British railway stocks,
in the 1980s with Japanese real estate,
in 1999 with dot-com IPOs,
in 2006 with Florida condos,
and in 2021 with NFTs.

<div class="callout" markdown="1">

Japan's stock and real estate bubble peaked in December 1989—
when the Nikkei index hit 38,915 and Tokyo land was theoretically worth more than all US real estate—
and was followed by thirty years of stagnation
that every mainstream forecast predicted would end within a few years,
which is what "this time it's different" sounds like from the inside.

</div>

The first thing to understand about a bubble is that it is not entirely irrational
while it is happening.
Tulips *were* genuinely scarce and genuinely fashionable.
Railway technology *was* genuinely transformative,
and the internet *did* change commerce.
Every bubble grows from a real phenomenon,
which is precisely what makes it so effective at separating people from their money.

The second thing is [%g greater_fool_theory "the greater fool theory" %].
You do not have to believe that a tulip bulb is worth a house.
You only have to believe that someone else will pay you more for it next month
than you paid for it today.
This is rational behavior when prices are rising,
but disastrous the moment they stop.

[%b Mackay1841 %] documented this pattern in 1841,
which remains readable and depressing because every pattern he identified is still with us.
Isaac Newton, one of the smartest people who ever lived,
lost the equivalent of several million dollars in the South Sea Bubble of 1720.
He reportedly said afterward that he could calculate the motions of heavenly bodies,
but not the madness of men.
He had already sold his shares at a profit,
watched the price continue rising,
bought back in near the peak,
and then watched it collapse.

Robert Shiller, who won a Nobel Prize partly for studying this problem,
argues that markets are driven less by rational calculation than by contagious stories [%b Shiller2015 %].
He calls this [%g narrative_economics "narrative economics" %]:
when a compelling story spreads through a population,
it changes behavior,
and changed behavior changes prices,
which seems to confirm the story,
so it spreads further.
This feedback loop is difficult to interrupt because
the people caught up in it are not obviously doing anything wrong.
They are listening to their neighbors,
watching prices,
reading the news,
and making bets based on the best available information.
The information just happens to be mostly about what other people are betting.

The British Railway Mania of the 1840s combined technological innovation with genuine investment needs
to produce something close to collective insanity.
Between 1844 and 1846, Parliament approved over 400 new railway projects.
Engineers, lawyers, and promoters collected fees
regardless of whether the lines were ever built.
Landowners extracted fortunes from right-of-way negotiations.
Ordinary investors poured their savings into railways that had no surveyed routes,
no locomotives,
and sometimes no identifiable board of directors.
When the bubble collapsed,
it wiped out a significant fraction of the British middle class,
destroyed several major banks,
and left behind a network of railways that,
once consolidated by the surviving companies,
actually worked.

That last part matters.
Bubbles are destructive for investors,
but sometimes productive for infrastructure.
The dot-com crash of 2000 that wiped out trillions of dollars in market value
left behind fiber-optic cable in the ground,
server farms,
and the engineering knowledge to run large-scale internet services cheaply.
Most of the companies that failed deserved to fail:
their business models assumed that selling pet food online at a loss,
while paying for national television advertising,
would somehow eventually produce a profit.
The crash was the market performing its nominal function of
reallocating capital away from bad ideas.
The problem was that the reallocation happened *after*
several hundred thousand people lost their jobs and several million lost their retirement savings.

The housing bubble that collapsed in 2008 followed a different structure
because it was built on debt rather than equity [%b Lewis2010 %].
Banks lent money to people who could not repay it,
packaged those loans into securities that were sold to pension funds and insurance companies,
bought insurance against those securities from companies that could not pay out,
and collected fees at every stage of the transaction.
The economists who designed the risk models assumed,
based on historical data,
that housing prices never declined nationally at the same time.
They were right until they were catastrophically wrong.

Crucially,
the losses did not fall on the banks that had made the bad loans—the US government covered those.
The losses fell on homeowners who lost their houses and
workers who lost their jobs when the broader economy contracted.
John Kenneth Galbraith noted in his history of the 1929 crash
that the capacity of human beings to ignore evidence
that contradicts a profitable belief is essentially unlimited [%b Galbraith1954 %].
The 2008 crisis added the observation that when enough money is at stake,
the strongest defenders of free markets suddenly become socialists in all but name.

Another feature of [%g speculative_bubble "speculative bubbles" %] is that
they tend to be ahistorical.
The dot-com bubble was the first internet bubble;
there were no previous internet bubbles to learn from.
The mortgage securities market of the 2000s was large enough
that its collapse was qualitatively different from anything that had happened before.
The phrase "this time it's different" has become shorthand
for the moment just before a collapse,
but it is genuinely true in a narrow sense:
the "why" of a particular collapse is usually novel enough that
people who want to believe can point to real differences from previous disasters [%b Kindleberger2005 %].

Which brings us to AI.
Large language models are genuinely impressive.
The companies building them have produced tools that fundamentally change how people write and program.
But the valuations of AI companies have,
since roughly 2023,
been running well ahead of their revenue,
their profit margins,
and any plausible estimate of the addressable market.
The story driving those valuations is that AI will soon be able to do everything,
which is a story that has been told before about nuclear power,
and about previous generations of expert systems and neural networks.

This doesn't mean that AI companies will collapse to nothing,
any more than railways did.
The real question is who is going capture the value
and who is going to absorb the cost
when reality catches up with the hype.
Historically, the engineers and founders who cashed out early do well.
The pension funds, retail investors, and laid-off workers who arrived later in the story do not,
while the people who collected fees at every stage of the transaction do best of all.
