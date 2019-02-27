---
title: The DS Papers(1) - How Special Relativity and Distributed Systems together,
  probably taught your messenger to manage your chats.
layout: post
sidebar_link: true
tags:
- Distributed Systems
- Peer to Peer
---

### Required Knowledge:

1. A sound idea of order theory and sets. ([Wikipedia page on Order Theory is quite good](https://en.wikipedia.org/wiki/Order_theory) )

2. Undergraduate understanding of Calculus. ( [Pretty good place to start is MIT's OpenCourseWare](https://ocw.mit.edu/courses/mathematics/18-01-single-variable-calculus-fall-2006/) )



This week we will look into one of the most seminal papers in Distributed Systems. 

As cleared by [The Theory of Special Relativity](https://en.wikipedia.org/wiki/Special_relativity), simply speaking, ordering of events in space-time is not absolute but is relative and consequently agreement on the ordering of events can become a problem when you have parts of a system distributed in space and time. So in 1978, a paper:

[Time, Clocks, and Ordering of Events in a Distributed System by Leslie Lamport](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/), sought to answer a seemingly simple yet surprisingly significant question:

> How can processes running on different machines with different ideas about time, coordinate events in an ordered manner without exclusive dependence on absolute concepts of time?

Or in the context of the millennium generation:

> How does your messenger keeps track of a chat with your friend?

## The Millennial problem statement

Okay I almost cheated. Well, we are not exactly talking about your average messenger but some peer-to-peer messenger that (I hope) some of you may have played with.

So how do these messengers with no central server arrange their chats in the correct order?
Let's try to find out the basic concept behind all the new, fancy implementations... 

## The real problem statement

The real motive of the paper was twofold:

* Firstly, what is meant by ordering of events in a system where you cannot depend on physically defined concepts of time, Let's take the millennial example:
	* Lets say Goo and Tar have the newest, coolest P2P Messenger called lire. Now Let's say 	Goo wants to chat with Tar. and here is, a proof of your privilege, a screenshot of their chat:![Chat that you can't see](/images/screenshot_chat.png  "Average chat")
	
		Now let's say that we know that Goo and Tar are both in different cities or in different continents. Now, what does the concept of time mean in this scenario, through which the messages(events) on their smartphones can be ordered correctly in the chats(systems)?
	

* Secondly, and perhaps most importantly, how do you design such a system where you can totally establish the order of the events occurring in its different parts without any means of a single source of absolute time.


To put in terms of set theory:

>This papers discusses the **partial ordering defined** by the "happened before" relation, and gives a **distributed algorithm** for extending it to a **consistent total ordering** of all the events.

## The real axioms

The first task in solving any problem logically involves picking up some axioms to recognize our options.

Here, Leslie's basic axiom consists of deriving a standard notation for the "happened before" relation between the events, *a* and *b*.

The first challenge that comes in defining such a relation is just simply saying:
> *a* happened **before** *b* simply means that *a* happened at an **earlier time** than *b*

which signals that for the above statement to hold any substance, we need to be able to strictly define the term *time*.

An initial solution could be bounding the term *time* to the notion of physical time. However, that soon creates a number of problems:

* As Leslie succinctly points out, if we mean to define a system accurately, the description or the specification of the system needs to be given in terms of events that are observable or measurable in the given system. 
 
Therefore, if the specification of the system is in terms of physical time, we need to include physical clocks in the system as well.  

* And if we use real physical clocks then it is clearly known that clocks do not keep accurate time, relatively speaking. 
 
Hence, a better solution would be to include a system where there is no dependency on any notion of physical time.

To create such a solution, Leslie came up with a simple relation called the "happened before" relation, denoted by "⟶".

The "happened before" relation is defined on the set of events of a system satisfying the folowing three conditions (The first two of which together,  is termed the **Clock Condition**):

**C1.** If *a* and *b*  are events in the same process, and *a* comes before *b*, then *a* ⟶ *b*.

**C2.** If *a* is the sending of a message by one process and *b* is the receipt of the same message by another process, then *a* ⟶ *b* .

**C3.**  If *a* ⟶ *b* and *b* ⟶ *c*, then *a* ⟶ *c*.

And naturally, we can further deduce that:

**Col1.** Two distinct events *a* and *b* are said to be concurrent if, *a* ⟶ *b* and *b* ⟶ *a*,

Let's give some millennial examples for each of the conditions and let's assume events are messages in the chat and processes are Goo and Tar.
1. if *msg1* and *msg2* are messsages from the same person, and *msg1* comes before *msg2*, then *msg1*  ⟶ *msg2*.
2. if *msg* is sent by Goo and *recpt* is recieved by Tar, then *msg*  ⟶ *recpt*.

Now that the conditions guiding the relation are clear, let's have a look at this interesting sentence in the paper:
> The " ⟶" relation implies an irreflexive, partial ordering on the set of all events in the system.

By the above sentence, Leslie meant that, the " ⟶" relation is a special type of partial ordering on the set where the property of reflexivity is not preserved but all other properties of a partially ordered set or *poset* are preserved.

The other two properties of a *poset* are:
1. Transitivity, which is preserved through **C3**.
2. Antisymmetry, which is preserved by our deduction **Col1**.


So, by defining such a relation we have completed the first part of our problem.


**SIDE NOTE**: 
* A common total order you're probably most familiar with is the 'less than' on the natural numbers: 1 is less than 2, which is less than 3, and so on. If we draw a total order, it looks just like a long line of objects (again, in the finite case at least). So the 'Less than' relation is total ordering. and 'Happend Before' needs to be turned into the 'Less than' somehow.