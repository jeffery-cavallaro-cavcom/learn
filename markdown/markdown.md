# Markdown Cheat Sheet

## Paragraphs and Line Breaks

### Wordwrapping

Consecutive lines are word-wrapped
into the
same paragraph.

### Line Breaks

Lines ending in two  
or more spaces result  
in line breaks.

### Paragraphs

Paragraphs are separated by
one or more blank lines.

This is a new paragraph.

## Headers

### SetExt Style

Level One Header  
\=

Level Two Header  
\-

### ATX Style

\# Level One Header  
\## Level Two Header  
\### Level Three Header  
\#### Level Four Header  
\##### Level Five Header  
\###### Level Six Header

## Emphasis

Use a single *asterisk* or _underscore_ for italics (emphasis).

Use double **asterisks** or __underscores__ for bold.

## Lists

### Ordered Lists

1. Item one.
1. Item two.
1. Item three.

Alphabetic and nested ordered lists are not supported.

### Unordered Lists

* Level one item one.
  + Level two item one.
    - Level three item one.
    - Level three item one.
  + Level two item two.
* Level one item two.
* Level one item three.

The markers (\*, \+, \-) are interchangeable; only indent matter.

## Links

This is an [inline](http://www.google.com) link to google.

This is a [reference][ref] link to google using an ID.

This is a [reference] link to google using the link text.

[ref]: http://www.google.com "Google"
[reference]: http://www.google.com "Google"

The optional title attribute in the link definition can enclosed in single
quotes, double quotes, or parentheses.

This is an automatic link to <http://www.google.com>.

This is an automatic email link to <jeffery@cavcom.com>.

## Block Quotes

Block quotes are indicated by one or more right angle brackets.
> Here is the first level
> of the block quote.  Each continuation line
> can optionally begin with another
> right angle bracket.
>> This is a second level block quote.
>> The number of right-angle brackets determines the level.
>>> One more level for demonstration purposes.

That is the end of the blockquotes.

## Code Blocks

### Standard

Code blocks are indented:

    # apt-get update
    # apt-get install emacs

Or can be inline: `echo 'Hello, World!!!'` like this.

### GFM

Use triple back ticks with an optional language specifier:

``` java
public static void main(String [] args) {
    System.out.println("Hello, World!!!");
}
```

## Images

This is an inline image of a man
![a man](https://static.thenounproject.com/png/63361-200.png "Man")
of a ghost.

This is an image of ![a man][man] by image ID.

[man]: https://static.thenounproject.com/png/63361-200.png "Man"

## Horizontal rules

Three or more hyphens, asterisks, or underscores:

---

***

___

## Special Characters

sequence | character
--- | ---
\\ | backslash
\` | backtick
\* | asterisk
\_ | underscore
\{ | left curly brace
\} | right curly brace
\[ | left square bracket
\] | right square bracket
\( | left parenthesis
\) | right parenthesis
\# | hash mark
\+ | plus sign
\- | minus sign
\. | dot
\! | exclamation mark
\| | vertical bar
