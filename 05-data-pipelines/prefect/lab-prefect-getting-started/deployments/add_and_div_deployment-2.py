from prefect.deployments import DeploymentSpec

DeploymentSpec(
    name="add-and-div-deployment-2",
    flow_location="./flows/add_and_div_flow_2.py",
    tags=['tutorial','test'],
    parameters={'seed':10}
)
