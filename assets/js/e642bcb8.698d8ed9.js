"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[41859],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>m});var r=a(67294);function n(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,r)}return a}function l(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){n(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,r,n=function(e,t){if(null==e)return{};var a,r,n={},i=Object.keys(e);for(r=0;r<i.length;r++)a=i[r],t.indexOf(a)>=0||(n[a]=e[a]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)a=i[r],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var d=r.createContext({}),s=function(e){var t=r.useContext(d),a=t;return e&&(a="function"==typeof e?e(t):l(l({},t),e)),a},c=function(e){var t=s(e.components);return r.createElement(d.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var a=e.components,n=e.mdxType,i=e.originalType,d=e.parentName,c=o(e,["components","mdxType","originalType","parentName"]),u=s(a),m=n,y=u["".concat(d,".").concat(m)]||u[m]||p[m]||i;return a?r.createElement(y,l(l({ref:t},c),{},{components:a})):r.createElement(y,l({ref:t},c))}));function m(e,t){var a=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=a.length,l=new Array(i);l[0]=u;var o={};for(var d in t)hasOwnProperty.call(t,d)&&(o[d]=t[d]);o.originalType=e,o.mdxType="string"==typeof e?e:n,l[1]=o;for(var s=2;s<i;s++)l[s]=a[s];return r.createElement.apply(null,l)}return r.createElement.apply(null,a)}u.displayName="MDXCreateElement"},50787:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>d,contentTitle:()=>l,default:()=>p,frontMatter:()=>i,metadata:()=>o,toc:()=>s});var r=a(87462),n=(a(67294),a(3905));const i={},l="Cars Data Modeling MySQL",o={unversionedId:"data-modeling/lab-cars-mysql-datamodel/datamodel-cars",id:"data-modeling/lab-cars-mysql-datamodel/datamodel-cars",title:"Cars Data Modeling MySQL",description:"ETL, data modeling and Data quality runs on cars and dealership dataset",source:"@site/docs/04-data-modeling/lab-cars-mysql-datamodel/datamodel-cars.md",sourceDirName:"04-data-modeling/lab-cars-mysql-datamodel",slug:"/data-modeling/lab-cars-mysql-datamodel/datamodel-cars",permalink:"/docs/data-modeling/lab-cars-mysql-datamodel/datamodel-cars",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"AirBnB Postgres Datamodel",permalink:"/docs/data-modeling/lab-airbnb-postgres-datamodel/"},next:{title:"Create a Data Model for a Digital Music Library",permalink:"/docs/data-modeling/lab-cassandra-digital-music-library/"}},d={},s=[{value:"Objective",id:"objective",level:2},{value:"Activity 1 - Dealership ETL",id:"activity-1---dealership-etl",level:2},{value:"Activity 2 - Billing and Data Quality",id:"activity-2---billing-and-data-quality",level:2}],c={toc:s};function p(e){let{components:t,...a}=e;return(0,n.kt)("wrapper",(0,r.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"cars-data-modeling-mysql"},"Cars Data Modeling MySQL"),(0,n.kt)("blockquote",null,(0,n.kt)("p",{parentName:"blockquote"},"ETL, data modeling and Data quality runs on cars and dealership dataset")),(0,n.kt)("h2",{id:"objective"},"Objective"),(0,n.kt)("p",null,"ETL, data modeling and Data quality runs on cars and dealership dataset"),(0,n.kt)("h2",{id:"activity-1---dealership-etl"},"Activity 1 - Dealership ETL"),(0,n.kt)("p",null,"In this activity, data from a car dealer stored in different file formats will be extracted, transformed and loaded into a MySQL database. Thereafter, basic analysis will be performed against the data in the MySQL database."),(0,n.kt)("h2",{id:"activity-2---billing-and-data-quality"},"Activity 2 - Billing and Data Quality"),(0,n.kt)("p",null,"In this activity, we will first create a Star schema for billing data and then ingest the data into Postgres database. We will then run data quality checks on the data."))}p.isMDXComponent=!0}}]);