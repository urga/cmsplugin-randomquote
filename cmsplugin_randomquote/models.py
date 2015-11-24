from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from cms.models.pluginmodel import CMSPlugin


@python_2_unicode_compatible
class Quote(models.Model):
    quote_text = models.TextField(_(u'Quote Text'))
    author = models.CharField(_(u'Author'), max_length=255)
    author_url = models.URLField(_(u'Author URL'), null=True, blank=True, default=None, max_length=255)

    def __str__(self):
        return '[%s] %s...' % (self.author, self.quote_text[:20])


@python_2_unicode_compatible
class RandomQuotePlugin(CMSPlugin):
    amount = models.IntegerField(
        default=1,
        help_text=_('The number of random quotes to be displayed.')
    )

    def __str__(self):
        return 'displaying %s' % (self.amount)


@python_2_unicode_compatible
class SingleQuotePlugin(CMSPlugin):
    quote = models.ForeignKey(Quote)

    def __str__(self):
        return str(self.quote)
