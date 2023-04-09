"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[47228],{3905:(e,t,n)=>{n.d(t,{Zo:()=>c,kt:()=>m});var a=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var s=a.createContext({}),p=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},c=function(e){var t=p(e.components);return a.createElement(s.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),d=p(n),m=r,f=d["".concat(s,".").concat(m)]||d[m]||u[m]||o;return n?a.createElement(f,i(i({ref:t},c),{},{components:n})):a.createElement(f,i({ref:t},c))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=d;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:r,i[1]=l;for(var p=2;p<o;p++)i[p]=n[p];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},72553:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>u,frontMatter:()=>o,metadata:()=>l,toc:()=>p});var a=n(87462),r=(n(67294),n(3905));const o={},i="OLX Data Engineering Challenge",l={unversionedId:"assignments/olx-python/README",id:"assignments/olx-python/README",title:"OLX Data Engineering Challenge",description:"Tasks",source:"@site/docs/11-assignments/olx-python/README.md",sourceDirName:"11-assignments/olx-python",slug:"/assignments/olx-python/",permalink:"/docs/assignments/olx-python/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Reading data from MySQL in CSV and saving into S3",permalink:"/docs/assignments/mysql-s3-incremental/"},next:{title:"Batch and Stream Unified analytics for Sakila Music Company",permalink:"/docs/assignments/sakila/"}},s={},p=[{value:"Tasks",id:"tasks",level:2},{value:"What do we expect from you?",id:"what-do-we-expect-from-you",level:2},{value:"Workflow",id:"workflow",level:2},{value:"Airflow Pipeline",id:"airflow-pipeline",level:2}],c={toc:p};function u(e){let{components:t,...o}=e;return(0,r.kt)("wrapper",(0,a.Z)({},c,o,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"olx-data-engineering-challenge"},"OLX Data Engineering Challenge"),(0,r.kt)("h2",{id:"tasks"},"Tasks"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"Filter only Portuguese cities"),(0,r.kt)("li",{parentName:"ol"},"Add a new column with corresponding ",(0,r.kt)("a",{parentName:"li",href:"https://en.wikipedia.org/wiki/Geohash"},"GeoHash")," codes using the set of longitude and latitude coordinates."),(0,r.kt)("li",{parentName:"ol"},"Write out the final dataset into AWS S3 Bucket.")),(0,r.kt)("p",null,"The solution must be coded in Python and you can use any public domain libraries. It should work with any file respecting the same schema as the one provided."),(0,r.kt)("p",null,"You should provide the data on AWS S3 with the structure of the example, ie:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-json"},'[{\n"city": "Lisbon",\n"lat": 38.708,\n"lng": -9.139,\n"population": 506654, "geohash": "eycs0n94my5w"},\n{"city": "Sintra",\n"lat": 38.7974,\n"lng": -9.3904, "population": 377835, "geohash": "eyckdqf55zd3"},\n{"city": "Vila Nova de Gaia", "lat": 41.1333,\n"lng": -8.6167, "population": 302295, "geohash": "ez3f5bjdb6fu"},\n{"city": "Porto",\n"lat": 41.1495,\n"lng": -8.6108, "population": 237591, "geohash": "ez3fh51c1yf0"\n}]\n')),(0,r.kt)("h2",{id:"what-do-we-expect-from-you"},"What do we expect from you?"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Proper documentation"),(0,r.kt)("li",{parentName:"ul"},"Setup/Launch instructions if required"),(0,r.kt)("li",{parentName:"ul"},"Good software design"),(0,r.kt)("li",{parentName:"ul"},"Proper use of data structures"),(0,r.kt)("li",{parentName:"ul"},"Compliance with Python standards and modern usages (eg.: ",(0,r.kt)("a",{parentName:"li",href:"https://www.python.org/dev/peps/pep-0008/"},"PEP8"),")")),(0,r.kt)("h2",{id:"workflow"},"Workflow"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"img",src:n(92161).Z,width:"757",height:"313"})),(0,r.kt)("h2",{id:"airflow-pipeline"},"Airflow Pipeline"),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"img",src:n(78423).Z,width:"1905",height:"451"})))}u.isMDXComponent=!0},78423:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/img1-d40ad99ca209f001b524211dc78e37f5.png"},92161:(e,t,n)=>{n.d(t,{Z:()=>a});const a=n.p+"assets/images/img2-ef7720b7795fb1625a0aa6c04e27cb2f.png"}}]);