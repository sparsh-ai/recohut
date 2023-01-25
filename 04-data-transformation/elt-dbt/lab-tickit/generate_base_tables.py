import sys
import os
import yaml

from subprocess import Popen, PIPE


def exec_cli(cmd):

    process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()

    return out.decode(), err.decode()


def save_output(location, output):

    output_file = open(location, 'w')
    output_file.write(output)
    output_file.close()


schema_file_name = 'schema.yml'
packages_file_name = 'packages.yml'

dbt_labs_codegen = {
    'packages': [
        {
            'package': 'dbt-labs/codegen',
            'version': '0.6.0'
        }
    ]
}


if len(sys.argv) != 3:
    print('# Program: 2 arguments required - 1) dbt project name and 2) schema to extract base layer metadata.')

else:
    # Get dbt project and schema to extract base layer metadata
    dbt_project = sys.argv[1]
    schema = sys.argv[2]

    if not os.path.exists(dbt_project):
        print(f"# Program: No folder named {dbt_project} in same directory as generate_base_tables.py")

    else:
        # Change cwd to dbt project
        os.chdir(os.path.join(os.getcwd(), dbt_project))

        # Create packages.yml if not exists
        if not os.path.exists(packages_file_name):
            save_output(packages_file_name, yaml.dump(dbt_labs_codegen))

        # Pull dbt dependencies
        print('# Program: Pulling dependencies')

        out_deps, err_deps = exec_cli(['dbt', 'deps'])

        print(out_deps)

        if 'dbt-labs/codegen' not in out_deps:
            print('# Program: Require dbt-labs/codegen in packages.yml')

        else:
            # Create schema folder in models if not exists
            schema_folder = os.path.join('models', 'base_' + schema)

            if not os.path.exists(schema_folder):
                os.makedirs(schema_folder)

            # Extract tables in schema
            print(f"# Program: Creating or updating {schema_file_name}")

            out_schema, err_schema = exec_cli(['dbt', 'run-operation', 'generate_source', '--args', f"{{'schema_name': '{schema}'}}"])

            if 'Database Error' in out_schema:
                print(out_schema)

            elif 'Compilation Error' in out_schema:
                print(out_schema)

            else:
                # Clean output_schema
                output_schema_list = out_schema.split('\n')
                output_schema_list = output_schema_list[output_schema_list.index('sources:'):]

                output_schema_final = '\n'.join(output_schema_list)

                print(output_schema_final)

                # Save output
                save_output(os.path.join(schema_folder, schema_file_name), 'version: 2\n\n' + output_schema_final)

                # Convert output to dict
                output_schema_dict = yaml.safe_load(output_schema_final)

                # Parse dict
                for schema_details in output_schema_dict['sources']:
                    
                    schema_name = schema_details['name']
                    schema_tables = schema_details['tables']

                    if schema_tables is None:
                        print(f"# Program: No tables in schema {schema}")

                    else:
                        # For each table, generate base model for reference
                        for table_details in schema_tables:

                            table_name = table_details['name']

                            print(f"# Program: Generating base model file for: {schema_name}.{table_name}")

                            out_table, err_table = exec_cli(['dbt', 'run-operation', 'generate_base_model', '--args', f"{{'source_name': '{schema_name}', 'table_name': '{table_name}'}}"])

                            output_table_list = out_table.split('\n')
                            output_table_list = output_table_list[output_table_list.index('with source as ('):]

                            output_table_final = '\n'.join(output_table_list)

                            print(output_table_final)

                            save_output(os.path.join(schema_folder, f"base_{schema_name}_{table_name}.sql"), output_table_final)
