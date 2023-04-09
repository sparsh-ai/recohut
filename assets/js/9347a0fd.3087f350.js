"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[90033],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>u});var i=a(67294);function o(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function n(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,i)}return a}function r(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?n(Object(a),!0).forEach((function(t){o(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):n(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,i,o=function(e,t){if(null==e)return{};var a,i,o={},n=Object.keys(e);for(i=0;i<n.length;i++)a=n[i],t.indexOf(a)>=0||(o[a]=e[a]);return o}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(i=0;i<n.length;i++)a=n[i],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(o[a]=e[a])}return o}var l=i.createContext({}),d=function(e){var t=i.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):r(r({},t),e)),a},c=function(e){var t=d(e.components);return i.createElement(l.Provider,{value:t},e.children)},h={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},p=i.forwardRef((function(e,t){var a=e.components,o=e.mdxType,n=e.originalType,l=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),p=d(a),u=o,g=p["".concat(l,".").concat(u)]||p[u]||h[u]||n;return a?i.createElement(g,r(r({ref:t},c),{},{components:a})):i.createElement(g,r({ref:t},c))}));function u(e,t){var a=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var n=a.length,r=new Array(n);r[0]=p;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:o,r[1]=s;for(var d=2;d<n;d++)r[d]=a[d];return i.createElement.apply(null,r)}return i.createElement.apply(null,a)}p.displayName="MDXCreateElement"},5517:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>r,default:()=>h,frontMatter:()=>n,metadata:()=>s,toc:()=>d});var i=a(87462),o=(a(67294),a(3905));const n={},r="Gradient Boosting",s={unversionedId:"datascience/algorithms/gradient-boosting",id:"datascience/algorithms/gradient-boosting",title:"Gradient Boosting",description:"Gradient Boosting describes a certain technique in modeling with a variety of different algorithms that are based upon it. The first successful algorithm that utilizes Gradient Boosting is AdaBoost (Adaptive Gradient Boosting) in 1998 formulated by Leo Breiman. In 1999, Jerome Friedman composed the generalization of boosting algorithms emerging at this time, such as AdaBoost, into a single method: Gradient Boosting Machines. Quickly, the idea of Gradient Boosting Machines became extremely popular and proved to be high performing in many real-life tabular datasets. To this day, various Gradient Boosting algorithms such as AdaBoost, XGBoost, and LightGBM are the first choice for many data scientists operating on large, difficult datasets.",source:"@site/docs/10-datascience/algorithms/gradient-boosting.md",sourceDirName:"10-datascience/algorithms",slug:"/datascience/algorithms/gradient-boosting",permalink:"/docs/datascience/algorithms/gradient-boosting",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Decision Trees",permalink:"/docs/datascience/algorithms/decision-trees"},next:{title:"K-Nearest Neighbors",permalink:"/docs/datascience/algorithms/knn"}},l={},d=[{value:"AdaBoost",id:"adaboost",level:2},{value:"XGBoost",id:"xgboost",level:2},{value:"LightGBM",id:"lightgbm",level:2}],c={toc:d};function h(e){let{components:t,...a}=e;return(0,o.kt)("wrapper",(0,i.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"gradient-boosting"},"Gradient Boosting"),(0,o.kt)("p",null,"Gradient Boosting describes a certain technique in modeling with a variety of different algorithms that are based upon it. The first successful algorithm that utilizes Gradient Boosting is AdaBoost (Adaptive Gradient Boosting) in 1998 formulated by Leo Breiman. In 1999, Jerome Friedman composed the generalization of boosting algorithms emerging at this time, such as AdaBoost, into a single method: Gradient Boosting Machines. Quickly, the idea of Gradient Boosting Machines became extremely popular and proved to be high performing in many real-life tabular datasets. To this day, various Gradient Boosting algorithms such as AdaBoost, XGBoost, and LightGBM are the first choice for many data scientists operating on large, difficult datasets."),(0,o.kt)("p",null,"Gradient Boosting operates on similar ideas to those of Random Forest, using an ensemble of weaker models to build one, strong prediction. What differentiates Gradient Boosting from Random Forest is that instead of having individual, uncorrelated models, Gradient Boosting constructs models that are based on others\u2019 errors to continuously \u201cboost\u201d the performance."),(0,o.kt)("p",null,"Say you\u2019re picking a team of five people to represent your school, organization, or country at a trivia tournament in which the team that can answer the most questions about music, history, literature, mathematics, science, etc. wins. What is your strategy? You could pick five people who each have broad and overlapping knowledge of most topics likely to be covered (a Random Forest\u2013style ensembling approach). Perhaps a better approach is to pick a person A who\u2019s really good in one area, then pick and train person B on the topics that person A isn\u2019t a specialist in, then pick and train person C on the topics that person B isn\u2019t a specialist in, and so on. By boosting learners on top of each other, we can build sophisticated and adaptive ensembles."),(0,o.kt)("p",null,"The concept of Gradient Boosting can be adapted to many different machine learning models such as Linear Regression, Decision Trees, and even deep learning methods. However, the most common use of Gradient Boosting is in conjunction with Decision Trees or tree-based methods in general. Although there have emerged various popular Gradient Boosting models, their initial and core intuition relies on the same algorithm; thus, we will be analyzing the original Gradient Boosting process while briefly going over the differences in each specific type of Boosting model."),(0,o.kt)("p",null,"Gradient Boosting naively adapts to both regression and classification. We can start by understanding the regression approach first as demonstrated in the following figure:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Assuming the target variable is continuous, create a leaf with the average of the targets, which represents our initial guess of the labels."),(0,o.kt)("li",{parentName:"ol"},"Build a Regression Tree based on the errors of the first leaf. More specifically",(0,o.kt)("ul",{parentName:"li"},(0,o.kt)("li",{parentName:"ul"},"Calculate the error between our initial prediction and ground-truth labels for every sample, which we refer to as pseudo residuals."),(0,o.kt)("li",{parentName:"ul"},"Construct a Regression Tree to predict the pseudo residuals of samples with a restricted number of leaves. Replace leaves with more than one label with the average of all labels that are in the leaf, which will be the prediction for that leaf."))),(0,o.kt)("li",{parentName:"ol"},"Predict the target variables with a trained Decision Tree as follows:",(0,o.kt)("ul",{parentName:"li"},(0,o.kt)("li",{parentName:"ul"},"Start with the initial prediction, which is the average of all labels."),(0,o.kt)("li",{parentName:"ul"},"Predict pseudo residuals using the Decision Trees we trained."),(0,o.kt)("li",{parentName:"ul"},"Add predictions to the initial guess multiplied by a factor that we refer to as the learning rate, which becomes the final prediction."))),(0,o.kt)("li",{parentName:"ol"},"Calculate new pseudo residuals based on the prediction of the previous model(s)."),(0,o.kt)("li",{parentName:"ol"},"Construct a new tree to predict the new pseudo residuals, repeating steps 2\u20134. For step 3, we simply add the new tree\u2019s prediction and multiply by the same learning rate along with other trees that were created in previous iterations."),(0,o.kt)("li",{parentName:"ol"},"Repeat steps 2\u20134 until the maximum specified models are reached or the predictions start to worsen.")),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/230726029-f8fa6cc3-52f1-480c-9f61-cb19d97009f7.jpeg",alt:"525591_1_En_1_Fig59_HTML"})),(0,o.kt)("p",null,"The approach for Gradient Boosting classification is extremely like regression. During our first initial \u201cguess,\u201d instead of the average across targets, we compute the log odds on the labels. In order to calculate the pseudo residuals, we convert the log odds to probability using the sigmoid function."),(0,o.kt)("h2",{id:"adaboost"},"AdaBoost"),(0,o.kt)("p",null,"Adaptive Gradient Boosting, or AdaBoost, is one of the earliest forms of Gradient Boosting. It was published before the generalization of Gradient Boosting Machines was proposed. The main idea that drives AdaBoost lies in the fact it uses weighted stumps, which combine into the final prediction. A stump is a Decision Tree with a root and only two leaves."),(0,o.kt)("h2",{id:"xgboost"},"XGBoost"),(0,o.kt)("p",null,"XGBoost, short for Extreme Gradient Boosting, was developed in the early 2010s as a regularized variation of Gradient Boosting Machines. The development of XGBoost began as a research project by Tianqi Chen as part of the Distributed Machine Learning Community. It was then later popularized to the Machine Learning and Data Science Community during the Higgs Boson Machine Learning competition in 2014. Compared with AdaBoost, XGBoost is a lot more optimized for speed and performance and closely resembles the original approach of Gradient Boosting Machines."),(0,o.kt)("h2",{id:"lightgbm"},"LightGBM"),(0,o.kt)("p",null,"LightGBM, short for Light Gradient Boosting Machines, is an optimized Gradient Boosting algorithm that aims for reduced memory usage and speed while keeping the performance high. Developed by Microsoft in 2016, LGBM quickly gained popularity due to the advantages stated above along with its capability of handling large-scale data with parallel computing on GPUs."),(0,o.kt)("p",null,"One major difference between LGBM and other similar Gradient Boosting algorithms is the fact that Decision Trees grow leaf-wise in LGBM, while in other cases they grow level-wise. Leaf-wise growth handles overfitting better than level-wise and is much faster when operating on large datasets. Additionally, level-wise growth produces many unnecessary leaves and nodes. In contrast, leaf-wise growth only expands on nodes with high performance, thus keeping the number of decision nodes constant."),(0,o.kt)("p",null,"Furthermore, LGBM samples the datasets using two novel techniques known as Gradient-Based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB), which reduce the size of the dataset without affecting performance."),(0,o.kt)("p",null,"GOSS samples the dataset aiming for the model to focus on data points where there\u2019s a larger error. By the concept of gradient descent, samples with lower gradients produce lower training error and vice versa. GOSS selects samples with a greater absolute gradient. Note that GOSS also chooses samples that have relatively lower gradients as it keeps the distribution of the output data like before GOSS."),(0,o.kt)("p",null,"The goal of EFB is to eliminate, or more appropriately merge, features. The algorithm bundles features that are mutually exclusive, meaning that they could never be of the same value simultaneously. The bundled features are then converted to a single feature, reducing the size and dimensionality of the dataset."),(0,o.kt)("p",null,"Finally, LGBM performs binning on continuous features to decrease the number of possible splits during Decision Tree building, introducing another major speedup to the algorithm."))}h.isMDXComponent=!0}}]);