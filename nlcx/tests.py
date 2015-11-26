#!/usr/bin/env python

import unittest
from markdown import Markdown


class NLBQExtensionTest(unittest.TestCase):

    # list of tuples (description, markup, expected)
    test_cases = [
(
"one code block with indented newline",
"""
    if not anaconda.isKickstart:
        self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))
    
    if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
        asUtc = True
""",
"""
<pre><code>if not anaconda.isKickstart:
    self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))

if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
    asUtc = True
</code></pre>
"""),

(
"two code blocks divided by newline",
"""
    if not anaconda.isKickstart:
        self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))

    if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
        asUtc = True
""",
"""
<pre><code>if not anaconda.isKickstart:
    self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))
</code></pre>
<pre><code>if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
    asUtc = True
</code></pre>
"""),

(
"two code blocks divided by regular text",
"""
    if not anaconda.isKickstart:
        self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))

Next file looks like

    if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
        asUtc = True
""",
"""
<pre><code>if not anaconda.isKickstart:
    self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))
</code></pre>
<p>Next file looks like</p>
<pre><code>if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
    asUtc = True
</code></pre>
"""),


]

    def setUp(self):
        self.md = Markdown(extensions=['nlcx'])

    def runTest(self):
        for (description, markup, expected) in self.test_cases:
            self.assertEquals(self.md.convert(markup), expected.strip(), msg=description)


if __name__ == "__main__":
    unittest.main()
