"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[32165],{3905:(e,t,r)=>{r.d(t,{Zo:()=>f,kt:()=>u});var a=r(67294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function o(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},i=Object.keys(e);for(a=0;a<i.length;a++)r=i[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)r=i[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var s=a.createContext({}),c=function(e){var t=a.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):o(o({},t),e)),r},f=function(e){var t=c(e.components);return a.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,i=e.originalType,s=e.parentName,f=l(e,["components","mdxType","originalType","parentName"]),m=c(r),u=n,d=m["".concat(s,".").concat(u)]||m[u]||p[u]||i;return r?a.createElement(d,o(o({ref:t},f),{},{components:r})):a.createElement(d,o({ref:t},f))}));function u(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=r.length,o=new Array(i);o[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:n,o[1]=l;for(var c=2;c<i;c++)o[c]=r[c];return a.createElement.apply(null,o)}return a.createElement.apply(null,r)}m.displayName="MDXCreateElement"},65584:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>p,frontMatter:()=>i,metadata:()=>l,toc:()=>c});var a=r(87462),n=(r(67294),r(3905));const i={},o="Airflow Email Notifications",l={unversionedId:"orchestration/airflow/lab-airflow-email-notifications/README",id:"orchestration/airflow/lab-airflow-email-notifications/README",title:"Airflow Email Notifications",description:"1. Create AWS SES Identity with Email here.",source:"@site/docs/06-orchestration/airflow/lab-airflow-email-notifications/README.md",sourceDirName:"06-orchestration/airflow/lab-airflow-email-notifications",slug:"/orchestration/airflow/lab-airflow-email-notifications/",permalink:"/docs/orchestration/airflow/lab-airflow-email-notifications/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Airflow connection using Python",permalink:"/docs/orchestration/airflow/lab-airflow-conn-py/"},next:{title:"Getting Started with Airflow",permalink:"/docs/orchestration/airflow/lab-airflow-getting-started/"}},s={},c=[],f={toc:c};function p(e){let{components:t,...r}=e;return(0,n.kt)("wrapper",(0,a.Z)({},f,r,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"airflow-email-notifications"},"Airflow Email Notifications"),(0,n.kt)("ol",null,(0,n.kt)("li",{parentName:"ol"},(0,n.kt)("p",{parentName:"li"},"Create AWS SES Identity with Email ",(0,n.kt)("a",{parentName:"p",href:"https://us-east-1.console.aws.amazon.com/ses/home?region=us-east-1#/verified-identities/create"},"here"),".")),(0,n.kt)("li",{parentName:"ol"},(0,n.kt)("p",{parentName:"li"},"Configure Airflow Email setting with the following parameters:"),(0,n.kt)("pre",{parentName:"li"},(0,n.kt)("code",{parentName:"pre",className:"language-yaml"},"[email]\n # Email backend to use\n email_backend = airflow.providers.amazon.aws.utils.emailer.send_email\n\n # Email connection to use\n email_conn_id = aws_default\n\n # Whether email alerts should be sent when a task is retried\n default_email_on_retry = True\n\n # Whether email alerts should be sent when a task failed\n default_email_on_failure = True\n\n # Email address that will be used as sender address.\n from_email = Airflow <sprsag@gmail.com>\n"))),(0,n.kt)("li",{parentName:"ol"},(0,n.kt)("p",{parentName:"li"},"Run the DAG"))))}p.isMDXComponent=!0}}]);