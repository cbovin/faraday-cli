from simple_rest_client.resource import Resource


class LoginResource(Resource):
    actions = {
        "auth": {"method": "POST", "url": "login"},
        "whoami": {"method": "GET", "url": "v3/whoami"},
        "get_token": {"method": "GET", "url": "v3/token"},
        "validate": {"method": "GET", "url": "v3/preferences"},
        "second_factor": {"method": "POST", "url": "confirmation"},
    }


class ConfigResource(Resource):
    actions = {
        "config": {"method": "GET", "url": "config"},
    }


class WorkspaceResource(Resource):
    actions = {
        "list": {"method": "GET", "url": "v3/ws"},
        "get": {"method": "GET", "url": "v3/ws/{}"},
        "create": {"method": "POST", "url": "v3/ws"},
        "delete": {"method": "DELETE", "url": "v3/ws/{}"},
    }


class BulkCreateResource(Resource):
    actions = {"create": {"method": "POST", "url": "v3/ws/{}/bulk_create"}}


class HostResource(Resource):
    actions = {
        "list": {"method": "GET", "url": "v3/ws/{}/hosts"},
        "get": {"method": "GET", "url": "v3/ws/{}/hosts/{}"},
        "create": {"method": "POST", "url": "v3/ws/{}/hosts"},
        "delete": {"method": "DELETE", "url": "v3/ws/{}/hosts/{}"},
        "get_services": {
            "method": "GET",
            "url": "v3/ws/{}/hosts/{}/services",
        },
        "get_vulns": {"method": "GET", "url": "v3/ws/{}/vulns"},
    }


class ServiceResource(Resource):
    actions = {
        "list": {"method": "GET", "url": "v3/ws/{}/services"},
        "get": {"method": "GET", "url": "v3/ws/{}/services/{}"},
    }


class VulnResource(Resource):
    actions = {
        "list": {"method": "GET", "url": "v3/ws/{}/vulns"},
        "filter": {"method": "GET", "url": "v3/ws/{}/vulns/filter"},
    }


class CredentialResource(Resource):
    actions = {
        "list": {"method": "GET", "url": "v3/ws/{}/credential"},
    }


class AgentResource(Resource):
    actions = {
        "list": {"method": "GET", "url": "v3/ws/{}/agents"},
        "get": {"method": "GET", "url": "v3/ws/{}/agents/{}"},
        "run": {"method": "POST", "url": "v3/ws/{}/agents/{}/run"},
    }


class ExecutiveReportResource(Resource):
    actions = {
        "list_templates": {
            "method": "GET",
            "url": "v3/ws/{}/reports/listTemplates",
        },
        "generate": {"method": "POST", "url": "v3/ws/{}/reports"},
        "status": {"method": "GET", "url": "v3/ws/{}/reports/{}"},
        "download": {"method": "GET", "url": "v3/ws/{}/reports/{}/download"},
    }
