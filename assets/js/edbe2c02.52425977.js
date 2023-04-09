"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[73412],{3905:(e,t,r)=>{r.d(t,{Zo:()=>d,kt:()=>p});var o=r(67294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function s(e,t){if(null==e)return{};var r,o,n=function(e,t){if(null==e)return{};var r,o,n={},a=Object.keys(e);for(o=0;o<a.length;o++)r=a[o],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(o=0;o<a.length;o++)r=a[o],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var c=o.createContext({}),l=function(e){var t=o.useContext(c),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},d=function(e){var t=l(e.components);return o.createElement(c.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},m=o.forwardRef((function(e,t){var r=e.components,n=e.mdxType,a=e.originalType,c=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),m=l(r),p=n,h=m["".concat(c,".").concat(p)]||m[p]||u[p]||a;return r?o.createElement(h,i(i({ref:t},d),{},{components:r})):o.createElement(h,i({ref:t},d))}));function p(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var a=r.length,i=new Array(a);i[0]=m;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:n,i[1]=s;for(var l=2;l<a;l++)i[l]=r[l];return o.createElement.apply(null,i)}return o.createElement.apply(null,r)}m.displayName="MDXCreateElement"},69865:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>c,contentTitle:()=>i,default:()=>u,frontMatter:()=>a,metadata:()=>s,toc:()=>l});var o=r(87462),n=(r(67294),r(3905));const a={title:"Short-video Background Music Recommender",authors:"sparsh",tags:["recsys"]},i=void 0,s={permalink:"/blog/2021/10/01/short-video-background-music-recommender",source:"@site/blog/2021-10-01-short-video-background-music-recommender.mdx",title:"Short-video Background Music Recommender",description:"Matching micro-videos with suitable background music can help uploaders better convey their contents and emotions, and increase the click-through rate of their uploaded videos. However, manually selecting the background music becomes a painstaking task due to the voluminous and ever-growing pool of candidate music. Therefore, automatically recommending background music to videos becomes an important task.",date:"2021-10-01T00:00:00.000Z",formattedDate:"October 1, 2021",tags:[{label:"recsys",permalink:"/blog/tags/recsys"}],readingTime:2.17,hasTruncateMarker:!1,authors:[{name:"Sparsh Agarwal",title:"Data Scientist & Engineer",url:"https://github.com/sparsh-ai",email:"sprsag@gmail.com",imageURL:"https://github.com/sparsh-ai.png",key:"sparsh"}],frontMatter:{title:"Short-video Background Music Recommender",authors:"sparsh",tags:["recsys"]},prevItem:{title:"Semantic Similarity",permalink:"/blog/2021/10/01/semantic-similarity"},nextItem:{title:"The progression of analytics in enterprises",permalink:"/blog/2021/10/01/the-progression-of-analytics-in-enterprises"}},c={authorsImageUrls:[void 0]},l=[],d={toc:l};function u(e){let{components:t,...a}=e;return(0,n.kt)("wrapper",(0,o.Z)({},d,a,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("p",null,"Matching micro-videos with suitable background music can help uploaders better convey their contents and emotions, and increase the click-through rate of their uploaded videos. However, manually selecting the background music becomes a painstaking task due to the voluminous and ever-growing pool of candidate music. Therefore, automatically recommending background music to videos becomes an important task."),(0,n.kt)("p",null,"In ",(0,n.kt)("a",{parentName:"p",href:"https://arxiv.org/pdf/2107.07268.pdf"},"this")," paper, Zhu et. al. shared their approach to solve this task. They first collected ~3,000 background music from popular TikTok videos and also ~150,000 video clips that used some kind of background music. They named this dataset ",(0,n.kt)("inlineCode",{parentName:"p"},"TT-150K"),"."),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"An exemplar subset of videos and their matched background music in the established TT-150k dataset",src:r(6050).Z,width:"902",height:"688"})),(0,n.kt)("p",null,"An exemplar subset of videos and their matched background music in the established TT-150k dataset"),(0,n.kt)("p",null,"After building the dataset, they worked on modeling and proposed the following architecture:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"Proposed CMVAE (Cross-modal Variational Auto-encoder) framework",src:r(90746).Z,width:"1041",height:"532"})),(0,n.kt)("p",null,"Proposed CMVAE (Cross-modal Variational Auto-encoder) framework"),(0,n.kt)("p",null,"The goal is to represent videos (",(0,n.kt)("inlineCode",{parentName:"p"},"users")," in recsys terminology) and music (",(0,n.kt)("inlineCode",{parentName:"p"},"items"),") in a shared latent space. To achieve this, CMVAE use pre-trained models to extract features from unstructured data - ",(0,n.kt)("inlineCode",{parentName:"p"},"vggish")," model for audio2vec, ",(0,n.kt)("inlineCode",{parentName:"p"},"resnet")," for video2vec and ",(0,n.kt)("inlineCode",{parentName:"p"},"bert-multilingual")," for text2vec.  Text and video vectors are then fused using product-of-expert approach. "),(0,n.kt)("p",null,"It uses the reconstruction power of variational autoencoders to 1) reconstruct video from music latent vector and, 2) reconstruct music from video latent vector. In layman terms, we are training a neural network that will try to guess the video activity just by listening background music, and also try to guess the background music just by seeing the video activities. "),(0,n.kt)("p",null,"The joint training objective is $\\mathcal{L}",(0,n.kt)("em",{parentName:"p"},"{(z_m,z_v)} = \\beta \\cdot\\mathcal{L}"),"{cross","_","recon} - \\mathcal{L}",(0,n.kt)("em",{parentName:"p"},"{KL} + \\gamma \\cdot \\mathcal{L}"),"{matching}$, where $\\beta$ and $\\gamma$ control the weight of the cross reconstruction loss and the matching loss, respectively."),(0,n.kt)("p",null,"After training the model, they compared the model's performance with existing baselines and the results are as follows:"),(0,n.kt)("p",null,(0,n.kt)("img",{alt:"/img/content-blog-raw-blog-short-video-background-music-recommender-untitled-2.png",src:r(47967).Z,width:"1240",height:"450"})),(0,n.kt)("p",null,(0,n.kt)("strong",{parentName:"p"},"Conclusion"),": I don't make short videos myself but can easily imagine the difficulty in finding the right background music. If I have to do this task manually, I will try out 5-6 videos and select one that I like. But here, I will be assuming that my audience would also like this music. Moreover, feedback is not actionable because it will create kind of an implicit sub-conscious effect (because when I see a video, I mostly judge it at overall level and rarely notice that background music is the problem). So, this kind of recommender system will definitely help me in selecting a better background music. Excited to see this feature soon in TikTok, Youtube Shorts and other similar services."))}u.isMDXComponent=!0},90746:(e,t,r)=>{r.d(t,{Z:()=>o});const o=r.p+"assets/images/content-blog-raw-blog-short-video-background-music-recommender-untitled-1-81086e3ba53f8bc9648682e6f1b367ed.png"},47967:(e,t,r)=>{r.d(t,{Z:()=>o});const o=r.p+"assets/images/content-blog-raw-blog-short-video-background-music-recommender-untitled-2-0002224cfc03822d344479f3766cd1ec.png"},6050:(e,t,r)=>{r.d(t,{Z:()=>o});const o=r.p+"assets/images/content-blog-raw-blog-short-video-background-music-recommender-untitled-8e4334cad8c9ec206ebdba19b1163b61.png"}}]);