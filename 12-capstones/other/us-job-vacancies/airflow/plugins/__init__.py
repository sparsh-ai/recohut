from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

import operators
import helpers

# Defining the plugin class
class WorkAroundTheWorldPlugin(AirflowPlugin):
    name = "work_around_the_world_plugin"
    operators = [
        operators.StageJsonToRedshiftOperator,
        operators.StageCsvToRedshiftOperator,
        operators.StageGithubJobsOperator,
        operators.StageLandingJobsOperator,
        operators.StageStackoverflowJobsOperator,
        operators.LoadFactOperator,
        operators.LoadDimensionOperator,
        operators.DataQualityOperator
    ]
    helpers = [
        helpers.SqlQueries
    ]
