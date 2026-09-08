# How Organizations Mirror Their Structures

[%g conways_law "Conway's Law" %] states that organizations produce systems that mirror
their communication structures. It is well known in software
engineering but its implications are not fully absorbed. The same
principle operates in hospitals, government agencies, and armies: the
architecture of the product reflects the architecture of the
organization that built it.  This means you cannot change the product
without changing the organization, and you cannot change the
organization without understanding what interests the current
structure serves. [%g institutional_knowledge "Institutional knowledge" %] is the tacit, distributed
understanding of why things work the way they do.  It is a form of
capital that is easy to destroy and hard to reconstruct.

Melvin Conway published his observation in 1968, having watched it appear repeatedly in his own work: the structure of a communication system will resemble the communication structure of the organization that produced it. Fred Brooks gave it wider circulation in *The Mythical Man-Month*, and it has since become a piece of conventional wisdom in software engineering. What is less often discussed is the directionality of the claim. It is not merely that structure influences output. It is that organizational structure is difficult to change, that it tends to be stable even when the explicit goals of the organization change, and that systems inherit this stability whether or not it is wanted.

The pattern appears in domains that have nothing to do with software. Hospital information systems are notoriously fragmented along departmental lines, not because fragmentation is technically necessary, but because hospitals are organized by departments with distinct professional cultures, billing codes, and lines of authority that resist integration. Military logistics systems reflect the organizational seams between services, branches, and commands. Public transit infrastructure in most American cities reflects the political geography of jurisdictions that were drawn before the systems were built, which is why a bus network often stops at a county line that a commuter crosses daily. The system is a map of the organization, and the organization is a map of its political history.

[%g sociotechnical "Sociotechnical congruence" %] is the formal version of this observation: that technical systems and social structures co-evolve over time, and that each comes to sustain the other. A codebase develops conventions that reflect the team that built it. New team members learn those conventions. The team's communication patterns solidify around the architecture. Changing one requires changing the other, which requires coordinating across both dimensions simultaneously. This is why reorganizations that look simple on an org chart often produce unexpected technical debt: the new structure does not align with the existing code, and the friction is invisible to anyone who does not understand both.

Rewrite projects fail so often for exactly this reason. The old system, however poorly documented and internally inconsistent, encodes institutional knowledge about the problem domain: edge cases that were discovered over years of operation, implicit contracts with upstream and downstream systems, decisions that look arbitrary but reflect constraints that no longer exist in any written form. The team doing the rewrite typically knows the parts that are explicitly documented and none of the rest. They rebuild the easy parts correctly and rediscover the hard parts the way the original team discovered them, by encountering problems in production. The new system is often less capable than the old one for years after launch.

When an organization is reorganized or downsized rapidly, the knowledge that is lost is not primarily what is in the documentation. It is the knowledge of which documentation is wrong, who to call when the monitoring is lying, what the system does in failure modes that have not been seen in years, and how to read the historical record to understand whether a new anomaly is genuinely new. This knowledge is distributed across the heads of people who have worked together long enough to develop shared context. It cannot be transferred in exit interviews or captured in wikis. It evaporates when the people leave, and it leaves a system that looks the same from the outside but is now being operated by people who do not know what they do not know.

A useful diagnostic for organizational health follows directly from this: pay attention to what a team is having meetings about. Meetings accumulate around coordination failures. When two teams cannot resolve something at the working level, it escalates. When a process is broken, people meet to manage the breakage. When a system's behavior is not understood, people meet to compare theories. The meeting schedule is a heat map of where the organization's structure is misaligned with its actual work.

[%b Brooks1975 Bellotti2021 Vaughan1996 %]
