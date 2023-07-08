"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[26258],{3905:(e,t,r)=>{r.d(t,{Zo:()=>d,kt:()=>f});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var s=n.createContext({}),c=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},d=function(e){var t=c(e.components);return n.createElement(s.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},p=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,d=l(e,["components","mdxType","originalType","parentName"]),p=c(r),f=a,m=p["".concat(s,".").concat(f)]||p[f]||u[f]||o;return r?n.createElement(m,i(i({ref:t},d),{},{components:r})):n.createElement(m,i({ref:t},d))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,i=new Array(o);i[0]=p;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:a,i[1]=l;for(var c=2;c<o;c++)i[c]=r[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}p.displayName="MDXCreateElement"},98807:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>u,frontMatter:()=>o,metadata:()=>l,toc:()=>c});var n=r(87462),a=(r(67294),r(3905));const o={},i="Amazon Redshift ML",l={unversionedId:"storage/lab-redshift-ml/README",id:"storage/lab-redshift-ml/README",title:"Amazon Redshift ML",description:"In this Lab, we will Create, Train and Deploy Multi Layer Perceptron (MLP) models using Amazon Redshift ML.",source:"@site/docs/02-storage/lab-redshift-ml/README.md",sourceDirName:"02-storage/lab-redshift-ml",slug:"/storage/lab-redshift-ml/",permalink:"/docs/storage/lab-redshift-ml/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{}},s={},c=[],d={toc:c};function u(e){let{components:t,...r}=e;return(0,a.kt)("wrapper",(0,n.Z)({},d,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"amazon-redshift-ml"},"Amazon Redshift ML"),(0,a.kt)("p",null,"In this Lab, we will Create, Train and Deploy Multi Layer Perceptron (MLP) models using Amazon Redshift ML."),(0,a.kt)("p",null,"Here we use the Credit Card Fraud detection data available at ",(0,a.kt)("a",{parentName:"p",href:"https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud"},"https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud")," to create, train and deploy MLP model which\ncan be used further to identify fraudulent transactions from the newly captured transaction records."),(0,a.kt)("p",null,"For that, we have downloaded the dataset from the mentioned URL and identified the schema of the CSV file that comes with the downloaded content."),(0,a.kt)("p",null,"We first create a table in Amazon Redshift which should hold the data.\nOne can even keep this CSV file in S3, crawl it using AWS Glue and/or catalog it using Amazon Athena to prepare an external table which can be queried for training the MLP model."),(0,a.kt)("p",null,"Here we choose the option to create a table inside the Amazon Redshift cluster (or Amazon Redshift serverless endpoint)."),(0,a.kt)("p",null,"This is the code we use for training the fraud-detection MLP model:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"CREATE model creditcardsfrauds_mlp\nFROM (select * from creditcardsfrauds where txtime < 120954)\nTARGET class \nFUNCTION creditcardsfrauds_mlp_fn\nIAM_ROLE DEFAULT\nMODEL_TYPE MLP\nSETTINGS (\n      S3_BUCKET '<<your-amazon-s3-bucket>>'',\n      MAX_RUNTIME 54000\n);\n")))}u.isMDXComponent=!0}}]);