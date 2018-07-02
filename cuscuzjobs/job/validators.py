from apistar import validators
from apistar.types import Type


class Job(Type):
    job_id = validators.Number(title='Id')
    job_title = validators.String(title='Title')
    job_type = validators.String(title='Type', allow_null=True)
    experience_level = validators.String(
        title='Experience Level', allow_null=True)
    role = validators.String(title='Role', allow_null=True)
    industry = validators.String(title='Industry', allow_null=True)
    company_size = validators.String(
        title='Company Size', allow_null=True)
    company_type = validators.String(
        title='Company Type', allow_null=True)
    tecnologies = validators.Array(title='Tecnologies', min_items=1)
    job_description = validators.String(title='Description', allow_null=True)
    joel_test = validators.Array(title='Joel Tests', allow_null=True)
    link_apply = validators.String(title='Link', allow_null=True)
    benefits = validators.Array(title='Benefits', allow_null=True)
    company = validators.String(title='Company Name', allow_null=True)
    salary = validators.String(title='Salary', allow_null=True)
    sponsor = validators.String(title='Sponsor', allow_null=True)
    paid = validators.String(title='Paid', allow_null=True)
