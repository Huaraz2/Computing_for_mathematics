---
layout     : post
categories : handouts
title      : Handout 5 - Some revision and classes and methods
comments   : true
---

Lecturer: Vince Knight

Office: M1.30

email: knightva@cf.ac.uk

**Office hours: Thursday 1300-1500**

## What you have learnt this week:

- How to create a class and an instance of a class;
- How to give a class attributes;
- How to give a class methods;
- How to create new classes from old through inheritance.

## An example I went through with a student who came to see me:

{% highlight python %}
def vk(n):
    """
    A function that returns whether or not a number is divisible by 2,3 and 5.
    """
    return n % 2 == 0 and n % 3 == 0 and n % 5 == 0

##
# Getting the numbers less than 1000 that are 'vk' numbers


l = range(1000) # Creating list of first 1000 numbers (from 0 to 999)

#count = 0
emptylist = []  # Creating an empty basket that we're going to put our numbers in
for i in l:  # This loops over EXACTLY the things in l
    if vk(i) == True:  # Checking if the think (i) is one of the numbers we want
#        count += 1
        emptylist.append(i)  # Appends it to a list

#print count
print emptylist
print len(emptylist)

##
# Getting the first 1000 numbers that are 'vk' numbers

k = 0  # k is a number that will keep count of how many of the numbers we want we have
i = 0  # i is just going to be the numbers we will check
emptylist = []  # An empty basket to put stuff in
while k < 1000:  # This loops (forever) until the condition is not true
    if vk(i) == True:  # Checking if the thing (i) is one of the numbers we want
        k += 1  # Adds 1 to the count of good numbers
        emptylist.append(i)  # Append it to a list
    i += 1  # Keeps counting (no matter what i was)

print emptylist
print len(emptylist)
{% endhighlight %}

If we look at the output of the above we see that those numbers increase by 30 (which is the _lowest common multiple_ of 2, 3 and 5).
This is how some theorems are gotten to: some code to see something, recognising and investigating a pattern and proving a general result.

## Let's create a (very basic) 'beat em up' game

Let's create a general class for a _warrior_ in a game:

{% highlight python %}
class Warrior():
    """
    A class for a warrior.

    Attributes:
        - Name (a string)
        - Weapon (a string)
        - HP (hit points - a number)
        - AP (attack points - a number)

    Methods:
        - __init__
        - attack (a method that attacks another warrior)
        - defend (a method that defends against an attack)
    """
    def __init__(sef, name, weapon, AP):
        self.name = name
        self.weapon = weapon
        self.HP = 100
        self.AP = AP

    def attack(self, otherwarrior):
        otherwarrior.defend(self)

    def defend(self, otherwarrior):
        self.HP -= otherwarrior.AP
{% endhighlight %}

The above just gives us the framework to be able to create warriors that would fight each other.
Here is how we would actually get a fight:

{% highlight python %}
def whowins(warrior1, warrior2):
    """
    A function that gets two warriors to fight until one of their HP becomes negative

    Arguments:
        warrior1: an instance of the Warrior class
        warrior2: an instance of the Warrior class

    Output:
        The name of the winner
    """


    while warrior1.HP > 0 and warrior2.HP > 0:
        warrior1.attack(warrior2)
        warrior2.attack(warrior1)
    if warrior1.HP > 0:
        return warrior1.name
    if warrior2.HP > 0:
        return warrior2.name
    return 'Tie'
{% endhighlight %}

Now let's use that function to create a fight:

{% highlight python %}
sophitia = Warrior('Sophitia', 'Sword and Shield', 6)
siegfried = Warrior('Siegfried', 'BIG sword', 9)

print whowins(sophitia, siegfried)
{% endhighlight %}


## What you should do next:

- Start the next sheet: this is a short one and the aim is for you to be familiar with Sage.
- Continue to revise for the class test: work through all your lab sheets. If you can do exercises in the lab sheets (not just ‘understand them’ but actually ‘do them’) you will be fine.
- To make the best use of the lab sessions turn up having finished your sheets;
- If anything is still unclear please come and see me during office hours.
