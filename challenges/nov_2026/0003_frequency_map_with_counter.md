Practice Problem: Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.

I practiced on 11/12/2026

I couldn't find in one try, but my logic was good.

I didn't understand I had to import a package lmao.
It would have been much faster.

So what did I learn:
- You can import the counter function from collection packages to count nb of times each character appear in a string

What was my mistakes:
- I forgot to include the count = 1 inside the loop, so it wasn't being reset
- I forgot that .strip() only removes " " at the border
- Now I remember to use .replace() instead
- And also, enter the value directly inside .find()