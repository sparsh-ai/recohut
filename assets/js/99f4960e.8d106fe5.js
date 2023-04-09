"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[83706],{3905:(e,t,a)=>{a.d(t,{Zo:()=>l,kt:()=>f});var n=a(67294);function o(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){o(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,o=function(e,t){if(null==e)return{};var a,n,o={},r=Object.keys(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||(o[a]=e[a]);return o}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(o[a]=e[a])}return o}var u=n.createContext({}),d=function(e){var t=n.useContext(u),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},l=function(e){var t=d(e.components);return n.createElement(u.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},p=n.forwardRef((function(e,t){var a=e.components,o=e.mdxType,r=e.originalType,u=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),p=d(a),f=o,m=p["".concat(u,".").concat(f)]||p[f]||c[f]||r;return a?n.createElement(m,i(i({ref:t},l),{},{components:a})):n.createElement(m,i({ref:t},l))}));function f(e,t){var a=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var r=a.length,i=new Array(r);i[0]=p;var s={};for(var u in t)hasOwnProperty.call(t,u)&&(s[u]=t[u]);s.originalType=e,s.mdxType="string"==typeof e?e:o,i[1]=s;for(var d=2;d<r;d++)i[d]=a[d];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}p.displayName="MDXCreateElement"},32911:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>u,contentTitle:()=>i,default:()=>f,frontMatter:()=>r,metadata:()=>s,toc:()=>d});var n=a(87462),o=(a(67294),a(3905));const r={},i="Data Quality",s={unversionedId:"foundations/data-engineering-foundations/data-quality",id:"foundations/data-engineering-foundations/data-quality",title:"Data Quality",description:"Do your product dashboards look funky? Are your quarterly reports stale? Is the data set you're using broken or just plain wrong? Have you ever been about to sign off after a long day running queries or building data pipelines only to get pinged by your head of marketing that \u201cthe data is missing\u201d from a critical report? What about a frantic email from your CTO about \u201cduplicate data\u201d in a business intelligence dashboard? Or a memo from your CEO, the same one who is so bullish on data, about a confusing or inaccurate number in his latest board deck? If any of these situations hit home for you, you\u2019re not alone. These problems affect almost every team, yet they're usually addressed on an ad hoc basis and in a reactive manner.",source:"@site/docs/01-foundations/02-data-engineering-foundations/data-quality.md",sourceDirName:"01-foundations/02-data-engineering-foundations",slug:"/foundations/data-engineering-foundations/data-quality",permalink:"/docs/foundations/data-engineering-foundations/data-quality",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Data Pipelines",permalink:"/docs/foundations/data-engineering-foundations/data-pipelines"},next:{title:"Data Storages",permalink:"/docs/foundations/data-engineering-foundations/data-storages"}},u={},d=[],l=(c="YouTube",function(e){return console.warn("Component "+c+" was not imported, exported, or provided by MDXProvider as global scope"),(0,o.kt)("div",e)});var c;const p={toc:d};function f(e){let{components:t,...a}=e;return(0,o.kt)("wrapper",(0,n.Z)({},p,a,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"data-quality"},"Data Quality"),(0,o.kt)("p",null,"Do your product dashboards look funky? Are your quarterly reports stale? Is the data set you're using broken or just plain wrong? Have you ever been about to sign off after a long day running queries or building data pipelines only to get pinged by your head of marketing that \u201cthe data is missing\u201d from a critical report? What about a frantic email from your CTO about \u201cduplicate data\u201d in a business intelligence dashboard? Or a memo from your CEO, the same one who is so bullish on data, about a confusing or inaccurate number in his latest board deck? If any of these situations hit home for you, you\u2019re not alone. These problems affect almost every team, yet they're usually addressed on an ad hoc basis and in a reactive manner. "),(0,o.kt)("p",null,"This problem, often referred to as \u201cdata downtime,\u201d happens to even the most innovative and data-first companies, and, in our opinion, it\u2019s one of the biggest challenges facing businesses in the 21st century. Data downtime refers to periods of time where data is missing, inaccurate, or otherwise erroneous, and it manifests in stale dashboards, inaccurate reports, and even poor decision making. The root of data downtime? Unreliable data, and lots of it. Data downtime can cost companies upwards of millions of dollars per year, not to mention customer trust. In fact, ZoomInfo found in 2019 that one in five companies lost a customer due to a data quality issue. As you\u2019re likely aware, your company\u2019s bottom line isn\u2019t the only thing that\u2019s suffering from data downtime. Handling data quality issues consumes upwards of 40% of your data team\u2019s time that could otherwise be spent working on more interesting projects or actually innovating for the business."),(0,o.kt)(l,{vid:"5ZPCEzLpS38",title:"Quality considerations",mdxType:"YouTube"}),(0,o.kt)("p",null,"Many data engineering teams today face the \"good pipelines, bad data\" problem. It doesn't matter how advanced your data infrastructure is if the data you're piping is bad. We will learn how to tackle data quality and trust at scale by leveraging best practices and technologies used by some of the world's most innovative companies."),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Build more trustworthy and reliable data pipelines"),(0,o.kt)("li",{parentName:"ul"},"Write scripts to make data checks and identify broken pipelines with data observability"),(0,o.kt)("li",{parentName:"ul"},"Learn how to set and maintain data SLAs, SLIs, and SLOs"),(0,o.kt)("li",{parentName:"ul"},"Develop and lead data quality initiatives at your company"),(0,o.kt)("li",{parentName:"ul"},"Learn how to treat data services and systems with the diligence of production software"),(0,o.kt)("li",{parentName:"ul"},"Automate data lineage graphs across your data ecosystem"),(0,o.kt)("li",{parentName:"ul"},"Build anomaly detectors for your critical data assets")))}f.isMDXComponent=!0}}]);