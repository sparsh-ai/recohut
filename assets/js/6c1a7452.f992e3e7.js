"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[39910],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>m});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function s(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var l=a.createContext({}),p=function(e){var t=a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):s(s({},t),e)),n},c=function(e){var t=p(e.components);return a.createElement(l.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},u=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,l=e.parentName,c=i(e,["components","mdxType","originalType","parentName"]),u=p(n),m=r,h=u["".concat(l,".").concat(m)]||u[m]||d[m]||o;return n?a.createElement(h,s(s({ref:t},c),{},{components:n})):a.createElement(h,s({ref:t},c))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,s=new Array(o);s[0]=u;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i.mdxType="string"==typeof e?e:r,s[1]=i;for(var p=2;p<o;p++)s[p]=n[p];return a.createElement.apply(null,s)}return a.createElement.apply(null,n)}u.displayName="MDXCreateElement"},85815:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>d,frontMatter:()=>o,metadata:()=>i,toc:()=>p});var a=n(87462),r=(n(67294),n(3905));const o={},s="Logsense",i={unversionedId:"assignments/logsense/README",id:"assignments/logsense/README",title:"Logsense",description:"Lab 1: Apache Server Log Analysis",source:"@site/docs/11-assignments/logsense/README.md",sourceDirName:"11-assignments/logsense",slug:"/assignments/logsense/",permalink:"/docs/assignments/logsense/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Klodars Datalake Design",permalink:"/docs/assignments/klodars-datalake-design/"},next:{title:"Mistplay Data Engineer Take Home Challenge",permalink:"/docs/assignments/mistplay-takehome/"}},l={},p=[{value:"Lab 1: Apache Server Log Analysis",id:"lab-1-apache-server-log-analysis",level:2}],c={toc:p};function d(e){let{components:t,...n}=e;return(0,r.kt)("wrapper",(0,a.Z)({},c,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"logsense"},"Logsense"),(0,r.kt)("h2",{id:"lab-1-apache-server-log-analysis"},"Lab 1: Apache Server Log Analysis"),(0,r.kt)("p",null,"This lab is designed to help gain an understanding of working with the error log of a website and user interaction on different modules of a website. You should be able to analyze the dataset for this project to create a report. You will be able to use PySpark, do analyses, and obtain the desired results."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Objectives")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Perform server log analysis to assist businesses in identifying and analyzing critical business errors"),(0,r.kt)("li",{parentName:"ul"},"Identify potential customers and their domains")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Problem Statement")),(0,r.kt)("p",null,'The Apache services such as Hadoop, Spark, Tomcat, and Hive run on most data engineering servers throughout the world. All the services follow the same pattern because they are all open source. You are a data engineer who works for a start-up named "Logsense", which serves major clientele.'),(0,r.kt)("p",null,"You have been assigned to one of their prestigious clients to resolve a production issue. As you are dealing with Hadoop, you are familiar with the working of logs. The server's information is stored in the logs along with the information listed below:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Resource details"),(0,r.kt)("li",{parentName:"ol"},"Identification of the person who accessed the logs"),(0,r.kt)("li",{parentName:"ol"},"Date and time the logs were accessed"),(0,r.kt)("li",{parentName:"ol"},"Specifications on any problems that emerge"),(0,r.kt)("li",{parentName:"ol"},"Information about the final product")),(0,r.kt)("p",null,"Perform the following tasks on the dataset provided using PySpark:"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Status code analysis",(0,r.kt)("ol",{parentName:"li"},(0,r.kt)("li",{parentName:"ol"},"Read the log file as an RDD in PySpark"),(0,r.kt)("li",{parentName:"ol"},"Consider the sixth element as it is a \u201crequest type\u201d"),(0,r.kt)("li",{parentName:"ol"},'Replace the \u201csingle quote" with a blank'),(0,r.kt)("li",{parentName:"ol"},"Convert each word into a tuple of (word,1)"),(0,r.kt)("li",{parentName:"ol"},"Apply the \u201creduceByKey\u201c transformation to count the values"),(0,r.kt)("li",{parentName:"ol"},"Display the data"))),(0,r.kt)("li",{parentName:"ol"},"Arrange the result in descending order and display"),(0,r.kt)("li",{parentName:"ol"},"Identify the top 10 frequent visitors of the website"),(0,r.kt)("li",{parentName:"ol"},"Identify the top 10 missing (does not exist) URLs using these steps:",(0,r.kt)("ol",{parentName:"li"},(0,r.kt)("li",{parentName:"ol"},"Read the log file as an RDD in PySpark"),(0,r.kt)("li",{parentName:"ol"},"Identify the URLs for which the server is returning the 404-request code and display the data"))),(0,r.kt)("li",{parentName:"ol"},"Identify the traffic (total number of HTTP requests received per day)",(0,r.kt)("ol",{parentName:"li"},(0,r.kt)("li",{parentName:"ol"},"Read the log file as an RDD in PySpark"),(0,r.kt)("li",{parentName:"ol"},'Fetch the DateTime string and replace "[" with blank'),(0,r.kt)("li",{parentName:"ol"},"Get the date string from the DateTime"),(0,r.kt)("li",{parentName:"ol"},"Identify HTTP requests using the map function"))),(0,r.kt)("li",{parentName:"ol"},"Identify the top 10 endpoints that transfer maximum content in megabytes and display the data")))}d.isMDXComponent=!0}}]);