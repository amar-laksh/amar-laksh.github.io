---
title: 'Your friendly neighbourhood util: factor'
draft: true
layout: post
sidebar_link: true
tags:
- coreutils
- factor
- maths
- linux
---

Welcome to a series where we learn about extremely useful and incredibly designed core utilities that exist on all Linux systems. (and some mac ones too!)

Our first stop is a small but impressive command line tool called factor. 
## Usage
```
factor [number to be factored]
```

```
$time factor 1232342819441289473259823473498421353435834573295241234325
1232342819441289473259823473498421353435834573295241234325: 3 3 5 5 179 191 79999 1283382111247 1307652744733469 1193245082041178989

real    0m7.161s
user    0m7.142s
sys     0m0.000s

$time factor 123234281944128947325982347349842135343583457329524123432
123234281944128947325982347349842135343583457329524123432: 2 2 2 36473 27959756010443 2623923161772596273 5756858765046553207

real    4m20.620s
user    4m19.385s
sys     0m0.438s
```
So  how does it factor the number *1232342819441289473259823473498421353435834573295241234325*  and how does this happen so fast?

Also, more interestingly why does the number *123234281944128947325982347349842135343583457329524123432* take so long to factor?

## Algorithm
If you look at the [Official Documentation](https://www.gnu.org/software/coreutils/manual/html_node/factor-invocation.html#factor-invocation) it tells you that  **factor** uses the [Pollard's rho algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm) to factor the numbers quickly. However, if you look into the [sourcecode](https://github.com/coreutils/coreutils/blob/master/src/factor.c) of *factor*, you will find a complex file that employes a variety of tricks to make the program as fast as it is now.

So let's go back to simpler times and look at the first time, the *Pollard-rho algorithm* was added to the code:

```
commit 00c6aacf318a6ef0db4895b08d572d924eab90d0
Author: James Youngman <jay@gnu.org>
Date:   Thu Jul 31 09:58:10 2008 +0200

    factor arbitrarily large numbers

    * m4/gmp.m4: New file; adds cu_GMP, which detects GNU MP.
    * configure.ac: Use cu_GMP.
    * src/Makefile.am: Link factor against libgmp if available.
    * src/factor.c: Use GNU MP if it is available.
    (emit_factor, emit_ul_factor, factor_using_division,
    factor_using_pollard_rho, extract_factors_multi,
    sort_and_print_factors, free_factors): new functions
    for the arbitrary-precision implementation, taken from an example
    in GNU MP.
    (factor_wheel): Renamed; was called factor.
    (print_factors_single): Renamed; was called print_factors.
    (print_factors): New function, chooses between the single- and
    arbitrary-precision algorithms according to availability of GNU MP
    and the length of the number to be factored.
    (usage, main): New options --bignum and --no-bignum.
    * coreutils.texi (factor invocation): Document new command-line
    options for the MP implementation and update the performance
    numbers to take into account the asymptotically faster algorithm.
    * TODO: Remove item about factoring large primes (it's done).
    * m4/gmp.m4: Add support for --without-gmp.
    * NEWS: Mention the new feature.
```
