"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[76545],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>m});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var p=n.createContext({}),l=function(e){var t=n.useContext(p),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},c=function(e){var t=l(e.components);return n.createElement(p.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,p=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),d=l(a),m=r,g=d["".concat(p,".").concat(m)]||d[m]||u[m]||i;return a?n.createElement(g,o(o({ref:t},c),{},{components:a})):n.createElement(g,o({ref:t},c))}));function m(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,o=new Array(i);o[0]=d;var s={};for(var p in t)hasOwnProperty.call(t,p)&&(s[p]=t[p]);s.originalType=e,s.mdxType="string"==typeof e?e:r,o[1]=s;for(var l=2;l<i;l++)o[l]=a[l];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}d.displayName="MDXCreateElement"},86749:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>p,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>s,toc:()=>l});var n=a(87462),r=(a(67294),a(3905));const i={},o="Spark Optimizations for Analytics Workloads",s={unversionedId:"foundations/programming-languages/pyspark/lab-spark-optimizations/README",id:"foundations/programming-languages/pyspark/lab-spark-optimizations/README",title:"Spark Optimizations for Analytics Workloads",description:"Optimizations\xa0in\xa0Apache\xa0Spark\xa0play a crucial role while building big data solutions. Knowledge and experience in tuning Spark-based workloads help organizations save costs and time while running these workloads on the cloud. In this lab, we will learn about various optimization techniques concerning\xa0Spark\xa0DataFrames\xa0and\xa0big data analytics\xa0in general. We will learn about the limitations of the\xa0collect()\xa0method and\xa0inferSchema\xa0when reading data. This will be followed by an overview of the best practices for working with\xa0CSV\xa0files,\xa0Parquet\xa0files,\xa0Pandas\xa0projects, and\xa0Koalas\xa0projects. Also, we will learn about some powerful optimization techniques, such as\xa0column predicate pushdown,\xa0column pruning, and\xa0partitioning strategies.",source:"@site/docs/01-foundations/04-programming-languages/pyspark/lab-spark-optimizations/README.md",sourceDirName:"01-foundations/04-programming-languages/pyspark/lab-spark-optimizations",slug:"/foundations/programming-languages/pyspark/lab-spark-optimizations/",permalink:"/docs/foundations/programming-languages/pyspark/lab-spark-optimizations/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Pyspark NYC Taxi",permalink:"/docs/foundations/programming-languages/pyspark/lab-pyspark-nyctaxi/"},next:{title:"Spark Optimizations",permalink:"/docs/foundations/programming-languages/pyspark/lab-spark-optimizations-2/"}},p={},l=[],c={toc:l};function u(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"spark-optimizations-for-analytics-workloads"},"Spark Optimizations for Analytics Workloads"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Optimizations"),"\xa0in\xa0",(0,r.kt)("strong",{parentName:"p"},"Apache"),"\xa0",(0,r.kt)("strong",{parentName:"p"},"Spark"),"\xa0play a crucial role while building big data solutions. Knowledge and experience in tuning Spark-based workloads help organizations save costs and time while running these workloads on the cloud. In this lab, we will learn about various optimization techniques concerning\xa0",(0,r.kt)("strong",{parentName:"p"},"Spark"),"\xa0",(0,r.kt)("strong",{parentName:"p"},"DataFrames"),"\xa0and\xa0",(0,r.kt)("strong",{parentName:"p"},"big data analytics"),"\xa0in general. We will learn about the limitations of the\xa0",(0,r.kt)("strong",{parentName:"p"},"collect()"),"\xa0method and\xa0",(0,r.kt)("strong",{parentName:"p"},"inferSchema"),"\xa0when reading data. This will be followed by an overview of the best practices for working with\xa0",(0,r.kt)("strong",{parentName:"p"},"CSV"),"\xa0files,\xa0",(0,r.kt)("strong",{parentName:"p"},"Parquet"),"\xa0files,\xa0",(0,r.kt)("strong",{parentName:"p"},"Pandas"),"\xa0projects, and\xa0",(0,r.kt)("strong",{parentName:"p"},"Koalas"),"\xa0projects. Also, we will learn about some powerful optimization techniques, such as\xa0",(0,r.kt)("strong",{parentName:"p"},"column predicate pushdown"),",\xa0",(0,r.kt)("strong",{parentName:"p"},"column pruning"),", and\xa0",(0,r.kt)("strong",{parentName:"p"},"partitioning strategies"),"."),(0,r.kt)("p",null,"The topics covered in this lab are as follows:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Understanding the\xa0",(0,r.kt)("strong",{parentName:"li"},"collect()"),"\xa0method"),(0,r.kt)("li",{parentName:"ul"},"Understanding the use of\xa0",(0,r.kt)("strong",{parentName:"li"},"inferSchema")),(0,r.kt)("li",{parentName:"ul"},"Learning to differentiate between CSV and Parquet"),(0,r.kt)("li",{parentName:"ul"},"Learning to differentiate between pandas and Koalas"),(0,r.kt)("li",{parentName:"ul"},"Understanding built-in Spark functions"),(0,r.kt)("li",{parentName:"ul"},"Learning column predicate pushdown"),(0,r.kt)("li",{parentName:"ul"},"Learning partitioning strategies in Spark"),(0,r.kt)("li",{parentName:"ul"},"Understanding Spark SQL optimizations"),(0,r.kt)("li",{parentName:"ul"},"Understanding bucketing in Spark")),(0,r.kt)("p",null,"The code is in the assets folder. You will also find a ",(0,r.kt)("inlineCode",{parentName:"p"},".dbc")," file that can be imported directly into databricks."))}u.isMDXComponent=!0}}]);