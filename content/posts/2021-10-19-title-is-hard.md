---
title: "BlogPostExplainingNaming"
draft: true
---

![mandatory xckd](https://imgs.xkcd.com/comics/names.png)
<!-- more -->
Naming is hard because remembering names is hard.

By remembering names I mean:

- **recalling** the **form** of your *variable, function, functor* is hard.
- **explaining** the **function** for your *variable, function, functor* is hard.
- **encoding** the **context** of your *variable, function, functor* is hard.


So, I am going to use some beginners code to optimize for each of these problems and
then we'll have a look at a general approach through some real-world code.

```cpp
#include <iostream>

class Car {
  public:
    int speed(int maxSpeed);
};

int Car::speed(int maxSpeed) {
  return maxSpeed;
}

int main() {
  Car myObj;
  std::cout << myObj.speed(200);
  return 0;
}

```
</a>

## Optimizing for Form (ExplainingNaming)

This, of course, is the instinctive problem with naming.

> Form: **What** am I naming?

To think more clearly about this, let's see which kinds of forms are we talking about here?

Any entity you want to represent in a codebase (or in life) can be roughly divided into two categories:
- **Concrete entity**: it is bounded and is generally mutable. (e.g. USA, Ada Lovelace, Classes)
- **Abstract entity**: it is eternal and is generally immutable (e.g. Colours, Numbers, Physical matter)

BTW, I am basically stealing the above concept from the excellent [Elements of Programming](http://elementsofprogramming.com/) book (if you want to understand computer science from first principles using logic, run to this book!)

Armed with this knowledge, we can see that *Car* can be formed through two ways of looking:
### 1. *Car* as an abstract entity
Now, remember before we start talking about *Car* as a concrete entity, we need figure out the meta question:
> **What** is the **What** of the thing that I am naming?

Or put simply, what does this entity actually represent? What is the eternal concept that I am trying to put into this concrete entity?

Here, we need to look at codebases through a different prism.

What is the above program doing? It's encoding all these hand-wavy, abstract concepts of vehicles and speed into definite, concrete concepts of classes and methods.

Alright then, so if we optimize for form, in an abstract sense, how can we rewrite the following program?

We follow a really simple algorithm:
1. Replace all concrete names with the abstract entities they represent.
2. Done


```cpp
#include <iostream>

class Vehicle {
  public:
    int property(int value);
};

int Vehicle::property(int value) {
  return value;
}

int main() {
  Vehicle vehicle;
  std::cout << vehicle.property(200);
  return 0;
}

```

Now let's observe what this does to our interpretation of the program. Why the interpretation?
Because remember:
> All codebases are after all, text to be read by people

Looking at the changes, we can observe a few things:
1. Recalling the abstract ideas behind the program has become equivalent to reading it.
2. The specific concrete interpretation of the program has shifted from *printing the speed* to *printing the value of a property*.
3. However, the operation of the program has not changed at all. None of the methods work any differently. The methods will output the same result.

These observations seem trivial enough but there is more to think about!

Notice how this renaming has influenced the other two aspects of naming as well. (namely, pardon the pun, explaining the function and encoding the context)

We will talk about these relationships for each renaming procedures in a different blogpost.

### 2. *Car* as a concrete entity
In a concrete sense, the entity *Car* is a class bounded by it's contents.

The contents, basically has a speed method which returns the value of the speed property of this class.

So a more nuanced question, in this case, becomes:
> **What class** is this that I am naming?

The answer, of course in this particular example, becomes:
> This class is a class that 


## Optimizing for Function (Naming)

## Optimizing for Context (LetsThinkAboutNaming)
