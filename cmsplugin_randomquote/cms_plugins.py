from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Quote, RandomQuotePlugin, SingleQuotePlugin


class QuotePlugin(CMSPluginBase):
    """This plugin randomly renders a quote from the database."""
    model = RandomQuotePlugin
    name = _('Random Quotes')
    render_template = 'cmsplugin_randomquote/randomquotes.html'


    def render(self, context, instance, placeholder):
        try:
            context['quotes'] = Quote.objects.order_by('?')[:instance.amount]
        except IndexError:
            pass

        return context


class SingleQuotePlugin(CMSPluginBase):
    model = SingleQuotePlugin
    name = _('Quote')
    render_template = 'cmsplugin_randomquote/quote.html'

plugin_pool.register_plugin(QuotePlugin)
plugin_pool.register_plugin(SingleQuotePlugin)
