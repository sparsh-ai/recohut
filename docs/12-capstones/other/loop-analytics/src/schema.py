import re

import yaml
import glob
import os
import logging
import sys

class Schema:
    def __init__(self, schema_name):
        self.directory = os.path.dirname(__file__).replace('packages', 'schema') + '/' + schema_name
        self.name = schema_name
        self.schema_def = self.createSchemaDef(self.directory)
        self.schema_perms = self.getSchemaPerms(self.directory)
        self.transforms = {}

    def set_transforms(self, transform_map: dict = {}):
        self.transforms = transform_map

    def createSchemaDef(self, yaml_dir):
        schema = {}
        table_defs = glob.glob(yaml_dir + '/*.yaml')
        for f in table_defs:
            logging.debug('parsing yaml for {}'.format(f))
            if f == '_user_permissions.yaml':
                continue  # skip special object
            file_obj = open(f, 'r')
            table_def = yaml.load(file_obj, Loader=yaml.FullLoader)
            file_obj.close()
            schema.update(table_def)
        return schema

    def getSchemaPerms(self, yaml_dir):
        perms_file = yaml_dir + '/' + '_user_permissions.yaml'
        schema_perms = {}
        if os.path.isfile(perms_file):
            with open(perms_file, 'r') as f:
                schema_perms = yaml.load(f, Loader=yaml.FullLoader)
        return schema_perms

    def getSchemaTables(self):
        return list(self.schema_def.keys())

    def getSchemaName(self):
        return self.name

    def transform(self, field_name, transform_name: str = None, parameters: dict = {} ):
        template = self.transforms.get(transform_name)
        if template:
            replacements = {'field_name': field_name}
            replacements.update(parameters)
            field_name = eval("template.format({})".format(", ".join(["{}='{}'".format(k, v) for k, v in replacements.items()])))

        return field_name

    def getTableFields(self, table_name):
        return [self.transform(field['name'], transform_name=field.get('transform'), parameters=field.get('parameters')) for field in self.schema_def[table_name]['fields']]

    def getTableReplaceKeys(self, table_name):
        return self.schema_def[table_name]['incremental_replace_keys']

    def makeEmptyRow(self, table_name):
        """
        This function returns an dictionary with no values for a
        new record in a given table of the schema. The keys (or headers)
        are by default the name of the field, but if there is a key or key
        prefix (used for mapping json to a flat structure), those are used.
        """
        empty_row = {}
        for field in self.schema_def[table_name]['fields']:
            field_key = field.get('name') if not field.get('event_name') else field.get('event_name')
            if field.get('key_prefix'):
                field_key = field.get('key_prefix') + '.' + field_key
            elif field.get('key'):
                field_key = field.get('key')
            empty_row[field_key] = None
        return empty_row

    def getKeyEquivalencyMap(self, table_name):
        """
        This function returns a map of {key_equivalency: key} for the table name.
        This is useful when multiple json keys can relate to the same tablular
        data element. When that happens you can declare a key key_equivalency
        in the yaml and than use this function to replace the equivalent values
        to the expected key value.
        """
        returnData = {}
        for field in self.schema_def[table_name]['fields']:
            equivalencies = field.get('key_equivalencies')
            if equivalencies:
                for equivalency in equivalencies:
                    returnData[equivalency] = field['key']  # expect key there if we have equivalencies
        return returnData


if __name__ == '__main__':
    # Test Code
    schema = Schema('public')
    schema.set_transforms({
            'json': "CONVERT_FROM(loread(lo_open({field_name}::int,x'40000'::int),'{max_size}'::int),'UTF8') as {field_name}"
        })

    table_name = 'tekmetric_repair_orders'
    template = """
                SELECT {fields}
                FROM {schema}.{table}
                {time_range_filter}
                ORDER BY {idx_col}
                OFFSET {offset}
                FETCH NEXT {chunk_size} ROWS ONLY
            """.format(
                fields=',\n'.join([x for x in schema.getTableFields(table_name)]),
                schema='app_db',
                table=table_name,
                time_range_filter="{time_range_filter}",
                idx_col="{idx_col}",
                offset="{retrieved}",
                chunk_size="{this_chunk}"
            )
    print(template)