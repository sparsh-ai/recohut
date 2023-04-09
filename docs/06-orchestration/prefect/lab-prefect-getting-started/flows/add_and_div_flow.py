from prefect import task, flow

@task
def add_num(a, b):
    return a + b

@task
def div_num(a, b):
    return a / b

@flow
def add_and_div_flow(seed=100):
    c = add_num(seed, 20)
    d = div_num(c, 20)
    print(d)
    
if __name__ == "__main__":
    add_and_div_flow(seed=20)
