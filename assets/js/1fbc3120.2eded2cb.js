"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[48726],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>p});var n=a(67294);function i(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function s(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?s(Object(a),!0).forEach((function(t){i(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):s(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function r(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},s=Object.keys(e);for(n=0;n<s.length;n++)a=s[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(n=0;n<s.length;n++)a=s[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}var l=n.createContext({}),d=function(e){var t=n.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},c=function(e){var t=d(e.components);return n.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,i=e.mdxType,s=e.originalType,l=e.parentName,c=r(e,["components","mdxType","originalType","parentName"]),m=d(a),p=i,h=m["".concat(l,".").concat(p)]||m[p]||u[p]||s;return a?n.createElement(h,o(o({ref:t},c),{},{components:a})):n.createElement(h,o({ref:t},c))}));function p(e,t){var a=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var s=a.length,o=new Array(s);o[0]=m;var r={};for(var l in t)hasOwnProperty.call(t,l)&&(r[l]=t[l]);r.originalType=e,r.mdxType="string"==typeof e?e:i,o[1]=r;for(var d=2;d<s;d++)o[d]=a[d];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},79399:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>o,default:()=>u,frontMatter:()=>s,metadata:()=>r,toc:()=>d});var n=a(87462),i=(a(67294),a(3905));const s={},o="Disease Diagnosis and Medic Recommendation System",r={unversionedId:"data-modeling/lab-disease-diagnosis/README",id:"data-modeling/lab-disease-diagnosis/README",title:"Disease Diagnosis and Medic Recommendation System",description:"In our ever-evolving world, there are those who frequently relocate to new locations, such as students like us, expats, who without giving a thought to their safety and well being engage in extensive social interaction, consume unusual delicacies, follow unhealthy lifestyles which includes erratic sleep activity, unsafe sexual practices, intense smoking and drinking, and little to no physical exercise. This may result in anumber of illnesses and other health issues that are difficult to treat promptly. Being away from one's own country is difficult but at times not knowing where to reach for the right medical care can even cause death. The main goal of this lab is to aid expats and students who are away from home in finding and obtaining medical care as soon as possible.",source:"@site/docs/04-data-modeling/lab-disease-diagnosis/README.md",sourceDirName:"04-data-modeling/lab-disease-diagnosis",slug:"/data-modeling/lab-disease-diagnosis/",permalink:"/docs/data-modeling/lab-disease-diagnosis/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Create a Data Model for Online Shopping Carts",permalink:"/docs/data-modeling/lab-cassandra-shopping-cart-data-model/"},next:{title:"Postgres Pagila",permalink:"/docs/data-modeling/lab-dvd-rental-datamodel/"}},l={},d=[{value:"Tasks",id:"tasks",level:2}],c={toc:d};function u(e){let{components:t,...a}=e;return(0,i.kt)("wrapper",(0,n.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"disease-diagnosis-and-medic-recommendation-system"},"Disease Diagnosis and Medic Recommendation System"),(0,i.kt)("p",null,"In our ever-evolving world, there are those who frequently relocate to new locations, such as students like us, expats, who without giving a thought to their safety and well being engage in extensive social interaction, consume unusual delicacies, follow unhealthy lifestyles which includes erratic sleep activity, unsafe sexual practices, intense smoking and drinking, and little to no physical exercise. This may result in anumber of illnesses and other health issues that are difficult to treat promptly. Being away from one's own country is difficult but at times not knowing where to reach for the right medical care can even cause death. The main goal of this lab is to aid expats and students who are away from home in finding and obtaining medical care as soon as possible."),(0,i.kt)("p",null,"Our database comprises data  for around 200-300 diseases along with its criticality and symptoms. It will assist the user in matching his/her symptoms to diseases. The database will also comprise of doctors working in Massachusetts along with their area of expertise. In-depth diagnoses can be made  by the user as a result of this. And it would also help the user in locating a doctor and obtaining the necessary treatment on time. Furthermore, our database will also be able to help the user in locating a doctor upon multiple parameters such as a) Location b) Consulting Cost c) Gender d) Education e) Private/Public Consultations."),(0,i.kt)("h2",{id:"tasks"},"Tasks"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Develop a MySQL database that recommends medical professionals for patients based on location, cost, gender, and education"),(0,i.kt)("li",{parentName:"ol"},"Gather structured data from Health websites and Twitter using web-scraping techniques, analyze and transform it with Python's Pandas and NumPy libraries achieving 98% data accuracy and data completeness (already done)"),(0,i.kt)("li",{parentName:"ol"},"Load normalized database tables with clean data to eliminate data redundancy, create SQL views resulting in 100% database organization and visualize data using Seaborn library in Python")))}u.isMDXComponent=!0}}]);