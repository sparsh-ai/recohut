"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[78471],{3905:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>d});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var l=n.createContext({}),p=function(e){var t=n.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},u=function(e){var t=p(e.components);return n.createElement(l.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},h=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,o=e.originalType,l=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),h=p(a),d=r,m=h["".concat(l,".").concat(d)]||h[d]||c[d]||o;return a?n.createElement(m,i(i({ref:t},u),{},{components:a})):n.createElement(m,i({ref:t},u))}));function d(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=a.length,i=new Array(o);i[0]=h;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:r,i[1]=s;for(var p=2;p<o;p++)i[p]=a[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}h.displayName="MDXCreateElement"},97017:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>c,frontMatter:()=>o,metadata:()=>s,toc:()=>p});var n=a(87462),r=(a(67294),a(3905));const o={},i="Spark Execution Plan",s={unversionedId:"foundations/programming-languages/pyspark/execution-plan",id:"foundations/programming-languages/pyspark/execution-plan",title:"Spark Execution Plan",description:"Spark uses a query optimizer known as Catalyst to optimize the execution plan of Spark jobs. The execution plan is a representation of the physical execution of a query and it can be used to understand how Spark is processing data.",source:"@site/docs/01-foundations/04-programming-languages/pyspark/execution-plan.md",sourceDirName:"01-foundations/04-programming-languages/pyspark",slug:"/foundations/programming-languages/pyspark/execution-plan",permalink:"/docs/foundations/programming-languages/pyspark/execution-plan",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"PySpark DataFrame",permalink:"/docs/foundations/programming-languages/pyspark/dataframe"},next:{title:"Installing Spark",permalink:"/docs/foundations/programming-languages/pyspark/install"}},l={},p=[{value:"Tuning shuffle partitions",id:"tuning-shuffle-partitions",level:3},{value:"Identifying shuffles in a Spark query plan",id:"identifying-shuffles-in-a-spark-query-plan",level:3}],u={toc:p};function c(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},u,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"spark-execution-plan"},"Spark Execution Plan"),(0,r.kt)("p",null,"Spark uses a query optimizer known as Catalyst to optimize the execution plan of Spark jobs. The execution plan is a representation of the physical execution of a query and it can be used to understand how Spark is processing data."),(0,r.kt)("p",null,"The\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"explain()"),"\xa0the method can be used to view the execution plan of a query. The\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"explain()"),"\xa0method can be used on DataFrames and RDDs to view the physical execution plan of a query."),(0,r.kt)("p",null,"Here is an example of how to view the execution plan of a query:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-py"},'# View the execution plan of a query\ndf.filter(df["age"] > 30).explain()\n')),(0,r.kt)("p",null,"In this example, the\xa0",(0,r.kt)("inlineCode",{parentName:"p"},"explain()"),'\xa0the method is used to view the physical execution plan of a query that filters the DataFrame to include only rows where the "age" column is greater than 30. The output of the\xa0',(0,r.kt)("inlineCode",{parentName:"p"},"explain()"),"\xa0the method will show the physical execution plan of the query, which can be used to understand how Spark is processing data."),(0,r.kt)("p",null,"We can express the same query using any interface. The Spark SQL engine generates the same query plan used to optimize and execute on our Spark cluster."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214256593-38afbb18-1bc3-405d-916f-9981edb57522.png",alt:"query execution engine"})),(0,r.kt)("p",null,"Broadcasting in Spark can greatly improve the performance of Spark jobs by reducing the amount of data that needs to be sent over the network. Understanding the execution plan in Spark can also be helpful to understand how Spark is processing data and to optimize the performance of Spark jobs."),(0,r.kt)("p",null,"Whenever we execute transformations, Spark prepares a plan, and as soon as an action is called, it performs those transformations. Now, it's time to expand that knowledge. Let's dive deeper into Spark's query execution mechanism."),(0,r.kt)("p",null,"Every time a query is executed by Spark, it is done with the help of the following four plans:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Parsed Logical Plan"),": Spark\xa0prepares a\xa0",(0,r.kt)("em",{parentName:"li"},"Parsed Logical Plan"),", where it checks the metadata (table name, column names, and more) to confirm whether the respective entities exist or not."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Analyzed Logical Plan"),": Spark accepts the Parsed Logical Plan and converts it into what is called the\xa0",(0,r.kt)("em",{parentName:"li"},"Analyzed Logical Plan"),". This is\xa0then sent to Spark's catalyst optimizer, which is an advanced query optimizer for Spark."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Optimized Logical Plan"),": The catalyst optimizer applies further optimizations and comes up with the final logical plan, called\xa0the\xa0",(0,r.kt)("em",{parentName:"li"},"Optimized Logical Plan"),"."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Physical Plan"),": The\xa0",(0,r.kt)("em",{parentName:"li"},"Physical Plan"),"\xa0specifies\xa0how the Optimized Logical Plan is going to be executed on the cluster.")),(0,r.kt)("p",null,"Apart from the catalyst optimizer, there\xa0is another framework in Spark called the\xa0",(0,r.kt)("strong",{parentName:"p"},"cost-based optimizer"),"\xa0(",(0,r.kt)("strong",{parentName:"p"},"CBO"),"). The CBO collects statistics on data, such as the number of distinct values, row counts, null values, and more, to help Spark come up with a better Physical Plan. AQE is another optimization technique that speeds up query execution based on runtime statistics. It does this with the help of the following three features:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Dynamically coalescing shuffle partitions")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Dynamically switching join strategies")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"Dynamically optimizing skew joins"))),(0,r.kt)("p",null,"To write efficient Spark applications, we need to have some understanding of how Spark executes queries. Having a good understanding of how Spark executes a given query helps big data developers/engineers work efficiently with large volumes of data."),(0,r.kt)("p",null,"Query execution is a very broad subject, and, in this section, we will understand jobs, stages, and tasks. We will also learn how Spark lazy evaluation works, how to check and understand the execution plan when working with DataFrames or SparkSQL, how joins work in Spark and the different types of join algorithms Spark uses while joining two tables. We will also learn about the input, output, and shuffle partitions and the storage benefits of using different file formats."),(0,r.kt)("p",null,"Knowing about the internals will help you troubleshoot and debug your Spark applications more efficiently. By the end of this section, you will know how to execute Spark queries, as well as how to write and debug your Spark applications more efficiently."),(0,r.kt)("h3",{id:"tuning-shuffle-partitions"},"Tuning shuffle partitions"),(0,r.kt)("p",null,"Spark uses a\xa0technique called\xa0",(0,r.kt)("strong",{parentName:"p"},"shuffle"),"\xa0to move data between its executors or nodes while performing operations such as\xa0",(0,r.kt)("strong",{parentName:"p"},"join"),",\xa0",(0,r.kt)("strong",{parentName:"p"},"union"),",\xa0",(0,r.kt)("strong",{parentName:"p"},"groupby"),", and\xa0",(0,r.kt)("strong",{parentName:"p"},"reduceby"),". The shuffle\xa0operation is very expensive as it involves the movement of data between nodes. Hence, it is usually preferable to reduce the amount of shuffle involved in a Spark query. The number of partition splits that Spark performs while shuffling data is determined by the following configuration:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},'spark.conf.set("spark.sql.shuffle.partitions",200)\n')),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"200"),"\xa0is the default value and you can tune it to a number that suits your query the best. If you have too much data and too few partitions, this might result in longer tasks. But, on the other hand, if you have too little data and too many shuffle partitions, the overhead of shuffle tasks will degrade performance. So, you will have to run your query multiple times with different shuffle partition numbers to arrive at an optimum number."),(0,r.kt)("p",null,"You can learn\xa0more about Spark performance tuning and shuffle partitions here:\xa0",(0,r.kt)("a",{parentName:"p",href:"https://spark.apache.org/docs/latest/sql-performance-tuning.html"},"https://spark.apache.org/docs/latest/sql-performance-tuning.html"),"."),(0,r.kt)("h3",{id:"identifying-shuffles-in-a-spark-query-plan"},"Identifying shuffles in a Spark query plan"),(0,r.kt)("p",null,"Similar to SQL, we\xa0can use the\xa0",(0,r.kt)("strong",{parentName:"p"},"EXPLAIN"),"\xa0command to\xa0print the plans in Spark. Here is a simple example to generate two sets of numbers, partition them, and then join them. This will cause lot of data movement:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"val jump2Numbers = spark.range(0, 100000,2)\nval jump5Numbers = spark.range(0, 200000, 5)\nval ds1 = jump2Numbers.repartition(3)\nval ds2 = jump5Numbers.repartition(5)\nval joined = ds1.join(ds2)\njoined.explain\n")),(0,r.kt)("p",null,"The\xa0",(0,r.kt)("strong",{parentName:"p"},"joined.explain"),"\xa0request\xa0will print a plan similar to the\xa0sample shown as follows:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"== Physical Plan ==\nBroadcastNestedLoopJoin BuildRight, Inner\n:-\xa0**Exchange**\xa0RoundRobinPartitioning(3), [id=#216]\n:\xa0\xa0+- *(1) Range (0, 100000, step=2, splits=4)\n+- BroadcastExchange IdentityBroadcastMode, [id=#219]\n\xa0\xa0\xa0+-\xa0**Exchange**\xa0RoundRobinPartitioning(5), [id=#218]\n\xa0\xa0\xa0\xa0\xa0\xa0+- *(2) Range (0, 200000, step=5, splits=4)\n")),(0,r.kt)("p",null,"Just search for the\xa0",(0,r.kt)("strong",{parentName:"p"},"Exchange"),"\xa0keyword to identify the shuffle stages."),(0,r.kt)("p",null,"Alternatively, you can identify the shuffle stage from the Spark DAG. In the DAG, look for sections named\xa0",(0,r.kt)("strong",{parentName:"p"},"Exchange"),". These are the shuffle sections. Here is an example Spark DAG containing two\xa0",(0,r.kt)("strong",{parentName:"p"},"Exchange"),"\xa0stages:"),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/218312617-1624668d-96d7-449d-87ea-60edf79edf2d.jpeg",alt:"B17525_14_013"})),(0,r.kt)("p",null,"If there\xa0are very expensive shuffle sections, consider\xa0enabling the statistics and checking whether the engine generates a better plan. If not, you will have to rewrite the query to reduce the shuffles as much as possible."))}c.isMDXComponent=!0}}]);