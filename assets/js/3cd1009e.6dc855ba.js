"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[19411],{3905:(e,t,a)=>{a.d(t,{Zo:()=>h,kt:()=>d});var o=a(67294);function s(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function n(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,o)}return a}function r(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?n(Object(a),!0).forEach((function(t){s(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):n(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function i(e,t){if(null==e)return{};var a,o,s=function(e,t){if(null==e)return{};var a,o,s={},n=Object.keys(e);for(o=0;o<n.length;o++)a=n[o],t.indexOf(a)>=0||(s[a]=e[a]);return s}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(o=0;o<n.length;o++)a=n[o],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(s[a]=e[a])}return s}var l=o.createContext({}),c=function(e){var t=o.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):r(r({},t),e)),a},h=function(e){var t=c(e.components);return o.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},m=o.forwardRef((function(e,t){var a=e.components,s=e.mdxType,n=e.originalType,l=e.parentName,h=i(e,["components","mdxType","originalType","parentName"]),m=c(a),d=s,u=m["".concat(l,".").concat(d)]||m[d]||p[d]||n;return a?o.createElement(u,r(r({ref:t},h),{},{components:a})):o.createElement(u,r({ref:t},h))}));function d(e,t){var a=arguments,s=t&&t.mdxType;if("string"==typeof e||s){var n=a.length,r=new Array(n);r[0]=m;var i={};for(var l in t)hasOwnProperty.call(t,l)&&(i[l]=t[l]);i.originalType=e,i.mdxType="string"==typeof e?e:s,r[1]=i;for(var c=2;c<n;c++)r[c]=a[c];return o.createElement.apply(null,r)}return o.createElement.apply(null,a)}m.displayName="MDXCreateElement"},58486:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>r,default:()=>p,frontMatter:()=>n,metadata:()=>i,toc:()=>c});var o=a(87462),s=(a(67294),a(3905));const n={},r="Messflix (hypothetical)",i={unversionedId:"storage/casestudy-messflix-hypothetical",id:"storage/casestudy-messflix-hypothetical",title:"Messflix (hypothetical)",description:"Messflix, a movie- and TV-show streaming platform, just hit a wall. A\xa0data\xa0wall. The company has all the data in the world but complains about not even being able to build a proper recommendation system for its movies and shows. The competition seems to be able to get it done; in fact, the competition is famous for being the first movers in a lot of technology sectors.",source:"@site/docs/02-storage/casestudy-messflix-hypothetical.md",sourceDirName:"02-storage",slug:"/storage/casestudy-messflix-hypothetical",permalink:"/docs/storage/casestudy-messflix-hypothetical",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"BigQuery",permalink:"/docs/storage/bigquery"},next:{title:"Cassandra",permalink:"/docs/storage/cassandra"}},l={},c=[],h={toc:c};function p(e){let{components:t,...n}=e;return(0,s.kt)("wrapper",(0,o.Z)({},h,n,{components:t,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"messflix-hypothetical"},"Messflix (hypothetical)"),(0,s.kt)("p",null,"Messflix, a movie- and TV-show streaming platform, just hit a wall. A\xa0",(0,s.kt)("em",{parentName:"p"},"data"),"\xa0wall. The company has all the data in the world but complains about not even being able to build a proper recommendation system for its movies and shows. The competition seems to be able to get it done; in fact, the competition is famous for being the first movers in a lot of technology sectors."),(0,s.kt)("p",null,"Other companies in equally complex industries seem to be able to put their data to work. Messflix does work with data, and analysts are able to get some insights from it, but the organization's leaders don't feel like they can call themselves\xa0",(0,s.kt)("em",{parentName:"p"},"data driven"),"."),(0,s.kt)("p",null,'The data science trial runs seem to all end in "pretty prototypes" with no clear business value. The data scientists tell their managers that it\'s because the "product team just doesn\'t want to put these great prototypes on the roadmap," or, in another instance, "because the data from the source is way too messy and inconsistent."'),(0,s.kt)("p",null,"In short, Messflix hopefully sounds like your average business, which for some reason doesn't feel like it's able to\xa0",(0,s.kt)("em",{parentName:"p"},"let the right data flow to the right use cases"),". The data landscape, just like the technology landscape, has grown organically over time and has become quite complex."),(0,s.kt)("p",null,"The two key technology components of Messflix are its Messflix Streaming Platform and Hitchcock Movie Maker. The streaming platform does just what it says: enable subscribers to watch shows and movies. The movie maker is a set of tools helping the movie production teams choose good movie topics, themes, and content."),(0,s.kt)("p",null,"Additionally, Messflix has a data lake with an analytics platform on top of it taking data from everywhere. A few teams manage these components. The teams Orange and White together operate a few of the Hitchcock Movie Maker tools. Team Green is all about the subscriptions, the log-in processes, etc., and team Yellow is responsible for getting things on the screen inside the streaming platform. Figure below depicts a rough architecture sketch of a few of these components before we briefly discuss how data is currently handled at Messflix."),(0,s.kt)("p",null,(0,s.kt)("img",{alt:"img",src:a(17047).Z,width:"636",height:"758"})),(0,s.kt)("p",null,'The Data team gets data into the data warehouse from a few different places---for example, cost statements from the Hitchcock Movie Maker and subscriptions from the subscriptions service. The team also gets streaming data and subscription profiles from the data lake. Then the Data team does some number crunching to transform this data into information for fraud analysis and business decisions. Finally, this information is used by decentralized units to make those business decisions and for other use cases. This currently is a centralized workflow. The data team "sits in the middle."'),(0,s.kt)("p",null,"No matter where you're coming from and where you want to go, you will find yourself somewhere along the Messflix journey. So let's take one final look at the complete journey Messflix is going through. No data journey is a simple straight line. Likewise, we don't pretend that the Messflix journey is a simple linear progression of a series of steps."))}p.isMDXComponent=!0},17047:(e,t,a)=>{a.d(t,{Z:()=>o});const o=a.p+"assets/images/FM_F01_Siwiak-14f823ac871adb25cdc5ae03254f5a91.png"}}]);