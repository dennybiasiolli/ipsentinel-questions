# ip-sentinel questions

## project initialization

- create a virtualenv using Python 3.8+

    `python3 -m venv venv`

- activate the virtualenv

    `source venv/bin/activate`

- install requirements

    - `pip install -r requirements.txt` for production usage

    - `pip install -r requirements_dev.txt` for development

- follow instructions below for each question


## Question 1 (20 mins)

Execute with `python src/q1.py`

Write a script to implement the game "Fizz Buzz".
Counting from 1 to 100, print each number in turn, on a new line.
BUT...
 * If the number is divisible by 3, or contains a digit 3, print "Fizz" instead of the number.
 * Similarly, for 5s, print "Buzz".
 * If both the "3" and "5" conditions, "Fizz Buzz".

## Question 2 (30 mins)

Execute with `python src/q2.py`

Entries from an LDAP user database are represented in Python as a
dictionary of key-value pairs, where each key is a case-insensitive
string object and each value is a list of bytes objects. For example:

~~~~
ldapdict = {
    'objectclass': [b'inetOrgPerson', b'person'],
    'cn': [b'George Orwell'],
    'givenName': [b'George'],
    'sn': [b'Orwell'],
    'uidNumber': [b'1984'],
    'gidNumber': [b'1984'],
    'mail': [
        b'george.orwell@example.com',
        b'big.brother@example.com',
    ],
}
~~~~

Create an LdapEntry class with attributes for each of the keys listed
above that can be used as follows:
~~~~
e = LdapEntry(ldapdict)
assert(e.cn == 'George Orwell')
assert(e.uidNumber == 1984)
assert('big.brother@example.com' in e.mail)
assert(len(e.mail) == 2)
~~~~

## Question 3 (40 mins)

Use django rest framework to create a single endpoint *songs/* that returns a list of songs:
~~~~
[
    {
        "title": "Yesterday",
        "artist": "John Lennon"
    },
    {
        "title": "Wonderwall",
        "artist": "Oasis"
    }
]
~~~~
