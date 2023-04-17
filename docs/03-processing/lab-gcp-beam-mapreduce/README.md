# Lab: MapReduce in Beam using Python

## Objective

In this lab, you will identify Map and Reduce operations, execute the pipeline, and use command line parameters.

Objectives:

- Identify Map and Reduce operations
- Execute the pipeline
- Use command line parameters

## Task 1. Lab preparations

Specific steps must be completed to successfully execute this lab.

### Open the SSH terminal and connect to the training VM

You will be running all code from a curated training VM.

1. In the Console, on the Navigation menu, click Compute Engine > VM instances.
2. Locate the line with the instance called training-vm.
3. On the far right, under Connect, click on SSH to open a terminal window.
4. In this lab, you will enter CLI commands on the training-vm.

### Clone the training github repository

- In the training-vm SSH terminal enter the following command:

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

## Task 2. Identify map and reduce operations

- Return to the training-vm SSH terminal and navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/python` and view the file `is_popular.py` with Nano. Do not make any changes to the code. Press Ctrl+X to exit Nano.

```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano is_popular.py
```

Can you answer these questions about the file `is_popular.py`?

- What custom arguments are defined?
- What is the default output prefix?
- How is the variable output_prefix in `main()` set?
- How are the pipeline arguments such as `--runner` set?
- What are the key steps in the pipeline?
- Which of these steps happen in parallel?
- Which of these steps are aggregations?

## Task 3. Execute the pipeline

- In the training-vm SSH terminal, run the pipeline locally:

```
python3 ./is_popular.py
```

- Identify the output file. It should be and could be a sharded file:

```
ls -al /tmp
```

- Examine the output file, replacing '-*' with the appropriate suffix:

```
cat /tmp/output-*
```

## Task 4. Use command line parameters

- In the training-vm SSH terminal, change the output prefix from the default value:

```
python3 ./is_popular.py --output_prefix=/tmp/myoutput
```

What will be the name of the new file that is written out?

Note that we now have a new file in the /tmp directory:

```
ls -lrt /tmp/myoutput*
```

![](https://user-images.githubusercontent.com/62965911/214003333-3272b2fe-aebd-4632-9345-bf8ee8c44e4a.png)

Congratulations!
