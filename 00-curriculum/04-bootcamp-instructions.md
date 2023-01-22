# Bootcamp Instructions

## Assignments

- In assignments, you’re given a scenario and a set of tasks. Instead of following step-by-step instructions, you will use the skills learned from the classes to figure out how to complete the tasks on your own!
- When you take an assignment, you will not be taught new concepts. You are expected to extend your learned skills, like changing default values and reading and researching error messages to fix your own mistakes.
- To score 100% you must successfully complete all tasks within the time period!

## Project Process

```mermaid
flowchart TD
    A[Start] --> C[Understand the Project overview and Prerequisites]
    subgraph Prerequisite
    C --> D[Complete the Prerequisites]
    D --> E{Project Prerequisite Test}
    end
    subgraph Development
    E --> |Passed| B[Setup the initial project template in your git]
    E --> |Failed| C
    B --> F[Develop the Project - Test driven development]
    F --> G[Request for the Peer review and get the sign-off]
    G --> H{Signed-off}
    end
    subgraph Production
    H --> |No| F
    H --> |Yes| I[Deploy the Project]
    I --> J[Complete the Documentation]
    J --> K[Release the Project]
    K --> L[Add the project in your resume - Resume Buildup]
    L --> M[Take the Project Mock Interview - Full Mock]
    end
    M --> N[End]
    click C callback "Tooltip for a callback"
```

## Techstack

![techstack](https://user-images.githubusercontent.com/62965911/213917222-605aeffc-e909-4242-8649-9305e059e8ec.svg)