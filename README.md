# Ar Hap

## What Is It?

A set of common higher level randomness functions using a cryptographically suitable randomness 
generator, [os.urandom](https://docs.python.org/3/library/os.html#os.urandom).

## How Do I Use It?

Return a string of length _length_ of random characters
~~~
arhap.random_string(length=64, characters=a-zA-Z0-9)
~~~

Return a random 64bit integer
~~~
arhap.random_int()
~~~

Return a random number within a given range (inclusive)
~~~
arhap.random_range(min, max)
~~~

Randomly select a value from a list
~~~
arhap.random_choice(list)
~~~

## How Do I Get It?
~~~
pip install --upgrade git+https://github.com/joocer/arhap
~~~
or in your requirements.txt
~~~
git+https://github.com/joocer/arhap
~~~
