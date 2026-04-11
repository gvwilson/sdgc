# Alternatives and Dead Weight


## There's More Than One Way to Do It

When you start a company in Canada,
one of your first decisions is whether to incorporate federally or provincially.
Most first-time founders treat this as a paperwork question,
but it is not.
The legal structure you choose encodes assumptions about who controls the company,
who benefits when it succeeds,
and who bears the cost when it fails.
Those assumptions vary enormously across history and across cultures,
and the fact that most tech companies make the same choice
tells you something about whose interests the dominant model serves.

## The Usual Suspects

A [%g sole_proprietorship "sole proprietorship" %] is the simplest possible firm:
one person owns it, operates it, and is personally liable for everything it does.
If the business gets sued and loses,
the owner's house, car, and savings are all at risk.
Most small businesses start this way because there is no registration required—
you are in business the moment you start selling something,
though you must register your business name in most provinces
if you are trading under a name other than your own.

A [%g partnership "partnership" %] divides ownership between two or more people.
In a [%g general_partnership "general partnership" %], all partners share liability;
in a [%g limited_partnership "limited partnership" %],
the limited partners risk only what they invested,
while the general partner remains fully exposed.
Law firms, accounting firms, and investment funds have historically used partnership structures,
partly because unlimited personal liability concentrates the minds of the partners wonderfully.

The [%g limited_liability_corporation "limited liability corporation" %] is the dominant modern form,
and its history is stranger than most people realize.
[%g joint_stock_company "Joint-stock companies" %] with limited liability
appeared in England and the Netherlands in the early 1600s.
The Dutch East India Company, founded in 1602,
is often called the world's first publicly traded corporation:
it issued shares to outside investors,
its shareholders could not lose more than they invested,
and those shares were traded on what became the Amsterdam Stock Exchange.
The whole structure was designed to let wealthy merchants finance long and risky trading voyages
without betting their entire fortunes on any single ship.
Limited liability is a legal invention,
created by governments to encourage private investment
in ventures too expensive for any one person to fund alone.

A [%g public_benefit_corporation "public benefit corporation" %] (PBC) is a newer form,
legally requiring the company to consider the interests of employees,
communities,
and the environment,
not just shareholders.
The practical difference from a regular corporation is small in good times
but matters when a company faces acquisition pressure or demands for short-term earnings.

## The Cooperative Tradition

A [%g cooperative "cooperative" %] is a firm owned and governed by its members,
whether those members are workers, customers, or both.
Profits are distributed as dividends proportional to participation
rather than to capital invested.
This fundamentally changes the incentive structure:
a worker-owned cooperative has no absentee shareholders extracting returns,
and no structural pressure to cut wages in order to improve margins.

The most ambitious experiment in worker ownership at scale is the Mondragón network,
described in detail in [Alternatives That Scaled](@/cooperatives/).
Its founding in the Basque region in 1956 and the flexibility it demonstrated during the 2008 crisis
illustrate what the cooperative structure makes possible.

[%g consumer_cooperative "Consumer cooperatives" %] own the firm on behalf of their customers.
In Switzerland,
Migros and Coop together hold a majority of the grocery market,
both as consumer cooperatives.
[%g credit_union "Credit unions" %]—the most common form of cooperative in Canada—are
owned by their depositors
and return surplus to members rather than to outside shareholders.
Cooperatives can face difficulties raising capital
can develop their own forms of bureaucratic inertia,
but they show that the investor-owned model is not the only way to organize a business
[%b Ostrom2015 %].

<div class="callout" markdown="1">

Why can't cooperatives simply sell equity to outside investors?
Because they have nothing to sell.
In a conventional corporation,
an investor buys shares that give a proportional claim on future profits and, usually, a proportional vote.
That claim grows if the company grows, which is why investors want it.
In a cooperative, profits are distributed based on participation,
not on capital contributed.
An outside investor who puts in money
gets no proportional share of future surplus and no proportional governance voice.

A second problem is that worker-members have short time horizons:
a member's stake ends when they leave or retire,
which creates rational incentives to distribute surplus now
rather than reinvest it in long-term capital projects the member may not live to benefit from.
Economists call this the [%g horizon_problem "horizon problem" %].
The main escape valve is debt,
but debt has fixed repayment obligations regardless of conditions.
Mondragón has partially solved this with indivisible reserves,
which are a pool of retained earnings belonging to the cooperative collectively
that no individual member can withdraw.
It works,
but it requires members to permanently give up a claim on capital they contributed,
which can be difficult.

