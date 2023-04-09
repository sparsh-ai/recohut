"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[99520],{3905:(e,t,r)=>{r.d(t,{Zo:()=>p,kt:()=>b});var n=r(67294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function s(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var l=n.createContext({}),c=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},p=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=c(r),b=a,h=u["".concat(l,".").concat(b)]||u[b]||d[b]||o;return r?n.createElement(h,i(i({ref:t},p),{},{components:r})):n.createElement(h,i({ref:t},p))}));function b(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,i=new Array(o);i[0]=u;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var c=2;c<o;c++)i[c]=r[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},49096:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>d,frontMatter:()=>o,metadata:()=>s,toc:()=>c});var n=r(87462),a=(r(67294),r(3905));const o={title:"OCR experiments",authors:"sparsh",tags:["ocr","vision"]},i=void 0,s={permalink:"/blog/2021/10/01/ocr-experiments",source:"@site/blog/2021-10-01-ocr-experiments.mdx",title:"OCR experiments",description:"/img/content-blog-raw-blog-ocr-experiments-untitled.png",date:"2021-10-01T00:00:00.000Z",formattedDate:"October 1, 2021",tags:[{label:"ocr",permalink:"/blog/tags/ocr"},{label:"vision",permalink:"/blog/tags/vision"}],readingTime:1.155,hasTruncateMarker:!1,authors:[{name:"Sparsh Agarwal",title:"Data Scientist & Engineer",url:"https://github.com/sparsh-ai",email:"sprsag@gmail.com",imageURL:"https://github.com/sparsh-ai.png",key:"sparsh"}],frontMatter:{title:"OCR experiments",authors:"sparsh",tags:["ocr","vision"]},prevItem:{title:"Object detection with YOLO3",permalink:"/blog/2021/10/01/object-detection-with-yolo3"},nextItem:{title:"PDF to Wordcloud via Mail",permalink:"/blog/2021/10/01/pdf-to-wordcloud-via-mail"}},l={authorsImageUrls:[void 0]},c=[{value:"1. Tesseract",id:"1-tesseract",level:2},{value:"2. EasyOCR",id:"2-easyocr",level:2},{value:"3. KerasOCR",id:"3-kerasocr",level:2},{value:"4. ArabicOCR",id:"4-arabicocr",level:2}],p={toc:c};function d(e){let{components:t,...o}=e;return(0,a.kt)("wrapper",(0,n.Z)({},p,o,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("p",null,(0,a.kt)("img",{alt:"/img/content-blog-raw-blog-ocr-experiments-untitled.png",src:r(62948).Z,width:"602",height:"360"})),(0,a.kt)("h2",{id:"1-tesseract"},"1. Tesseract"),(0,a.kt)("p",null,"Tesseract is an open-source text recognition engine that is available under the Apache 2.0 license and its development has been sponsored by Google since 2006."),(0,a.kt)("p",null,(0,a.kt)("a",{parentName:"p",href:"https://nbviewer.jupyter.org/gist/sparsh-ai/2d1f533048a3655de625298c3dd32d47"},"Notebook on nbviewer")),(0,a.kt)("h2",{id:"2-easyocr"},"2. EasyOCR"),(0,a.kt)("p",null,"Ready-to-use OCR with 70+ languages supported including Chinese, Japanese, Korean and Thai. EasyOCR is built with Python and Pytorch deep learning library, having a GPU could speed up the whole process of detection. The detection part is using the CRAFT algorithm and the Recognition model is CRNN. It is composed of 3 main components, feature extraction (we are currently using Resnet), sequence labelling (LSTM) and decoding (CTC). EasyOCR doesn\u2019t have much software dependencies, it can directly be used with its API."),(0,a.kt)("p",null,(0,a.kt)("a",{parentName:"p",href:"https://nbviewer.jupyter.org/gist/sparsh-ai/12359606ee4127513c66fc3b4ff18e5b"},"Notebook on nbviewer")),(0,a.kt)("h2",{id:"3-kerasocr"},"3. KerasOCR"),(0,a.kt)("p",null,"This is a slightly polished and packaged version of the Keras CRNN implementation and the published CRAFT text detection model. It provides a high-level API for training a text detection and OCR pipeline and out-of-the-box OCR models, and an end-to-end training pipeline to build new OCR models."),(0,a.kt)("p",null,(0,a.kt)("a",{parentName:"p",href:"https://nbviewer.jupyter.org/gist/sparsh-ai/2fcb764619baf5f56cf7122b1b2c527c"},"Notebook on nbviewer")),(0,a.kt)("h2",{id:"4-arabicocr"},"4. ArabicOCR"),(0,a.kt)("p",null,"It is an OCR system for the Arabic language that converts images of typed text to machine-encoded text. It currently supports only letters (29 letters).  ArabicOCR aims to solve a simpler problem of OCR with images that contain only Arabic characters (check the dataset link below to see a sample of the images)."),(0,a.kt)("p",null,(0,a.kt)("a",{parentName:"p",href:"https://nbviewer.jupyter.org/gist/sparsh-ai/26df76b78f8cd2018a068b284b7cfe56"},"Notebook on nbviewer")))}d.isMDXComponent=!0},62948:(e,t,r)=>{r.d(t,{Z:()=>n});const n=r.p+"assets/images/content-blog-raw-blog-ocr-experiments-untitled-7efe4530732678d915b7176ba9205352.png"}}]);