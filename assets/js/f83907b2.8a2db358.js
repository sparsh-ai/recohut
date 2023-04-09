"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[71868],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>d});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var o=n.createContext({}),u=function(e){var t=n.useContext(o),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},p=function(e){var t=u(e.components);return n.createElement(o.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,l=e.originalType,o=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),m=u(a),d=r,b=m["".concat(o,".").concat(d)]||m[d]||c[d]||l;return a?n.createElement(b,i(i({ref:t},p),{},{components:a})):n.createElement(b,i({ref:t},p))}));function d(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var l=a.length,i=new Array(l);i[0]=m;var s={};for(var o in t)hasOwnProperty.call(t,o)&&(s[o]=t[o]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var u=2;u<l;u++)i[u]=a[u];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},27381:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>o,contentTitle:()=>i,default:()=>c,frontMatter:()=>l,metadata:()=>s,toc:()=>u});var n=a(87462),r=(a(67294),a(3905));const l={},i="Streaming Data Processing - Publish Streaming Data into PubSub",s={unversionedId:"processing/lab-gcp-pubsub",id:"processing/lab-gcp-pubsub",title:"Streaming Data Processing - Publish Streaming Data into PubSub",description:"Objective",source:"@site/docs/03-processing/lab-gcp-pubsub.md",sourceDirName:"03-processing",slug:"/processing/lab-gcp-pubsub",permalink:"/docs/processing/lab-gcp-pubsub",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Streaming Data Processing - Streaming Data Pipelines",permalink:"/docs/processing/lab-gcp-pubsub-processing"},next:{title:"GCP Serverless Dataflow",permalink:"/docs/processing/lab-gcp-serverless-dataflow"}},o={},u=[{value:"Objective",id:"objective",level:2},{value:"Preparation",id:"preparation",level:2},{value:"Create Pub/Sub topic and subscription",id:"create-pubsub-topic-and-subscription",level:2},{value:"Simulate traffic sensor data into Pub/Sub",id:"simulate-traffic-sensor-data-into-pubsub",level:2},{value:"Verify that messages are received",id:"verify-that-messages-are-received",level:2}],p={toc:u};function c(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},p,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"streaming-data-processing---publish-streaming-data-into-pubsub"},"Streaming Data Processing - Publish Streaming Data into PubSub"),(0,r.kt)("h2",{id:"objective"},"Objective"),(0,r.kt)("p",null,"Google Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications. Use Cloud Pub/Sub to publish and subscribe to data from multiple sources, then use Google Cloud Dataflow to understand your data, all in real time."),(0,r.kt)("p",null,"In this lab, you will simulate your traffic sensor data into a Pub/Sub topic for later to be processed by Dataflow pipeline before finally ending up in a BigQuery table for further analysis."),(0,r.kt)("p",null,"In this lab, you will perform the following tasks:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Create a Pub/Sub topic and subscription"),(0,r.kt)("li",{parentName:"ul"},"Simulate your traffic sensor data into Pub/Sub")),(0,r.kt)("h2",{id:"preparation"},"Preparation"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Go to the Compute > VM > training-vm instance"),(0,r.kt)("li",{parentName:"ul"},"Connect via SSH"),(0,r.kt)("li",{parentName:"ul"},"Verify by listing our the files - ",(0,r.kt)("inlineCode",{parentName:"li"},"ls /training"))),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/211212971-f62f3c34-cec9-4969-821a-75a1b97cdb60.png",alt:null})),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Next you will download a code repository for use in this lab:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"git clone https://github.com/GoogleCloudPlatform/training-data-analyst\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Set the DEVSHELL_PROJECT_ID environment variable and export it so it will be available to other shells:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"export DEVSHELL_PROJECT_ID=$(gcloud config get-value project)\n")),(0,r.kt)("h2",{id:"create-pubsub-topic-and-subscription"},"Create Pub/Sub topic and subscription"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"On the training-vm SSH terminal, navigate to the directory for this lab:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"cd ~/training-data-analyst/courses/streaming/publish\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Create your topic and publish a simple message:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"gcloud pubsub topics create sandiego\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Publish a simple message:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'gcloud pubsub topics publish sandiego --message "hello"\n')),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Create a subscription for the topic:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"gcloud pubsub subscriptions create --topic sandiego mySub1\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Pull the first message that was published to your topic:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"gcloud pubsub subscriptions pull --auto-ack mySub1\n")),(0,r.kt)("p",null,"Do you see any result? If not, why?"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Try to publish another message and then pull it using the subscription:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'gcloud pubsub topics publish sandiego --message "hello again"\ngcloud pubsub subscriptions pull --auto-ack mySub1\n')),(0,r.kt)("p",null,"Did you get any response this time?"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"In the training-vm SSH terminal, cancel your subscription:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"gcloud pubsub subscriptions delete mySub1\n")),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/211212970-18a2c9ef-0725-422d-862d-2d88c4e38bc2.png",alt:null})),(0,r.kt)("h2",{id:"simulate-traffic-sensor-data-into-pubsub"},"Simulate traffic sensor data into Pub/Sub"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Explore the python script to simulate San Diego traffic sensor data. Do not make any changes to the code.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"cd ~/training-data-analyst/courses/streaming/publish\nnano send_sensor_data.py\n")),(0,r.kt)("p",null,"Look at the simulate function. This one lets the script behave as if traffic sensors were sending in data in real time to Pub/Sub. The speedFactor parameter determines how fast the simulation will go. Exit the file by pressing Ctrl+X."),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Download the traffic simulation dataset:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"./download_data.sh\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Simulate streaming sensor data. Run the send_sensor_data.py:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"./send_sensor_data.py --speedFactor=60 --project $DEVSHELL_PROJECT_ID\n")),(0,r.kt)("p",null,'This command simulates sensor data by sending recorded sensor data via Pub/Sub messages. The script extracts the original time of the sensor data and pauses between sending each message to simulate realistic timing of the sensor data. The value\xa0speedFactor\xa0changes the time between messages proportionally. So a\xa0speedFactor\xa0of 60 means "60 times faster" than the recorded timing. It will send about an hour of data every 60 seconds.'),(0,r.kt)("p",null,"Leave this terminal open and the simulator running."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/211212968-b34434d3-046a-486f-9f96-d98da24243dc.png",alt:null})),(0,r.kt)("h2",{id:"verify-that-messages-are-received"},"Verify that messages are received"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Open a second SSH terminal and connect to the training VM")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Change into the directory you were working in:"))),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"cd ~/training-data-analyst/courses/streaming/publish\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Create a subscription for the topic and do a pull to confirm that messages are coming in (note: you may need to issue the 'pull' command more than once to start seeing messages):")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"gcloud pubsub subscriptions create --topic sandiego mySub2\ngcloud pubsub subscriptions pull --auto-ack mySub2\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Confirm that you see a message with traffic sensor information.")),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/211212961-0bdc468e-d6ea-4b16-8904-98c1ac231ebf.png",alt:null})),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Cancel this subscription:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"gcloud pubsub subscriptions delete mySub2\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Close the second terminal:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"exit\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Stop the sensor simulator. Return to the first terminal.")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Interrupt the publisher by typing Ctrl+C to stop it.")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("p",{parentName:"li"},"Close the first terminal:"))),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"exit\n")))}c.isMDXComponent=!0}}]);