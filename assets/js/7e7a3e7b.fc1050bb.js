"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[50283],{3905:(t,e,a)=>{a.d(e,{Zo:()=>u,kt:()=>m});var n=a(67294);function r(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function o(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function i(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?o(Object(a),!0).forEach((function(e){r(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function s(t,e){if(null==t)return{};var a,n,r=function(t,e){if(null==t)return{};var a,n,r={},o=Object.keys(t);for(n=0;n<o.length;n++)a=o[n],e.indexOf(a)>=0||(r[a]=t[a]);return r}(t,e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(t);for(n=0;n<o.length;n++)a=o[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(r[a]=t[a])}return r}var d=n.createContext({}),l=function(t){var e=n.useContext(d),a=e;return t&&(a="function"==typeof t?t(e):i(i({},e),t)),a},u=function(t){var e=l(t.components);return n.createElement(d.Provider,{value:e},t.children)},p={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},c=n.forwardRef((function(t,e){var a=t.components,r=t.mdxType,o=t.originalType,d=t.parentName,u=s(t,["components","mdxType","originalType","parentName"]),c=l(a),m=r,g=c["".concat(d,".").concat(m)]||c[m]||p[m]||o;return a?n.createElement(g,i(i({ref:e},u),{},{components:a})):n.createElement(g,i({ref:e},u))}));function m(t,e){var a=arguments,r=e&&e.mdxType;if("string"==typeof t||r){var o=a.length,i=new Array(o);i[0]=c;var s={};for(var d in e)hasOwnProperty.call(e,d)&&(s[d]=e[d]);s.originalType=t,s.mdxType="string"==typeof t?t:r,i[1]=s;for(var l=2;l<o;l++)i[l]=a[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}c.displayName="MDXCreateElement"},43865:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>d,contentTitle:()=>i,default:()=>p,frontMatter:()=>o,metadata:()=>s,toc:()=>l});var n=a(87462),r=(a(67294),a(3905));const o={},i="Data Storages",s={unversionedId:"foundations/data-engineering-foundations/data-storages",id:"foundations/data-engineering-foundations/data-storages",title:"Data Storages",description:"| Architecture          | Total cost of solution                                                                                                                                                  | Flexibility of scenarios                                                                                                                                                                      | Complexity of development                                                                                                                                                     | Maturity of ecosystem                                                                                                                                                                         | Organizational maturity required                                                                                                                                                            |",source:"@site/docs/01-foundations/02-data-engineering-foundations/data-storages.md",sourceDirName:"01-foundations/02-data-engineering-foundations",slug:"/foundations/data-engineering-foundations/data-storages",permalink:"/docs/foundations/data-engineering-foundations/data-storages",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Data Quality",permalink:"/docs/foundations/data-engineering-foundations/data-quality"},next:{title:"Basics",permalink:"/docs/foundations/data-engineering-foundations/de-basics"}},d={},l=[],u={toc:l};function p(t){let{components:e,...a}=t;return(0,r.kt)("wrapper",(0,n.Z)({},u,a,{components:e,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"data-storages"},"Data Storages"),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"th"},"Architecture")),(0,r.kt)("th",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"th"},"Total cost of solution")),(0,r.kt)("th",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"th"},"Flexibility of scenarios")),(0,r.kt)("th",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"th"},"Complexity of development")),(0,r.kt)("th",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"th"},"Maturity of ecosystem")),(0,r.kt)("th",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"th"},"Organizational maturity required")))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Cloud data warehouse")),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"High"),"\xa0- given cloud data warehouses rely on proprietary data formats and offer an end to end solution together, the cost is high"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Low"),"\xa0- Cloud data warehouses are optimized for BI/SQL based scenarios, there is some support for data science/exploratory scenarios which is restrictive due to format constraints"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Low"),"\xa0- there is less moving parts and you can get started almost immediately with an end to end solution"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"High"),"\xa0- for SQL/BI scenarios, Low - for other scenarios"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Low"),"\xa0- the tools and ecosystem are largely well understood and ready to be consumed by organizations of any shape/size.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Modern data warehouse")),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium"),"\xa0- the data preparation and historical data can be moved to the data lake at lower cost, still need a cloud warehouse which is expensive"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium"),"\xa0- diverse ecosystem of tools nad more exploratory scenarios supported in the data lake, correlating data in the warehouse and data lake needs data copies"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium"),"\xa0- the data engineering team needs to ensure that the data lake design is efficient and scalable, plenty of guidance and considerations available, including this book"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium"),"\xa0- the data preparation and data engineering ecosystem, such as Spark/Hadoop has a higher maturity, tuning for performance and scale needed, High - for consumption via data warehouse"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium"),"\xa0- the data platform team needs to be skilled up to understand the needs of the organization and make the right design choices at the least to support the needs of the organization")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Data lakehouse")),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Low"),"\xa0- the data lake storage acts as the unified repository with no data movement required, compute engines are largely stateless and can be spun up and down on demand"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"High"),"\xa0- flexibility of running more scenarios with a diverse ecosystem enabling more exploratory analysis such as data science, and ease of sharing of data between BI and data science teams"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium to High"),"\xa0- careful choice of right datasets and the open data format needed to support the lakehouse architecture"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium to High"),"\xa0- while technologies such as Delta Lake, Apache Iceberg, and Apache Hudi are gaining maturity and adoption, today, this architecture requires thoughtful design"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium to High"),"\xa0- the data platform team needs to be skilled up to understand the needs of the organization and the technology choices that are still new")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Data mesh")),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Medium"),"\xa0- while the distributed design ensures cost is lower, lot of investment required in automation/blueprint/data governance solutions"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"High"),"\xa0- flexibility in supporting different architectures and solutions in the same organization, and no bottlenecks on a central lean organization"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"High"),"\xa0- this relies on an end to end automated solution and an architecture that scales to 10x growth and sharing across architectures/cloud solutions"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"Low"),"\xa0- relatively nascent in guidance and available toolsets"),(0,r.kt)("td",{parentName:"tr",align:null},(0,r.kt)("strong",{parentName:"td"},"High"),"\xa0- data platform team and product/domain teams need to be skilled up in data lakes.")))),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Cost versus complexity of cloud data lake architectures")),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/213930648-3e63ea81-b214-411a-9e4a-39a403ed35df.png",alt:null})))}p.isMDXComponent=!0}}]);