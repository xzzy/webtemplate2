from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'webtemplate_dpaw/base.html'

    def get_context_data(self, **kwargs):
        context = super(TestPage, self).get_context_data(**kwargs)
        context['page_title'] = 'Test page'
        context['page_description'] = 'Meta tag page description'
        context['site_title'] = 'SITE TITLE'
        return context


class TestDBCAPage(TemplateView):
    template_name = 'webtemplate_dpaw/base_dbca.html'

    def get_context_data(self, **kwargs):
        context = super(TestDBCAPage, self).get_context_data(**kwargs)
        context['page_title'] = 'Test page'
        context['page_description'] = 'Meta tag page description'
        context['site_title'] = 'SITE TITLE'
        return context


class TestPage2(TestPage):
    template_name = 'test_template.html'


class TestInternetPage(TemplateView):
    template_name = 'webtemplate_dpaw/base_internet.html'

    def get_context_data(self, **kwargs):
        context = super(TestInternetPage, self).get_context_data(**kwargs)
        context['page_title'] = 'Test page'
        context['page_description'] = 'Meta tag page description'
        context['site_title'] = 'SITE TITLE'
        return context
