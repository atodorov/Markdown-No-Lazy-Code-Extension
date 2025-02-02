import xml.etree.ElementTree as etree

from markdown import util, Extension
from markdown.blockprocessors import CodeBlockProcessor
from markdown.preprocessors import NormalizeWhitespace


class NLCodeExtension(Extension):
    def extendMarkdown(self, md):
        # from markdown/blockprocessors.py
        md.parser.blockprocessors.register(NLCodeProcessor(md.parser), 'code', 80)

        # from markdown/preprocessors.py
        md.preprocessors.register(KeepLeadingSpaces(md), 'normalize_whitespace', 30)


class KeepLeadingSpaces(NormalizeWhitespace):
    """ Keep leading spaces between newlines. """

    def run(self, lines):
        source = '\n'.join(lines)
        source = source.replace(util.STX, "").replace(util.ETX, "")
        source = source.replace("\r\n", "\n").replace("\r", "\n") + "\n\n"
        source = source.expandtabs(self.md.tab_length)
# here we've removed a regex substitution from NormalizeWhitespace
        return source.split('\n')


class NLCodeProcessor(CodeBlockProcessor):

    def run(self, parent, blocks):
        sibling = self.lastChild(parent)
        block = blocks.pop(0)
        theRest = ''

        pre = etree.SubElement(parent, 'pre')
        code = etree.SubElement(pre, 'code')
        block, theRest = self.detab(block)
        code.text = util.AtomicString('%s\n' % block.rstrip())

        if theRest:
            # This block contained unindented line(s) after the first indented
            # line. Insert these lines as the first block of the master blocks
            # list for future processing.
            blocks.insert(0, theRest)


def makeExtension(*args, **kwargs):
    return NLCodeExtension(*args, **kwargs)
