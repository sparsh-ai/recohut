// import React from 'react';
// import styles from './styles.module.css';
// import TimelineSvg from '@site/static/img/timeline.svg'
// import TechstackSvg from '@site/static/img/techstack.svg'

// function Timeline() {
//     return (
//       <div className={styles.Container}>
//         <h1>Our Timeline</h1>
//         <br/>
//         <TimelineSvg/>
//       </div>
//     );
//   }

//   function Techstack() {
//     return (
//       <div className={styles.Container}>
//         <h1>Our Techstack</h1>
//         <br/>
//         <TechstackSvg/>
//       </div>
//     );
//   }

//   export {Timeline, Techstack};

import React from 'react';
import styles from './styles.module.css';
import TechStackSvg from '@site/static/img/techstack.svg'
import { EditFilled, NotificationFilled, PlayCircleFilled, UpSquareFilled, CalendarOutlined } from '@ant-design/icons';
import { Timeline, Button, Popover } from 'antd';

function TechStack() {
  return (
    <div className={styles.Container}>
      <h1>Our Tech Stack</h1>
      <br/>
      <TechStackSvg/>
    </div>
  );
}

const week1 = (
  <div>
    <ol>
      <li>Candidate Onboarding</li>
      <li>Workspace Setup</li>
      <li>Fundamentals of Data Engineering</li>
    </ol>
  </div>
);

const week2 = (
  <div>
    <ol>
      <li>SQL Data Modeling with Postgres</li>
      <li>Data Warehousing with Snowflake</li>
      <li>Data Lakes with S3</li>
    </ol>
  </div>
);

const week3 = (
  <div>
    <ol>
      <li>Data Transformation with Python</li>
      <li>Data Transformation with SQL</li>
      <li>Data Transformation with AWS Lambda</li>
    </ol>
  </div>
);

const week4 = (
  <div>
    <ol>
      <li>Data Pipeline and Orchestration with Apache Airflow</li>
      <li>IaC with AWS CloudFormation</li>
      <li>NoSQL Data Modeling with Cassandra</li>
      <li>Data Warehousing with Amazon Redshift</li>
    </ol>
  </div>
);

const week5 = (
  <div>
    <ol>
      <li>Data Lakehouses with Delta Lake</li>
      <li>Data Transformation with Databricks PySpark</li>
    </ol>
  </div>
);

const week6 = (
  <div>
    <ol>
      <li>Data Transformation with AWS Glue Studio</li>
      <li>Data Transformation with dbt</li>
      <li>Data Quality and Validation with Great Expectations</li>
      <li>Real-time Event Streaming with Apache Kafka</li>
      <li>Real-time Event Streaming with Amazon Kinesis</li>
    </ol>
  </div>
);

const week7 = (
  <div>
    <ol>
      <li>REST API with FastAPI</li>
      <li>CICD Pipeline with GitHub Actions</li>
      <li>Advanced Data Engineering with Databricks</li>
      <li>Change Data Capture with Debezium</li>
    </ol>
  </div>
);

function BootcampTimeline() {
  return (
    <div className={styles.Container}>
      <h1>Bootcamp Timeline</h1>
      <br/>
      <Timeline mode="alternate">
      <Timeline.Item
            dot={
              <PlayCircleFilled
                style={{
                  fontSize: '16px',
                  color: "#ba8c0d",
                }}
              />
            }
          > 
          Bootcamp Session Starts on Zoom
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week1} title="Week 1">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 1</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week2} title="Week 2">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 2</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week3} title="Week 3">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 3</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week4} title="Week 4">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 4</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week5} title="Week 5">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 5</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week6} title="Week 6">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 6</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item color="#ba8c0d">
        <Popover content={week7} title="Week 7">
          <Button type="primary" shape="round" style={{ background: "#ba8c0d", borderColor: "#ba8c0d" }} icon={<CalendarOutlined />}>Week 7</Button>
        </Popover>
      </Timeline.Item>
      <Timeline.Item
            dot={
              <NotificationFilled
                style={{
                  fontSize: '16px',
                  color: "#ba8c0d"
                }}
              />
            }
          > Bootcamp Session Ends and Marketing Starts
      </Timeline.Item>
      </Timeline>
    </div>
  );
}

export {TechStack, BootcampTimeline};