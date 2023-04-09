"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[75729],{3905:(e,t,r)=>{r.d(t,{Zo:()=>d,kt:()=>h});var a=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function n(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function s(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?n(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):n(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,a,o=function(e,t){if(null==e)return{};var r,a,o={},n=Object.keys(e);for(a=0;a<n.length;a++)r=n[a],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(a=0;a<n.length;a++)r=n[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var c=a.createContext({}),l=function(e){var t=a.useContext(c),r=t;return e&&(r="function"==typeof e?e(t):s(s({},t),e)),r},d=function(e){var t=l(e.components);return a.createElement(c.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},p=a.forwardRef((function(e,t){var r=e.components,o=e.mdxType,n=e.originalType,c=e.parentName,d=i(e,["components","mdxType","originalType","parentName"]),p=l(r),h=o,b=p["".concat(c,".").concat(h)]||p[h]||u[h]||n;return r?a.createElement(b,s(s({ref:t},d),{},{components:r})):a.createElement(b,s({ref:t},d))}));function h(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var n=r.length,s=new Array(n);s[0]=p;var i={};for(var c in t)hasOwnProperty.call(t,c)&&(i[c]=t[c]);i.originalType=e,i.mdxType="string"==typeof e?e:o,s[1]=i;for(var l=2;l<n;l++)s[l]=r[l];return a.createElement.apply(null,s)}return a.createElement.apply(null,r)}p.displayName="MDXCreateElement"},15228:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>c,contentTitle:()=>s,default:()=>u,frontMatter:()=>n,metadata:()=>i,toc:()=>l});var a=r(87462),o=(r(67294),r(3905));const n={},s="Cybersecurity Databricks",i={unversionedId:"processing/databricks/lab-cybersecurity-databricks/README",id:"processing/databricks/lab-cybersecurity-databricks/README",title:"Cybersecurity Databricks",description:"Objective",source:"@site/docs/03-processing/databricks/lab-cybersecurity-databricks/README.md",sourceDirName:"03-processing/databricks/lab-cybersecurity-databricks",slug:"/processing/databricks/lab-cybersecurity-databricks/",permalink:"/docs/processing/databricks/lab-cybersecurity-databricks/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Boston Crime Analysis",permalink:"/docs/processing/databricks/boston-crime-analysis/"},next:{title:"Databricks AWS Integration and Clickstream Analysis",permalink:"/docs/processing/databricks/lab-databricks-clickstream/"}},c={},l=[{value:"Objective",id:"objective",level:2},{value:"Introduction",id:"introduction",level:2},{value:"Architecture",id:"architecture",level:2}],d={toc:l};function u(e){let{components:t,...r}=e;return(0,o.kt)("wrapper",(0,a.Z)({},d,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"cybersecurity-databricks"},"Cybersecurity Databricks"),(0,o.kt)("h2",{id:"objective"},"Objective"),(0,o.kt)("p",null,"Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events"),(0,o.kt)("h2",{id:"introduction"},"Introduction"),(0,o.kt)("p",null,"Endpoint data is required by security teams for threat detection, threat hunting, incident investigations and to meet compliance requirements. The data volumes can be terabytes per day or petabytes per year. Most organizations struggle to collect, store and analyze endpoint logs because of the costs and complexities associated with such large data volumes. But it doesn\u2019t have to be this way."),(0,o.kt)("p",null,"In this lab, we will learn how to operationalize petabytes of endpoint data with Databricks to improve the organizations's security posture with advanced analytics in a cost-effective way. "),(0,o.kt)("p",null,"We will use CrowdStrike\u2019s Falcon logs as our example. To access Falcon logs, one can use the Falcon Data Replicator (FDR) to push raw event data from CrowdStrike\u2019s platform to cloud storage such as Amazon S3. This data can be ingested, transformed, analyzed and stored using the Databricks Lakehouse Platform alongside the rest of their security telemetry. Customers can ingest CrowdStrike Falcon data, apply Python-based real-time detections, search through historical data with Databricks SQL, and query from SIEM tools like Splunk with Databricks Add-on for Splunk."),(0,o.kt)("h2",{id:"architecture"},"Architecture"),(0,o.kt)("p",null,"Auto Loader and Delta Lake simplify the process of reading raw data from cloud storage and writing to a Delta table at low cost and with minimal DevOps work. In this architecture, semi-structured CrowdStrike data is loaded to the customer\u2019s cloud storage in the landing zone. Then Auto Loader uses cloud notification services to automatically trigger the processing and ingestion of new files into the customer\u2019s Bronze tables, which will act as the single source of truth for all downstream jobs. Auto Loader will track processed and unprocessed files using checkpoints in order to prevent duplicate data processing. "),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214503749-fa3a5650-4dd6-4820-89d9-3a9bb7a72b19.png",alt:null})),(0,o.kt)("p",null,"As we move from the Bronze to the Silver stage, schema will be added to provide structure to the data. Since we are reading from a single source of truth, we are able to process all of the different event types and enforce the correct schema as they are written to their respective tables. The ability to enforce schemas at the Silver layer provides a solid foundation for building ML and analytical workloads."),(0,o.kt)("p",null,"The Gold stage, which aggregates data for faster query and performance in dashboards and BI tools, is optional, depending on the use case and data volumes. Alerts can be set to trigger when unexpected trends are observed. "),(0,o.kt)("p",null,"Another optional feature is the Databricks Add-on for Splunk, which allows security teams to take advantage of Databricks cost-effective model and the power of AI without having to leave the comforts of Splunk. Customers can run ad hoc queries against Databricks from within a Splunk dashboard or search bar with the add-on. Users can also launch notebooks or jobs in Databricks through a Splunk dashboard or in response to a Splunk search. The Databricks integration is bidirectional, letting customers summarize noisy data or run detections in Databricks that show up in Splunk Enterprise Security. Customers can even run Splunk searches from within a Databricks notebook to prevent the need to duplicate data."),(0,o.kt)("p",null,"The Splunk and Databricks integration allows customers to reduce costs, expand the data sources they analyze and provide the results of a more robust analytics engine, all without changing the tools used by their staff day-to-day."))}u.isMDXComponent=!0}}]);