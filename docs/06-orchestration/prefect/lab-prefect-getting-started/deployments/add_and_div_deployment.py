from prefect.deployments import DeploymentSpec

DeploymentSpec(
    name="add-and-div-deployment",
    flow_location="./flows/add_and_div_flow.py",
    tags=['tutorial','test'],
    parameters={'seed':10}
)
