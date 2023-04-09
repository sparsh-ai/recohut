"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[15691],{3905:(e,a,r)=>{r.d(a,{Zo:()=>l,kt:()=>m});var t=r(67294);function n(e,a,r){return a in e?Object.defineProperty(e,a,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[a]=r,e}function o(e,a){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);a&&(t=t.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),r.push.apply(r,t)}return r}function i(e){for(var a=1;a<arguments.length;a++){var r=null!=arguments[a]?arguments[a]:{};a%2?o(Object(r),!0).forEach((function(a){n(e,a,r[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(r,a))}))}return e}function s(e,a){if(null==e)return{};var r,t,n=function(e,a){if(null==e)return{};var r,t,n={},o=Object.keys(e);for(t=0;t<o.length;t++)r=o[t],a.indexOf(r)>=0||(n[r]=e[r]);return n}(e,a);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(t=0;t<o.length;t++)r=o[t],a.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var p=t.createContext({}),c=function(e){var a=t.useContext(p),r=a;return e&&(r="function"==typeof e?e(a):i(i({},a),e)),r},l=function(e){var a=c(e.components);return t.createElement(p.Provider,{value:a},e.children)},u={inlineCode:"code",wrapper:function(e){var a=e.children;return t.createElement(t.Fragment,{},a)}},d=t.forwardRef((function(e,a){var r=e.components,n=e.mdxType,o=e.originalType,p=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),d=c(r),m=n,f=d["".concat(p,".").concat(m)]||d[m]||u[m]||o;return r?t.createElement(f,i(i({ref:a},l),{},{components:r})):t.createElement(f,i({ref:a},l))}));function m(e,a){var r=arguments,n=a&&a.mdxType;if("string"==typeof e||n){var o=r.length,i=new Array(o);i[0]=d;var s={};for(var p in a)hasOwnProperty.call(a,p)&&(s[p]=a[p]);s.originalType=e,s.mdxType="string"==typeof e?e:n,i[1]=s;for(var c=2;c<o;c++)i[c]=r[c];return t.createElement.apply(null,i)}return t.createElement.apply(null,r)}d.displayName="MDXCreateElement"},65774:(e,a,r)=>{r.r(a),r.d(a,{assets:()=>p,contentTitle:()=>i,default:()=>u,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var t=r(87462),n=(r(67294),r(3905));const o={},i="PySpark DataFrame",s={unversionedId:"foundations/programming-languages/pyspark/dataframe",id:"foundations/programming-languages/pyspark/dataframe",title:"PySpark DataFrame",description:"Creating a DataFrame in PySpark",source:"@site/docs/01-foundations/04-programming-languages/pyspark/dataframe.md",sourceDirName:"01-foundations/04-programming-languages/pyspark",slug:"/foundations/programming-languages/pyspark/dataframe",permalink:"/docs/foundations/programming-languages/pyspark/dataframe",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"cheat-sheet",permalink:"/docs/foundations/programming-languages/pyspark/cheat-sheet"},next:{title:"Spark Execution Plan",permalink:"/docs/foundations/programming-languages/pyspark/execution-plan"}},p={},c=[{value:"Creating a DataFrame in PySpark",id:"creating-a-dataframe-in-pyspark",level:2}],l={toc:c};function u(e){let{components:a,...r}=e;return(0,n.kt)("wrapper",(0,t.Z)({},l,r,{components:a,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"pyspark-dataframe"},"PySpark DataFrame"),(0,n.kt)("h2",{id:"creating-a-dataframe-in-pyspark"},"Creating a DataFrame in PySpark"),(0,n.kt)("p",null,"The DataFrames are a fundamental data structure in PySpark, and they provide a powerful and flexible way to work with structured and semi-structured data. A DataFrame is a distributed collection of data organized into named columns. It is similar to a table in a relational database or a data frame in R/Python. DataFrames are built on top of RDDs and provide a higher-level abstraction for data processing. They also support a more powerful query optimizer, known as the Catalyst Optimizer, which can greatly improve the performance of Spark queries."),(0,n.kt)("p",null,"DataFrames can be created from a variety of data sources, including structured data files, Hive tables, external databases, and streaming data sources. The following code snippet shows how to create a DataFrame from a CSV file:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-py"},'df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)\n')),(0,n.kt)("p",null,"Once a DataFrame has been created, it can be transformed and processed using the same functions as an RDD, as well as additional functions specific to DataFrames."))}u.isMDXComponent=!0}}]);