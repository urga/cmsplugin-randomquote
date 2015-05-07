from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Quote, RandomQuotePlugin


class QuotePlugin(CMSPluginBase):
    """This plugin randomly renders a quote from the database."""
    name = _('Quote')
    render_template = 'cmsplugin_randomquote/quote.html'
    model = RandomQuotePlugin

    def render(self, context, instance, placeholder):
        try:
            context['quotes'] = Quote.objects.order_by('?')[:instance.amount]
        except IndexError:
            pass

        return context

plugin_pool.register_plugin(QuotePlugin)
