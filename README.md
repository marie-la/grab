## Grab is a simple working memory extension.

This will work best if:
1) you can quickly access a terminal via keyboard shortcut
2) you can bind 'grab' to 'python [path to python file] $argv'

There are lots of (key, value pairings) (phone numbers, random account numbers, emails, addresses) in our lives.
For example, if there's a wifi password you only have to remember sometimes,
first type "grab wifi [password]"

After that, just type "grab wifi" in the terminal to get the password directly in your clipboard.


Usage:

```
Set word: 'grab [term] "[mapping]"' or just 'grab [term]'

Get word: 'grab [term]'

Forgot key word? 'grab' to see all
```

Requirements:
'''
pyperclip, os, sys

'''

TODO:
- [ ] add encryption option
- [ ] improve searching for lost keyword
- [ ] 'undo' for accidentally overwriting term

Improvements:
- [x] implement deleting keyterm
