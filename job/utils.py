from company.models import Company


def create_object_from_field(data, fields):
    new_data = []
    for dt in data:
        payload = {'name': dt.get(fields[0])}
        list_update = [{field: dt.get(field, "")} for field in fields[1]]
        for dict_field in list_update:
            payload.update(dict_field)
        obj, created = Company.objects.get_or_create(**payload)
        dt[fields[0]] = obj.id
        new_data.append(dt)
    return new_data
