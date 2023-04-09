"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[33310],{3905:(e,t,r)=>{r.d(t,{Zo:()=>p,kt:()=>f});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function c(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var i=n.createContext({}),s=function(e){var t=n.useContext(i),r=t;return e&&(r="function"==typeof e?e(t):c(c({},t),e)),r},p=function(e){var t=s(e.components);return n.createElement(i.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,i=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),u=s(r),f=a,b=u["".concat(i,".").concat(f)]||u[f]||d[f]||o;return r?n.createElement(b,c(c({ref:t},p),{},{components:r})):n.createElement(b,c({ref:t},p))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,c=new Array(o);c[0]=u;var l={};for(var i in t)hasOwnProperty.call(t,i)&&(l[i]=t[i]);l.originalType=e,l.mdxType="string"==typeof e?e:a,c[1]=l;for(var s=2;s<o;s++)c[s]=r[s];return n.createElement.apply(null,c)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},32710:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>i,contentTitle:()=>c,default:()=>d,frontMatter:()=>o,metadata:()=>l,toc:()=>s});var n=r(87462),a=(r(67294),r(3905));const o={},c="Snowflake dbt cloud TPCH",l={unversionedId:"processing/lab-dbt-tpch/README",id:"processing/lab-dbt-tpch/README",title:"Snowflake dbt cloud TPCH",description:"Accelerating Data Teams with Snowflake and dbt Cloud Hands On Lab",source:"@site/docs/03-processing/lab-dbt-tpch/README.md",sourceDirName:"03-processing/lab-dbt-tpch",slug:"/processing/lab-dbt-tpch/",permalink:"/docs/processing/lab-dbt-tpch/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"dbt Redshift TICKIT",permalink:"/docs/processing/lab-dbt-tickit/"},next:{title:"EMR Serverless",permalink:"/docs/processing/lab-emr-serverless/"}},i={},s=[],p={toc:s};function d(e){let{components:t,...r}=e;return(0,a.kt)("wrapper",(0,n.Z)({},p,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"snowflake-dbt-cloud-tpch"},"Snowflake dbt cloud TPCH"),(0,a.kt)("blockquote",null,(0,a.kt)("p",{parentName:"blockquote"},"Accelerating Data Teams with Snowflake and dbt Cloud Hands On Lab")),(0,a.kt)("p",null,"In this lab we'll be transforming raw retail data into a consumable orders model that's ready for visualization. We'll be utilizing the TPC-H dataset that comes out of the box with your Snowflake account and transform it using some of dbt's most powerful features. By the time we're done you'll have a fully functional dbt project with testing and documentation, dedicated development and production environments, and experience with the dbt git workflow."),(0,a.kt)("p",null,(0,a.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214353071-f6a011dd-db9f-42f9-b04d-f48883956c15.png",alt:"dbtcloud"})),(0,a.kt)("p",null,(0,a.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214353091-0fbf7972-1e89-43f0-9b8d-d73cfac82d3e.png",alt:"dbtconnect"})),(0,a.kt)("p",null,(0,a.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214353101-a381a803-67f7-42fd-a47e-8f8eee3db637.png",alt:"flow"})))}d.isMDXComponent=!0}}]);