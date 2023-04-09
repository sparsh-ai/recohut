"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[87166],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>d});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function s(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var l=n.createContext({}),c=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),m=c(r),d=a,f=m["".concat(l,".").concat(d)]||m[d]||p[d]||o;return r?n.createElement(f,i(i({ref:t},u),{},{components:r})):n.createElement(f,i({ref:t},u))}));function d(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,i=new Array(o);i[0]=m;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var c=2;c<o;c++)i[c]=r[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},6946:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>p,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var n=r(87462),a=(r(67294),r(3905));const o={},i="Ternary",s={unversionedId:"assignments/ternary/README",id:"assignments/ternary/README",title:"Ternary",description:"Prompt",source:"@site/docs/11-assignments/ternary/README.md",sourceDirName:"11-assignments/ternary",slug:"/assignments/ternary/",permalink:"/docs/assignments/ternary/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Spotify Extract Load Airflow",permalink:"/docs/assignments/spotify-extract-load/"},next:{title:"Assignment: Extract Data from Twitter API and Load into AWS S3",permalink:"/docs/assignments/twitter-s3/"}},l={},c=[{value:"Prompt",id:"prompt",level:2},{value:"Requirements",id:"requirements",level:2},{value:"Submission Guidelines",id:"submission-guidelines",level:2}],u={toc:c};function p(e){let{components:t,...r}=e;return(0,a.kt)("wrapper",(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"ternary"},"Ternary"),(0,a.kt)("h2",{id:"prompt"},"Prompt"),(0,a.kt)("p",null,"At Ternary, we are eager to find ways to help customers gain visibility into all types of cloud services, especially those they may not be paying attention to. One of the areas that often go neglected and result in high costs is bucket storage \u2013 Google Cloud Storage (GCS)."),(0,a.kt)("p",null,"In this assignment, please develop a tool that can collect bucket object storage size data from a particular GCS bucket. The tool should take as input the bucket URI and collect the storage information for each object. Then save the usage information into a data format that can be used to generate a chart / report (e.g. Excel) showing either size per bucket or size per object. You can find storage client examples ",(0,a.kt)("a",{parentName:"p",href:"https://cloud.google.com/storage/docs/reference/libraries"},"here"),"."),(0,a.kt)("p",null,"Ternary has set up a bucket with some files in it for your convenience, but please feel free to set up your own bucket if you so desire.  You can find the bucket here:gs://ternary-public. We\u2019ve granted the following ",(0,a.kt)("a",{parentName:"p",href:"https://cloud.google.com/storage/docs/access-control/iam-roles"},"roles")," to the email we have on file, but if you\u2019d prefer access via a different email, please let us know the email address: Storage Object Viewer, Storage Legacy Bucket Reader."),(0,a.kt)("h2",{id:"requirements"},"Requirements"),(0,a.kt)("p",null,"While this is meant to be an open prompt, here are some minimum requirements to guide your development and give you a better sense of completion."),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"The tool is able to analyze the size of the input storage bucket and objects.",(0,a.kt)("ul",{parentName:"li"},(0,a.kt)("li",{parentName:"ul"},"Extra credit if the tool can analyze multiple buckets, or even all buckets in a particular project."))),(0,a.kt)("li",{parentName:"ul"},"The tool generates a file that can be loaded into a visualization tool of your choice."),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("strong",{parentName:"li"},"Hint"),": Try using Excel/Sheets to plot a chart."),(0,a.kt)("li",{parentName:"ul"},"Please attach some screenshots of charts or images from your created reporting.")),(0,a.kt)("h2",{id:"submission-guidelines"},"Submission Guidelines"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"Email the source code as a zip or tarball or create a GitHub repo."),(0,a.kt)("li",{parentName:"ul"},"Provide instructions via README for running the app locally on Linux or Mac OS (e.g. make, shell script, ...) Note any required dependencies that must be installed."),(0,a.kt)("li",{parentName:"ul"},"(Recommended but optional) Provide a Docker build for automating the build process and distribution of the final product.")))}p.isMDXComponent=!0}}]);