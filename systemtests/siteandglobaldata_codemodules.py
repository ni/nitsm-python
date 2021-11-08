import nitsm.codemoduleapi
from nitsm.codemoduleapi import SemiconductorModuleContext


@nitsm.codemoduleapi.code_module
def set_global_data(tsm_context: SemiconductorModuleContext, data_id, data):
    tsm_context.set_global_data(data_id, data)


@nitsm.codemoduleapi.code_module
def check_global_data(tsm_context: SemiconductorModuleContext, data_id, data):
    site_count = len(tsm_context.site_numbers)
    global_data_exists = [tsm_context.global_data_exists(data_id)] * site_count
    tsm_context.publish_per_site(global_data_exists, "GlobalDataExists")

    valid_global_data = [tsm_context.get_global_data(data_id) == data] * site_count
    tsm_context.publish_per_site(valid_global_data, "ValidGlobalData")


@nitsm.codemoduleapi.code_module
def set_site_data(tsm_context: SemiconductorModuleContext, data_id, data):
    tsm_context.set_site_data(data_id, data)


@nitsm.codemoduleapi.code_module
def check_site_data(tsm_context: SemiconductorModuleContext, data_id, data):
    site_count = len(tsm_context.site_numbers)
    site_data_exists = [tsm_context.site_data_exists(data_id)] * site_count
    tsm_context.publish_per_site(site_data_exists, "SiteDataExists")

    valid_site_data = [tsm_context.get_site_data(data_id) == tuple(data)] * site_count
    tsm_context.publish_per_site(valid_site_data, "ValidSiteData")