</div>

## Beyond the Anglo-American Tradition

Germany's large manufacturing firms operate under Mitbestimmung,
the codetermination system described in [Labor and Passion](@/labor/),
in which workers hold legally mandated seats on corporate supervisory boards.
The [%g mittelstand "Mittelstand" %]
(Germany's medium-sized family-owned manufacturers)
often combine this formal worker representation with multi-generational ownership
that is structurally indifferent to quarterly earnings reports.

Japan's [%g keiretsu "keiretsu" %] are networks of interlocked companies
that hold shares in one another,
maintain long-term trading relationships,
and are often anchored around a major bank.
Toyota sits at the center of one of the largest,
with dozens of suppliers holding Toyota shares and Toyota holding shares in them.
This mutual cross-shareholding insulates management from hostile takeovers
and creates strong incentives for long-term investment in shared production quality,
but it also insulates management from accountability when things go badly wrong,
as Japan's long economic stagnation after 1990 demonstrated
[%b Thelen1992 %].

The Islamic [%g waqf "waqf" %] is a form of charitable endowment
with no direct equivalent in Western legal systems.
Property dedicated as a waqf cannot be sold or inherited;
instead,
its income must be applied to specified charitable purposes in perpetuity.
Universities, hospitals, mosques, and public fountains across the Middle East and Central Asia
were historically funded through waqf endowments.
At their peak in the Ottoman Empire of the eighteenth century,
estimates suggest that as much as a third of agricultural land was held as waqf.
European colonialism systematically dismantled waqf structures across North Africa, the Levant, and South Asia,
converting endowed property to state ownership or private title—a transfer of wealth
whose scale is rarely recognized.

In India, the Hindu Undivided Family (HUF) has been a recognized legal entity
for tax and property purposes
since British colonial administration codified it in the nineteenth century.
An HUF is not a firm in the Western sense but a patrilineal kinship group
that can own property, run a business, and have its own tax identity.
Tata, Birla, and other major Indian conglomerates grew from family-business structures
in which the boundary between the family and the enterprise was deliberately blurred.

## Why Canadian Tech Companies End Up in Delaware

Despite the availability of federal and provincial incorporation,
a significant number of Canadian tech startups that raise venture capital
end up reincorporating as Delaware C-corporations.
The reason is not that Delaware law is superior.
It is that American venture capital funds,
the dominant source of growth-stage capital,
require Delaware C-corps because their legal documents were drafted for that structure,
their lawyers know it,
and their limited partners expect it.
A Canadian founder who takes US venture money
often has to execute what is called a "[%g delaware_flip "Delaware flip" %]":
creating a new Delaware holding company above the existing Canadian entity,
transferring the intellectual property,
and essentially making the company American on paper.
This is an expensive process that produces no operational benefit for the company;
it is pure path dependency imposed by the capital markets.

What tech companies on both sides of the border have innovated on
is not the basic corporate form
but the voting structure within it.
[%g dual_class_shares "Dual-class share structures" %],
in which founders hold shares with ten or more votes each
while public investors hold shares with one vote,
have become standard in major tech IPOs.
When Google went public in 2004,
Larry Page and Sergey Brin wrote a letter to shareholders explicitly explaining
that they intended to run the company unconventionally
and that investors who disagreed should not buy the stock.
Shopify, Canada's largest tech company, used a similar structure:
Tobi Lütke holds Class B shares with ten votes each
while public shareholders hold Class A shares with one vote.
The practical effect is that founders retain effective control regardless of how many shares they have sold:
the company is publicly traded but not publicly governed,
which is exactly what most founders want.

The usual excuse for why tech companies aren't worker cooperatives or other equitable structures
is that cooperative governance is too slow and cooperative financing too limited.
This explanation is conveniently incomplete.
It omits the fact that the founders, lawyers, and venture capitalists making the choice
benefit most from the conventional structure.
A Delaware C-corp with dual-class shares concentrates decision-making authority and financial upside
in the hands of a small number of people at the top.
Describing this as a neutral response to market conditions,
rather than as a choice made by self-interested parties who control the available alternatives,
takes a certain kind of nerve.

Silicon Valley has developed an elaborate ideology to justify the arrangement.
The founding team are visionaries whose judgment must be protected from short-term market pressure;
the employees are passionate craftspeople who are compensated with equity
so that their interests are aligned with the company's success.
In practice,
the equity granted to employees is typically worth a fraction of what founders and early investors receive,
and vests on a schedule designed to retain rather than reward.
Worker cooperatives,
codetermination boards,
and profit-sharing arrangements work—Mondragón has been running for nearly seventy years—but
they distribute power rather than concentrating it,
which is precisely why you will not find them recommended at Y Combinator
[%b Whyte1991 Kelly2012 Gordon2001 Linklater2015 Bakan2005 Cassidy2025 %].

## Alternatives That Scaled

In 1956, a Catholic priest named José María Arizmendiarrieta
gathered five workers in a converted school in Mondragón,
a small town in the Basque region of Spain,
and started making paraffin heaters.
The school had been set up to train young workers
who had no other way into higher education after the devastation of the Spanish Civil War.
The stove factory was meant to give those workers somewhere to apply what they had learned;
what Arizmendiarrieta wound up building instead
was one of the most durable experiments in worker ownership the twentieth century produced.

By 2024,
the Mondragón Corporation employed roughly 80,000 people
across manufacturing, retail, financial services, and education.
Its retail chain, Eroski, operates hundreds of supermarkets across Spain.
Its finance arm, Laboral Kutxa,
is one of the larger banks in the Basque Country,
and its manufacturing division makes everything from machine tools to household appliances.
None of this is run for the benefit of outside shareholders,
because there *are* no outside shareholders.
The workers own the enterprise.
They elect the management,
they negotiate pay scales internally,
and when Spain's economy collapsed after 2008—collapsing hard enough
that national unemployment hit 27 percent—Mondragón
moved workers between cooperatives rather than letting them go
[%b Morrison1991 %].

Mondragón is the most-cited example of worker ownership at scale,
but it is not the oldest.
In the 1860s,
Friedrich Raiffeisen was running a rural municipality in what is now Germany
and watching small farmers get crushed by moneylenders.
Commercial banks weren't interested in lending to peasants—the collateral was uncertain
and the administrative costs ate into profit margins—So
Raiffeisen organized the farmers to lend to each other.
Members pooled deposits,
the cooperative extended credit to members at rates commercial lenders couldn't match,
and the surplus stayed within the cooperative rather than flowing to outside investors.

The model spread across rural Germany to Austria and Switzerland
and then to the rest of the world.
Today the Raiffeisen network is one of Europe's largest banking groups,
with operations in over a dozen countries and hundreds of billions of euros in assets.
The World Council of Credit Unions estimates
that roughly a billion people worldwide are members of credit cooperatives of one kind or another.
That means a substantial fraction of the adult population of the planet
choose to do their banking outside the shareholder model,
but you wouldn't know that listening to conversations in Silicon Valley
[%b Whyte1991 %].

Vienna in the 1920s faced a housing crisis
that would look familiar to anyone paying rent in a large city today.
The city had grown rapidly during the late nineteenth century,
housing conditions for working-class residents were appalling,
and private landlords had neither the incentive nor the capital to fix things.

The Social Democratic city government,
elected in 1919 and governing what became known as Red Vienna,
decided to treat housing as a public utility rather than a market good.
Between 1923 and 1934,
the city built roughly 60,000 apartments in large municipal complexes called the Gemeindebau.
These were not the grim concrete towers that social housing became associated with in many countries.
They were substantial brick buildings with courtyards,
laundries, libraries, kindergartens, and clinics built in.
The Karl-Marx-Hof,
completed in 1930 and still standing today,
is over a kilometer long and houses several thousand people.
The whole program was funded by a progressive tax on luxury goods:
people buying fur coats and racehorses paid for workers to have decent apartments.

The program did not stop in 1934.
The city of Vienna still owns about 220,000 apartments directly
and subsidizes roughly another 200,000 through a nonprofit cooperative housing sector.
About 60 percent of Vienna's residents live in subsidized housing of one kind or another;
rents are set by law rather than by the market.
Vienna consistently ranks among the most livable cities in the world,
and the housing policy is a big part of that ranking.

Amul is an Indian dairy cooperative founded in 1946 in Gujarat
after farmers organized to break the monopoly of a single private contractor
who controlled their access to the Bombay milk market.
Today Amul is the world's largest dairy cooperative by volume,
collecting milk from roughly 3.6 million farmer-members across India
and distributing it through a network that reaches every major Indian city.
Amul did not stay small and artisanal: it scaled.

Canada's credit union sector,
which is one of the largest in the world per capita,
also proves that cooperatives can scale.
Desjardins, based in Quebec,
was founded in 1900 by a journalist named Alphonse Desjardins,
who had noticed that working-class Canadians were being charged usurious rates by commercial moneylenders.
Desjardins is now one of the largest financial institutions in Canada,
with roughly eight million members and assets over 400 billion Canadian dollars.
Members own it,
members elect the board,
and surplus is returned to members rather than to shareholders.
It survived the 2008 financial crisis in considerably better shape
than many of the shareholder-owned banks
that had been busy congratulating themselves on their sophistication.

Mondragón, Raiffeisen, the Viennese Gemeindebau, Amul, and Desjardins are not arguments in a seminar:
they are institutions that issue annual reports.
The claim that these structures cannot work at scale is simply false.
The more interesting question is why the claim persists
when the counterexamples are so large and so obvious.
Part of the answer is that the people
who benefit most from shareholder-owned structures
are the same people
who write most of the business press.
They cannot easily see alternatives
in the same way that a landlord genuinely cannot understand
why anyone would object to market-rate rent.

The shareholder firm captures value for shareholders,
transfers risk to workers and communities,
and concentrates decisions in a board
appointed to serve shareholder interests.
The worker cooperative captures value for workers,
distributes risk across the membership,
and makes decisions through governance structures
the members design and can change.
Neither of these is natural or inevitable.
They are all choices,
and the choice that has dominated tech for the past forty years
is not the only choice available
[%b Blasi2013 Yunus2007 %].

## The Eight-Hour Day

On April 21, 1856,
the stonemasons working on the construction of the University of Melbourne
stopped work at midday,
marched through the center of the city,
and held a celebration at the Criterion Hotel.
They had just won a reduction in their working day from ten hours to eight
by walking off the job during a construction boom,
when building contractors could not afford to wait them out.
It was the first time anywhere in the world
that workers had achieved the eight-hour day;
they did it not through moral persuasion
but by applying collective leverage at a moment of their opponents' weakness.

The demand itself was older.
Robert Owen,
the Welsh manufacturer and social reformer,
had called for "eight hours labour, eight hours recreation, eight hours rest" as far back as 1817.
The slogan was catchy,
but Owen could not make it happen through goodwill and argument.
It took workers
who understood that goodwill was irrelevant
and that argument only mattered when backed by the capacity to impose costs.
The Melbourne stonemasons made exactly that calculation.
They are mostly forgotten now,
which is itself informative about whose history gets told
[%b Thompson1963 Roediger1989 %].

What the Melbourne stonemasons demonstrated locally,
labor movements across the world began demanding internationally.
In May 1886,
a general strike for the eight-hour day shut down factories across the United States.
On May 4,
a bomb exploded in Haymarket Square during a protest meeting in Chicago,
killing both police officers and civilians.
The bomb-thrower was never identified,
but eight anarchists were tried anyway,
and four were hanged.
The Haymarket affair became a rallying point for the international labor movement;
May Day was adopted as a workers' holiday across most of the world
(with the notable exception of the United States and Canada,
which moved their Labor Day to September specifically to avoid the association).

In 1889,
the newly formed Second International—a
loose federation of socialist and labor parties—declared May 1
an international day of solidarity for the eight-hour day.
The Second International's campaign,
and the May Day commemorations that followed,
spread the eight-hour demand across Europe,
Latin America,
and Asia.
But spreading a demand and achieving it are different things.
In most countries,
forty years passed between the first serious campaigns for the eight-hour day
and its legal establishment.

What actually closed the gap was not sympathy,
but the end of the First World War,
a political crisis of such severity
that governments in Europe and North America
feared a revolution like one that threw Russia into chaos in 1917.
Germany had a workers' council movement in 1918
that briefly looked like it might go the same way,
Hungary had a Soviet republic in 1919,
and strikes were spreading in Britain, France, and the United States.
Employers and governments that had resisted the eight-hour day for decades
suddenly discovered they could live with it.

France legislated the eight-hour day in April 1919.
Britain passed the Hours of Work Convention that same year.
The first convention adopted by the newly created International Labour Organization in 1919
was an eight-hour day and forty-eight hour week for industrial workers.
Then and now,
labor gains were not won because employers and governments became convinced
that workers deserved better.
They were won because the cost of continued resistance
exceeded the cost of concession.

On March 25, 1911,
a fire broke out at the Triangle Shirtwaist Factory on the eighth floor of a building
in Greenwich Village, New York.
The managers had locked the stairwell doors
to prevent workers from taking unauthorized breaks
and to stop theft of fabric.
146 workers died,
most of them young immigrant women,
many of them Jewish and Italian.
Some jumped from the windows.
The owners were acquitted of manslaughter charges and collected the insurance.

The conditions the first exposed—locked exits, no sprinklers, overcrowding,
and abusive supervisors—were standard practice at the time.
What wasn't standard was the combination of a catastrophic death toll
and the organizational capacity that existed to exploit the political opening.
The Women's Trade Union League,
the International Ladies' Garment Workers' Union,
and the socialist press had spent years building exactly that capacity.
Within days of the fire,
Rose Schneiderman gave a speech at the Metropolitan Opera House
that reframed the debate.
This was not a tragedy but a crime,
and the perpetrators were not the invisible people who set fires
but the visible people who locked the doors and blocked regulation.

The result was a legislative investigation that produced fifty-six pieces of legislation over three years
covering fire safety, working hours, factory inspection, and child labor.
The fire itself didn't produce the laws;
it was the fire plus organized political capacity.
Without the unions and the reform organizations that could turn grief into legislative pressure,
the Triangle fire would have been grieved and forgotten like the hundreds of industrial disasters
that preceded and followed it
[%b Orleck1995 %].

<div class="callout" markdown="1">

New Zealand arrived at labor protections through a different route
that is worth knowing about because it is so rarely mentioned.
The Industrial Conciliation and Arbitration Act of 1894
established a system of compulsory arbitration
that gave workers formal legal recourse
without requiring them to build the confrontational union structures
that dominated British and American labor history.
Workers could take disputes to an arbitration court rather than striking.
New Zealand also introduced the eight-hour day for most workers in
1891—earlier than most of Europe or North America—and
had established old-age pensions by 1898,
thirty-seven years before the United States got around to Social Security.
The Liberal government of the time pushed this through
because the working-class vote was key to staying in power.

</div>

It would be convenient if the story ended with legislative victory,
but it doesn't work that way.
Laws passed under political pressure are enforced under political pressure.
When pressure falls,
enforcement falls with it.
The International Labour Organization's Convention No. 1 was adopted in 1919;
a century later,
most of the world's workers are not covered by it in practice,
and enforcement is fragmentary or absent in many countries that have ratified it.

In the garment industry—the industry where the Triangle fire happened—workers
are still dying in predictable, preventable ways.
The Rana Plaza building in Dhaka collapsed on April 24, 2013,
killing 1,134 workers,
most of whom were making clothes for Western brands.
The building had visible cracks that workers reported the day before;
managers ordered them back to work anyway.

After Rana Plaza,
the Accord on Fire and Building Safety in Bangladesh—a
legally binding agreement between brands and global unions—was signed within weeks.
It covered over 1600 factories.
This was a real gain,
but it was also partial, contested, and reversible:
the Accord expired,
was replaced by a weaker voluntary mechanism,
and was eventually renegotiated into a successor agreement after sustained campaigning.
That was not a failure:
two steps forward and one step back is still one step forward.

Tech workers currently occupy the same position as skilled craftworkers in the mid-nineteenth century.
They are well-paid relative to most workers,
which makes collective action feel unnecessary.
They work under employment contracts
that make collective action legally complicated.
And they identify with their employers,
which makes collective action feel like a betrayal,
right up to the moment of a layoff.

Today,
as their jobs are threatened by AI,
tech workers are starting to care more about labor rights and organizing.
What the history tells us is that in order for this to translate into effective action,
what matters is organizational capacity,
a moment of political opening,
and the willingness to impose costs.
The opening comes eventually,
usually from a crisis or a shock.
The organizational capacity takes years to build.
The lesson from the eight-hour day is not that patience pays off.
It is that you need to be organized before the opening arrives
[%b Beckerman2022 Harvey1998 %].

## Bullshit Jobs and Parkinson's Law

In 1930,
as the Great Depression settled in to stay,
John Maynard Keynes wrote an essay called "Economic Possibilities for Our Grandchildren".
He predicted that by 2030
the technical problems of production would be solved,
and that the standard of living in wealthy countries would have risen so dramatically
that people would work no more than fifteen hours per week.
Humanity's ancient struggle with scarcity would be essentially over;
the challenge would be figuring out what to do with all the leisure.

Keynes' reasoning was straightforward.
Productive capacity had been growing for 150 years,
and if it continued growing at a similar rate,
there would soon be more than enough to go around with minimal effort.
He turned out to be right about production and wrong about work:
we produce vastly more per person than in 1930,
but work roughly as many hours.
The question is, "Why?"
[%b Keynes1930 %]

The answer is that productivity gains were not distributed as leisure;
they were captured as profit.
The share of national income going to wages in most affluent countries has fallen since the 1970s,
while the share going to profits, dividends, and capital gains has risen.
When a factory installs machines that allow one worker to produce what three produced before,
the two workers who are no longer needed aren't given paid time off—they are fired
(or "let go", if you prefer the euphemism).
The worker who remains works the same hours as before,
for roughly the same wage;
the gains all accrue to the factory owner.

The second answer involves "conspicuous busyness",
a counterpart to Veblen's conspicuous consumption.
Human beings are primarily motivated by relative position, not absolute wealth.
If everyone gets more leisure,
no one's status improves compared to anyone else's.
But if you work longer hours than your colleagues,
you signal commitment, importance, and indispensability.
In many professional environments,
especially in the United States and East Asia,
extreme hours have become a status marker
[%b Veblen1899 %].

The third answer was given a name in 1955 by C. Northcote Parkinson,
a British historian writing satirically about how
the Royal Navy's administrative overheads had expanded
as its fighting fleet shrunk.
[%g parkinsons_law "Parkinson's Law" %] states that
work expands to fill the time available for its completion.
Organizations don't need actual work to justify hiring more administrators;
the administrators find or generate the work.
Parkinson was being funny,
but he was also describing a real phenomenon
that has been documented in organizations from colonial government ministries
to modern corporate compliance departments.

The anthropologist David Graeber spent years collecting accounts from people
who described their own jobs as largely or entirely pointless.
His 2018 book *Bullshit Jobs* offered both a taxonomy and an explanation.
Graeber's taxonomy identifies five types:

-   Flunkies,
    who exist to make their superiors feel important
    (e.g., the receptionist whose main function is to signal that the executive is important enough
    to have a receptionist);
-   Goons,
    who exist to defend their organization against the equivalent goons of competing organizations
    (including lobbyists, corporate lawyers, much of the advertising industry);
-   Duct tapers,
    who fix problems that could be solved permanently but aren't,
    because fixing them would eliminate someone's job or require an organizational change
    no one is willing to make;
-   Box tickers,
    who perform or administer paperwork that allows an organization to claim it is doing something
    it is not actually doing; and
-   Taskmasters,
    who assign and manage work that does not need to be assigned or managed.

These people aren't lazy—most of the ones Graeber interviewed worked hard
and were genuinely distressed about the pointlessness of their work.
His point is that the growth of these roles has been driven by
our social need to keep white-collar workers busy,
in "respectable" white-collar jobs.

The tech industry has been doing a speed-run through this.
Agile coaches,
scrum masters,
developer advocates,
and platform engineers whose platforms help other engineers manage their platforms
have proliferated faster than the number of people writing code.
Engineers who *do* write code frequently report that a significant fraction of their time
is consumed by meetings, status updates, documentation for internal audiences,
and other activities that Graeber's taxonomy would classify as box-ticking
[%b Graeber2018 %].

ON the other hand,
framing it this way is yet another example of engineers centering themselves
and dismissing everyone else's work as secondary.
In 2009,
Google ran an internal study called Project Oxygen
to settle the question of whether managers actually mattered.
The engineers running the study expected to confirm that management was overhead
and that flat teams of smart people would outperform hierarchically organized ones.
Instead they found the opposite:
the teams with the best managers performed significantly better.
When Google experimented with removing management layers,
engineers asked for their managers back:
not because they wanted to be supervised,
but because they needed someone to run interference with other teams,
to help them think through career decisions,
and to give them feedback that a technical peer couldn't
[%b Garvin2013 Sandel2020 %].
