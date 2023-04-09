"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[89451],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>f});var r=n(67294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var l=r.createContext({}),p=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},c=function(e){var t=p(e.components);return r.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),d=p(n),f=a,m=d["".concat(l,".").concat(f)]||d[f]||u[f]||o;return n?r.createElement(m,i(i({ref:t},c),{},{components:n})):r.createElement(m,i({ref:t},c))}));function f(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=d;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var p=2;p<o;p++)i[p]=n[p];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},12147:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>u,frontMatter:()=>o,metadata:()=>s,toc:()=>p});var r=n(87462),a=(n(67294),n(3905));const o={},i="Snowpark",s={unversionedId:"processing/snowpark",id:"processing/snowpark",title:"Snowpark",description:"What is Snowpark",source:"@site/docs/03-processing/snowpark.md",sourceDirName:"03-processing",slug:"/processing/snowpark",permalink:"/docs/processing/snowpark",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Ray",permalink:"/docs/processing/ray"},next:{title:"3NF/ Relational Modeling",permalink:"/docs/data-modeling/3nf-data-modeling"}},l={},p=[{value:"What is Snowpark",id:"what-is-snowpark",level:3},{value:"Theory",id:"theory",level:3}],c={toc:p};function u(e){let{components:t,...n}=e;return(0,a.kt)("wrapper",(0,r.Z)({},c,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"snowpark"},"Snowpark"),(0,a.kt)("h3",{id:"what-is-snowpark"},"What is Snowpark"),(0,a.kt)("p",null,"Snowpark at its core provides an API that developers can use to construct DataFrames that are executed lazily on Snowflake's platform. It enables data engineers, data scientists, and developers coding in languages other than SQL such as Python to take advantage of Snowflake's powerful platform without having to first move data out of Snowflake. This enables data application developers to run complex transformations within Snowflake while taking advantage of the built-in unlimited scalability, performance, governance and security features."),(0,a.kt)("p",null,"Use Python, Java or Scala with familiar DataFrame and custom function support to build powerful and efficient pipelines, machine learning (ML) workflows, and data applications. And gain the performance, ease of use, governance, and security while working inside Snowflake\u2019s Data Cloud."),(0,a.kt)("h3",{id:"theory"},"Theory"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"DBT generates a wrapper around the python model code that returns a Snowpark data frame."),(0,a.kt)("li",{parentName:"ul"},"The model code gets executed using Stored Procedures, that can be configured as Anonymous or Permanent."),(0,a.kt)("li",{parentName:"ul"},"Anaconda packages and other third-party packages can be specified in PACKAGES and IMPORTS respectively.")))}u.isMDXComponent=!0}}]);