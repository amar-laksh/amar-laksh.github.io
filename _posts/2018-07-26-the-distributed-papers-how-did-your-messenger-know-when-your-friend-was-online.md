---
title: The DS Papers(1) - How Special Relativity and Distributed Systems together, probably taught your messenger to manage your chats.
layout: post
sidebar_link: true
tags:
- Distributed Systems
- Peer to Peer
---

This week we will look into one of the most seminal papers in Distributed Systems. 

As cleared by [The Theory of Special Relativity](https://en.wikipedia.org/wiki/Special_relativity), simply speaking, time is not absolute but is relative and ordering of events can become a problem when you have parts of a system distributed in space and time. So in 1978, a paper was published:

[Time, Clocks, and Ordering of Events in a Distributed System by Leslie Lamport](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/), sought to answer a seemingly simple yet surprisingly significant question:

> How can processes running on different machines with different ideas about time, coordinate events in an ordered manner without exclusive dependence on absolute and consistent concepts of time?

Or in the context of the millennium generation:

> How does your messenger keeps track of a chat with your friend?


## Required Knowledge:

* A sound idea of order theory and sets. ([Wikipedia page on Order Theory is quite good](https://en.wikipedia.org/wiki/Order_theory) )

* Undergraduate understanding of Calculus. ( [Pretty good place to start is MIT's OpenCourseWare](https://ocw.mit.edu/courses/mathematics/18-01-single-variable-calculus-fall-2006/) )

## The Millennium problem statement

Okay I almost cheated. Well, we are not exactly talking about your average messenger but some peer-to-peer messenger that (I hope) some of you may have played with.

So how do these messengers with no central server arrange their chats in the correct order?
Let's see... 

## The real problem statement

The real motive of the paper was twofold:

* Firstly, what is meant by ordering of events in a system where you cannot depend on physically defined concepts of time .e.g. - *a* **happens after** *b* but how do you define "happens after" when you don't have an absolute and consistent definition of time?

* Secondly, and perhaps most importantly, how do you design such a system where you can totally establish the order of the events occurring in its different parts without any means of a single source of absolute time.

## The real axioms

The first task in solving any problem by the scientific method involves holding up some axioms to recognize our options and approach.

Here, Leslie 



