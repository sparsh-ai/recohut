"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[87760],{3905:(e,t,n)=>{n.d(t,{Zo:()=>s,kt:()=>d});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function p(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},i=Object.keys(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)n=i[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var o=a.createContext({}),u=function(e){var t=a.useContext(o),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},s=function(e){var t=u(e.components);return a.createElement(o.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,o=e.parentName,s=p(e,["components","mdxType","originalType","parentName"]),m=u(n),d=r,h=m["".concat(o,".").concat(d)]||m[d]||c[d]||i;return n?a.createElement(h,l(l({ref:t},s),{},{components:n})):a.createElement(h,l({ref:t},s))}));function d(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,l=new Array(i);l[0]=m;var p={};for(var o in t)hasOwnProperty.call(t,o)&&(p[o]=t[o]);p.originalType=e,p.mdxType="string"==typeof e?e:r,l[1]=p;for(var u=2;u<i;u++)l[u]=n[u];return a.createElement.apply(null,l)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},72876:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>o,contentTitle:()=>l,default:()=>c,frontMatter:()=>i,metadata:()=>p,toc:()=>u});var a=n(87462),r=(n(67294),n(3905));const i={},l="Lab: MapReduce in Beam using Python",p={unversionedId:"processing/lab-gcp-beam-mapreduce/README",id:"processing/lab-gcp-beam-mapreduce/README",title:"Lab: MapReduce in Beam using Python",description:"Objective",source:"@site/docs/03-processing/lab-gcp-beam-mapreduce/README.md",sourceDirName:"03-processing/lab-gcp-beam-mapreduce",slug:"/processing/lab-gcp-beam-mapreduce/",permalink:"/docs/processing/lab-gcp-beam-mapreduce/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681732641,formattedLastUpdatedAt:"Apr 17, 2023",frontMatter:{},sidebar:"docs",previous:{title:"Lab: Apache Beam Getting Started",permalink:"/docs/processing/lab-getting-started-with-beam/"},next:{title:"Lab: GCP Dataflow Pipeline - A Simple Dataflow Pipeline (Python)",permalink:"/docs/processing/lab-gcp-dataflow-pipeline"}},o={},u=[{value:"Objective",id:"objective",level:2},{value:"Task 1. Lab preparations",id:"task-1-lab-preparations",level:2},{value:"Open the SSH terminal and connect to the training VM",id:"open-the-ssh-terminal-and-connect-to-the-training-vm",level:3},{value:"Clone the training github repository",id:"clone-the-training-github-repository",level:3},{value:"Task 2. Identify map and reduce operations",id:"task-2-identify-map-and-reduce-operations",level:2},{value:"Task 3. Execute the pipeline",id:"task-3-execute-the-pipeline",level:2},{value:"Task 4. Use command line parameters",id:"task-4-use-command-line-parameters",level:2}],s={toc:u};function c(e){let{components:t,...n}=e;return(0,r.kt)("wrapper",(0,a.Z)({},s,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"lab-mapreduce-in-beam-using-python"},"Lab: MapReduce in Beam using Python"),(0,r.kt)("h2",{id:"objective"},"Objective"),(0,r.kt)("p",null,"In this lab, you will identify Map and Reduce operations, execute the pipeline, and use command line parameters."),(0,r.kt)("p",null,"Objectives:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Identify Map and Reduce operations"),(0,r.kt)("li",{parentName:"ul"},"Execute the pipeline"),(0,r.kt)("li",{parentName:"ul"},"Use command line parameters")),(0,r.kt)("h2",{id:"task-1-lab-preparations"},"Task 1. Lab preparations"),(0,r.kt)("p",null,"Specific steps must be completed to successfully execute this lab."),(0,r.kt)("h3",{id:"open-the-ssh-terminal-and-connect-to-the-training-vm"},"Open the SSH terminal and connect to the training VM"),(0,r.kt)("p",null,"You will be running all code from a curated training VM."),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"In the Console, on the\xa0Navigation menu, click\xa0Compute Engine\xa0>\xa0VM instances."),(0,r.kt)("li",{parentName:"ol"},"Locate the line with the instance called\xa0training-vm."),(0,r.kt)("li",{parentName:"ol"},"On the far right, under\xa0Connect, click on\xa0SSH\xa0to open a terminal window."),(0,r.kt)("li",{parentName:"ol"},"In this lab, you will enter CLI commands on the\xa0training-vm.")),(0,r.kt)("h3",{id:"clone-the-training-github-repository"},"Clone the training github repository"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"In the\xa0training-vm\xa0SSH terminal enter the following command:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"git clone https://github.com/GoogleCloudPlatform/training-data-analyst\n")),(0,r.kt)("h2",{id:"task-2-identify-map-and-reduce-operations"},"Task 2. Identify map and reduce operations"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Return to the\xa0training-vm\xa0SSH terminal and navigate to the directory\xa0",(0,r.kt)("inlineCode",{parentName:"li"},"/training-data-analyst/courses/data_analysis/lab2/python"),"\xa0and view the file\xa0",(0,r.kt)("inlineCode",{parentName:"li"},"is_popular.py"),"\xa0with Nano.\xa0Do not make any changes to the code.\xa0Press\xa0Ctrl+X\xa0to exit Nano.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"cd ~/training-data-analyst/courses/data_analysis/lab2/python\nnano is_popular.py\n")),(0,r.kt)("p",null,"Can you answer these questions about the file\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"is_popular.py"),"?"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"What custom arguments are defined?"),(0,r.kt)("li",{parentName:"ul"},"What is the default output prefix?"),(0,r.kt)("li",{parentName:"ul"},"How is the variable output_prefix in\xa0",(0,r.kt)("inlineCode",{parentName:"li"},"main()"),"\xa0set?"),(0,r.kt)("li",{parentName:"ul"},"How are the pipeline arguments such as\xa0",(0,r.kt)("inlineCode",{parentName:"li"},"--runner"),"\xa0set?"),(0,r.kt)("li",{parentName:"ul"},"What are the key steps in the pipeline?"),(0,r.kt)("li",{parentName:"ul"},"Which of these steps happen in parallel?"),(0,r.kt)("li",{parentName:"ul"},"Which of these steps are aggregations?")),(0,r.kt)("h2",{id:"task-3-execute-the-pipeline"},"Task 3. Execute the pipeline"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"In the\xa0training-vm\xa0SSH terminal, run the pipeline locally:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"python3 ./is_popular.py\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Identify the output file. It should be and could be a sharded file:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"ls -al /tmp\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Examine the output file, replacing '-*' with the appropriate suffix:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"cat /tmp/output-*\n")),(0,r.kt)("h2",{id:"task-4-use-command-line-parameters"},"Task 4. Use command line parameters"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"In the\xa0training-vm\xa0SSH terminal, change the output prefix from the default value:")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"python3 ./is_popular.py --output_prefix=/tmp/myoutput\n")),(0,r.kt)("p",null,"What will be the name of the new file that is written out?"),(0,r.kt)("p",null,"Note that we now have a new file in the\xa0/tmp\xa0directory:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"ls -lrt /tmp/myoutput*\n")),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003333-3272b2fe-aebd-4632-9345-bf8ee8c44e4a.png",alt:null})),(0,r.kt)("p",null,"Congratulations!"))}c.isMDXComponent=!0}}]);